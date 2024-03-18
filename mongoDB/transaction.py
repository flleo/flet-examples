import itertools
import os
from random import random

from bson import ObjectId

import services.credentials as cr

id_iter = itertools.count()


# Define the sequence of operations to perform inside the trasactions
def callback(
        session,
        transfer_id=None,
        account_id_receiver=None,
        account_id_sender=None,
        transfer_amount=None
):
    accounts_collection = session.client.bank.accounts
    transfer_collection = session.client.bank.transfers

    transfer = {
        'transfer_id': transfer_id,
        'to_account': account_id_receiver,
        'from_account': account_id_sender,
        'amount': {'$numberDecimal': transfer_amount}
    }

    # We must pass the session to each operation

    # Update sender account
    accounts_collection.update_one(
        {'account_id': account_id_sender},
        {
            '$inc': {'balance': -transfer_amount},
            '$push': {'transfers_complete': transfer_id}
        },
        session=session
    )

    # Update receiver account
    accounts_collection.update_one(
        {'account_id': account_id_receiver},
        {
            '$inc': {'balance': transfer_amount},
            '$push': {'transfers_complete': transfer_id}
        },
        session=session
    )

    transfer_collection.insert_one(transfer, session=session)

    print('Transaction successful')

    return


def callback_wrapper(s):
    callback(
        s,
        transfer_id=next(id_iter),
        account_id_receiver=1,
        account_id_sender=0,
        transfer_amount=50
    )


# Start a client session, then start a transaction
with cr.client.start_session() as session:
    # If a operation fail, all the operation fail, with_transaction
    session.with_transaction(callback_wrapper)

cr.client.close()
