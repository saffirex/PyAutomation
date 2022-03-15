from itertools import count

#assigning an account number that will be incremental
class account:
    count= count(start=1)
    def __init__(self,name,balance):
        acc_num= next(self.count)
        self.name= name
        self.balance= balance
        print("Hi",name,"your bank acc has been created with Rs.", balance)
    def method_1():
        print("this is the first method")

john= account(name= "John", balance=1500)
