import random
import re
import csv
import pandas as pd


class Inventory():

    def __init__(self, code, name, price, quantity, size):
        self.code = code
        self.name = name
        self.price = price
        self.quantity = quantity
        self.size = size

    def __str__(self):
        return f'{self.code},{self.name},{self.price},{self.quantity},{self.size}'
    def copy(self):
        return Inventory(self.code,self.name,self.price,self.quantity,self.size)


class Committing_order():

    def __init__(self):
        self.Cart = []

    def addItem(self,item):
        self.Cart.append(item)

    def removeItem(self,item):
        self.Cart.remove(item)

    def viewCart(self):
        for cart in self.Cart:
            print(cart)

    def run(self):
        buy_products = []

def valid_postalcode(postlcode):
    pattern1 = re.compile(r'^\d{10}$')
    return bool(pattern1.match(postalcode))

def valid_cardnumber(cardnumber):
    pattern2 = re.compile(r'^\d{16}$')
    return bool(pattern2.match(cardnumber))


class outgoing_orders():
    instance = None
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(outgoing_orders,cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.morning_orders = 0
        self.noon_orders = 0
        self.afternoon_orders = 0

    def determine_delivery_time(self):
        print("Please choose sending time :")

        print("Morning")

        if self.noon_orders < 3:
            print("Noon")

        if self.afternoon_orders < 3:
            print("Afternoon")

        time = input()

        if time == 'Morning':
            self.morning_orders += 1

        if time == 'Noon':
            self.noon_orders += 1

        if time == 'Afternoon':
            self.afternoon_orders += 1

        return time


logestic = outgoing_orders()

while True:

    print("Please Select Your Role :", "\n", "1: Sellers' Panel", "\n", "2: Buyers' Panel", "\n",
          "3: Close the application")

    panel = int(input())

    if panel == 1:

        while True:

            print(''' 
                  1: Add products to your inventory.
                  2: Change quantity of your products.
                  3: Back to select role menu.
                  4: َAccounting
                  5: Back to select role menu.
                  ''')

            work = int(input())

            if work == 1:

                n = int(input("How many products do you want to add to your inventory: "))
                inventory = []

                for i in range(n):
                    pro = Inventory(
                        code = int(input('Enter the Code of Your Product : ')),
                        name = input('Enter the Name of Your Product : '),
                        price = int(input('Enter the Price of Your Product :  ')),
                        quantity = int(input('Enter the Quantity of Your Product : ')),
                        size = int(input('Enter the Size of Your Product : '))
                    )
                    inventory.append(pro)

            elif work == 2:

                p = []
                p = inventory
                print('''
                      1: Edit with csv File.
                      2: Manual Edit.
                      ''')

                how = int(input())

                if how == 1:

                    df = pd.read_excel("add File location")

                    rows = df.values.tolist()

                    code = []

                    for i in rows:

                        for j in p:

                            code.append(j.code)

                            if i[0] in code:
                                a = code.index(i[0])

                                p[a].quantity = i[1]

                elif how == 2:

                    how_many = int(input("How many products do you want to change their quantity ?   "))

                    for i in range(how_many):

                        code = int(input("Enter the code of your product: "))
                        new_quantity = int(input("Enter the new quantity of your product: "))

                        for j in p:

                            if j.code == code:
                                j.quantity = new_quantity

            elif work == 3:

                c = []
                q = []
                l = []

                for i in range(len(inventory)):
                    c.append(inventory[i].code)
                    q.append(inventory[i].quantity)
                    l.append(1)

                dict = {"Code": c, "Quantity": q, "Inventory_code": l}

                df = pd.DataFrame(dict)
                df.to_csv("inventory.csv")
                print(df)

            elif work == 4:
                acc = open('Accounting.txt', "r")
                accountant = acc.read()
                print(accountant)
                acc.close()

            elif work == 5:

                break












