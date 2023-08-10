'''class Bank:
    def __init__(self, account_number, name, balance):
        self._account_number = account_number
        self._name = name
        self._balance = balance
       # self._transcount = 1
        self.__tlist = [("d", balance)]
    def get_name(self):
        return self._name
    def set_name(self):
        self._name = name
    def get_account_number(self):
        return self._account_number
    def set_account_number(self):
        self._account_number = account_number
    def get_balance(self):
        return self._balance
    def set_balance(self):
        self._balance = balance
    def deposit(self,cashin):
       # self._transcount += 1
        self._balance += cashin
        return self._balance
        self.__tlist.append(("d",cashin))
    def withdraw(self, cashout):
        if (self._balance-cashout <= 0):
            print("Balance is too low to make a withdraw")
            self.__tlist.append(("r",cashout))
        else:
            #self._transcount += 1
            self._balance -= cashout
            return self._balance
        self.__tlist.append(("w",cashout))
    def trans_count(self):
        #return self._transcount
        return len(self.__tlist)
        
bank = Bank("3200100198", "Amanda AK", 500000)
cust_name = bank.get_name()
cust_acc_no = bank.get_account_number()
cur_bal = bank.get_balance()
print("Customer's name:", cust_name)
print("Account Number:", cust_acc_no)
print("Current Account Balance:", cur_bal)
while True:
    deposit = bank.deposit(int(input("Enter amount to deposit:" )))
    print("New balance after deposit:", deposit)
    withdraw = bank.withdraw(int(input("Enter amount to withdraw:" )))
    print("New balance after withdraw:", withdraw)
    print("You have performed",bank.trans_count() , "transactions today.")
    quit '''
def common_data(list1, list2):
    for x in list1:
        for y in list2:
            if (x == y):
                result = True
                return result
print(common_data([1,2,3,4,5], [1,2,3,4,5]))
print(common_data([1,2,3,4,5], [1,7,8,9,510]))
print(common_data([1,2,3,4,5], [6,7,8,9,10]))
