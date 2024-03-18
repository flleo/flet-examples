import datetime
import itertools

id_iter = itertools.count()


class Account:
    def __init__(self, account_holder: str, account_type: str, balance, minimum_balance, transfers_complete: []):
        super().__init__()
        self.account_id = next(id_iter)
        self.account_holder = account_holder
        self.account_type = account_type
        self.balance = balance
        self.minimum_balance = minimum_balance
        self.transfers_complete = transfers_complete
        self.last_updated = datetime.datetime.now(datetime.UTC)

