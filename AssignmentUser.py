# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified

# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150

# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance

class User:

    # constructor
    def __init__(self, n = "", amt = 0):
        self.name = n
        self.amount = amt

    # class method
    # @classmethod


    # methods
    def make_deposit(self, amount):
        self.amount += amount
        return self

    def make_withdrawal(self, amount):
        self.amount -= amount
        return self

    def display_user_balance(self):
        print(self.amount)
        return self

    def transfer_money(self, other_user, amount):
        self.amount -= amount
        other_user.amount += amount
        return self

    
#################################

ericUser = User("Eric", 1000)
robyUser = User("Roby", 100)
zackUser = User("Zack", 3000)

ericUser.display_user_balance().make_deposit(199).display_user_balance()

ericUser.display_user_balance().make_withdrawal(1).display_user_balance()

print()

ericUser.display_user_balance().make_deposit(399).display_user_balance()

robyUser.display_user_balance().make_withdrawal(3).display_user_balance()

print()

robyUser.display_user_balance()
ericUser.display_user_balance()
robyUser.transfer_money(ericUser, 30).display_user_balance()
ericUser.display_user_balance()

