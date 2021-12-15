#"Budget App" by HL

class Category:
    '''This class handles information for a budget journal based on a single category type'''
    def __init__(self, name):
        '''This initializes the class Category with a name for the category and an empty list for the ledger and budget of 0'''
        self.name = name
        self.ledger = []
        self.budget = 0

    def __str__(self):
        '''Provides a printout of the total spent and on what from self.ledger'''
        printout = ''
        for integer in self.ledger:
            description = integer['description']
            amount = format(integer['amount'], '.2f')
            printout = printout + description[:23]+ amount.rjust(30-len(description[:23])) +'\n'
        printout = str(self.name.center(30,'*') + '\n' + printout + 'Total: ' + format(self.budget, '.2f'))
        return printout

    def deposit(cls, amount, description = ''):
        '''Method that accepts amount and description to append to self.ledger as a positive amount
        Parameters: amount (a numerical amount), description (default an empty string)
        Returns: the appended ledger for the category'''
        cls.budget = cls.budget + amount
        depositdict = {"amount": amount, "description": description}
        return cls.ledger.append(depositdict)

    def withdraw(cls, amount, description = ''):
        '''Method that accepts amount and description to append to self.ledger as a negative amount
        Parameters: amount (a numerical amount), description (default an empty string)
        Returns: the appended ledger for the category'''
        if cls.check_funds(amount) is False:
            return False
        else:
            cls.budget= cls.budget - amount
            depositdict = {"amount": amount*(-1), "description": description}
            cls.ledger.append(depositdict)
            return True
    def get_balance(cls):
        '''Get method to return current balance amount'''
        return cls.budget

    def transfer(cls, amount, category):
        '''Handles transferring amounts of money between budget categories
        Parameters: amount of money, a different budget object as a cateogry
        Returns: True or False if amount transfer was successful'''
        if cls.check_funds(amount) is False:
            return False
        else:
            cls.withdraw(amount, 'Transfer to ' + category.name)
            category.deposit(amount, 'Transfer from ' + cls.name)
            return True

    def check_funds(cls, amount):
        '''Checks if amount against category's budget
        Parameters: amount of money
        Returns: True or False depending on if budget is greater/less than amount compared'''
        if amount > cls.budget:
            return False
        else:
            return True




def create_spend_chart(categories):
    '''This function takes objects from the class category
    and generates a simple text bar graph representing the proportion of spending that occurred in each category
    Parameters: a list of category objects
    Returns: a string printout bar graph of the amount spent in each category'''
    percentsum = []
    categoryamount = []
    total = 0
    #iterate through categories and ledger list and dictionary to extract negative amounts and add them to new dictionary that is 'category:amount' and add the running amount to a total for future percentage calcuation'
    for integer in categories:
        withdrawal = 0
        for subInteger in integer.ledger:
            if subInteger['amount'] < 0:
                withdrawal = withdrawal + subInteger['amount']
                total = total - subInteger['amount']
        withdict = {integer.name:withdrawal}
        categoryamount.append(withdict)
    #iterate through new categoryamount list and dictionary to calculate percentage spent based on total and append to a list of percentages
    for integer in categoryamount:
        for value in integer.values():
            percentsum.append(value/total*-1)
    printout = ''
    total = 100
    #creates bar graph and adds 0 markers if percentsum is equal to or greater than y
    for integer in range(11):
        printout = printout + (str(total)+'|').rjust(4)
        for number in percentsum:
            if number*100 >=total:
                printout = printout + 'o'.center(3)
            else:
                printout = printout + ' '.center(3)
        printout = printout + ' \n'
        total= total - 10

    printout = 'Percentage spent by category\n' + printout + '----------\n'.rjust(15)
    #figure out longest named category for graph
    maxlen = -1
    for integer in categories:
        if len(integer.name) > maxlen:
            maxlen = len(integer.name)
    #adds names to bar graphs
    for total in range(maxlen+1):
        printout = printout + ' '.rjust(4)
        for integer in range(len(categories)):
            slicestr = str(categories[integer].name)
            printout = printout + slicestr[total:total+1].center(3)
        printout = printout +' \n'
    printout = printout[:-16]
    return printout
