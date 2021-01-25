print("Budget App")
import re
import math


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.budget = 0

    def __str__(self):
        printout = ''
        for i in self.ledger:
            d = i['description']
            a = format(i['amount'], '.2f')
            printout = printout + d[:23]+ a.rjust(30-len(d[:23])) +'\n'
        printout = str(self.name.center(30,'*') + '\n' + printout + 'Total: ' + format(self.budget, '.2f'))
        return printout

    def deposit(cls, amount, description = ''):
        cls.budget = cls.budget + amount
        depositdict = {"amount": amount, "description": description}
        return cls.ledger.append(depositdict)

    def withdraw(cls, amount, description = ''):
        if cls.check_funds(amount) is False:
            return False
        else:
            cls.budget= cls.budget - amount
            depositdict = {"amount": amount*(-1), "description": description}
            cls.ledger.append(depositdict)
            return True
    def get_balance(cls):
        return cls.budget

    def transfer(cls, amount, category):
        if cls.check_funds(amount) is False:
            return False
        else:
            cls.withdraw(amount, 'Transfer to ' + category.name)
            category.deposit(amount, 'Transfer from ' + cls.name)
            return True

    def check_funds(cls, amount):
        if amount > cls.budget:
            return False
        else:
            return True




def create_spend_chart(categories):
    percentsum = []
    categoryamount = []
    withdict = {}
    total = 0
    #iterate through categories and ledger list and dictionary to extract negative amounts and add them to new dictionary that is 'category:amount' and add the running amount to a total for future percentage calcuation'
    for i in categories:
        withdrawal = 0
        for j in i.ledger:
            if j['amount'] < 0:
                withdrawal = withdrawal + j['amount']
                total = total - j['amount']
        withdict = {i.name:withdrawal}
        categoryamount.append(withdict)
    #iterate through new categoryamount list and dictionary to calculate percentage spent based on total and append to a list of percentages
    for i in categoryamount:
        for v in i.values():
            percentsum.append(v/total*-1)
    printout = ''
    x = 100
    #creates bar graph and adds 0 markers if percentsum is equal to or greater than y
    for i in range(11):
        printout = printout + (str(x)+'|').rjust(4)
        for n in percentsum:
            if n*100 >=x:
                printout = printout + 'o'.center(3)
            else:
                printout = printout + ' '.center(3)
        printout = printout + ' \n'
        x= x - 10

    printout = 'Percentage spent by category\n' + printout + '----------\n'.rjust(15)
    #figure out longest named category for graph
    maxlen = -1
    for i in categories:
        if len(i.name) > maxlen:
            maxlen = len(i.name)
    #adds names to bar graphs
    for x in range(maxlen+1):
        printout = printout + ' '.rjust(4)
        for i in range(len(categories)):
            slicestr = str(categories[i].name)
            printout = printout + slicestr[x:x+1].center(3)
        printout = printout +' \n'
    printout = printout[:-16]
    return printout


#Tons of testing code
food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")
#print(food.ledger)
#print(food.ledger)
#food.deposit(37, 'Bananas')
#food.deposit(77, 'Cookies')
#food.withdraw(22,'Bananas')
#print(food.ledger)
#print(food.get_balance())
#food.transfer(9, entertainment)
#print(food.get_balance())
#print(entertainment.get_balance())
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
#print(food.get_balance())
#print(food.ledger)
#print(entertainment.ledger)
#print(repr(str(food)))
#print(repr("*************Food*************\ndeposit                 900.00\nmilk, cereal, eggs, bac -45.67\nTransfer to Entertainme -20.00\nTotal: 834.33"))
#print(create_spend_chart([business, food,entertainment]))
#print(repr(create_spend_chart([business, food,entertainment])))
#print(repr("Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "))
#print(create_spend_chart([business, food,entertainment]))
#print("Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  ")
