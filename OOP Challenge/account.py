class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt
        print('Deposit Accepted')

    def withdraw(self, amt):
        if self.balance >= amt:
            self.balance -= amt
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')

    def __str__(self):
        info_str = (
            'Account owner:   {}\n'
            'Account balance: ${}'
        )
        return info_str.format(self.owner, self.balance)

acct1 = Account('Jose', 100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)