# class classname:
#     name="sai"
#     emp_id=1234
#     def details(self):
#         print(f"The company name is ABC {self.name}")
#     def details_2(self):
#         print("The company is very powerful")

# ss=classname()
# ss.details()
# ss.details_2()
# print(ss.name)



# class person_details():#class definition
#     user_name = "kiran" #attributes
#     emp_id = 1234 #attributes
#     def details(self,):#method 1
#         print(f"he works at ABC company..{self.user_name}")
#     def details2(self,): #method 2
#         print(f"he owns ABC company..")
#         self.details()
# kiran_sagar = person_details()
# kiran_sagar.details()
# kiran_sagar.details2()
# print(kiran_sagar.user_name)
# print(kiran_sagar.emp_id)



# class feature_phone:
#     brand="nokia"
#     color="black"
#     model="2021"
#     def calling(self):
#         print(f"The phone is calling...{self.brand}")
#     def message(self):
#         print("the phone is message...") 

# sp=feature_phone()
# sp.calling()
# sp.message()   


# class feature_phone():
#     def __init__(self,brand,color,model):
#         self.brand = brand
#         self.color = color
#         self.model = model
#     def calling(self,mn):
#         print(f"you are calling from {self.brand}....... {mn}")
#     def message(self,text):
#         print(f"{text} sent successfully.............")
# class smart_phones(feature_phone):
#     def capture(self,):
#         print(f"photo has been captured {self.brand}")
#     def browsing(self,browser):
#         print(f"browsing from {browser}")
# obj = smart_phones("nokia","white",2018)
# obj.calling(12348549879)
# obj.message("hi")
# obj.capture()
# obj.browsing("chrome")

# # task 31--> Practice using classes and objects by writing a program to create Laptop object.
# class laptap():
#     def __init__(self,brand,color,model):
#         self.brand=brand
#         self.color=color
#         self.model=model
#     def feature_laptap(self):
#         print(f"The laptap feature are brand is {self.brand},color is {self.color},model is {self.model}")
#     def browsing(self,browser):
#         print(f"you are browsing in the computer {browser}")
#     def typing(self):
#         print("You are typing in the laptap")

# lp=laptap("HP","Silver","windows")
# lp.feature_laptap()
# lp.browsing("chrome")
# lp.typing()





# task 32--> 
# Implement an ATM program using object-oriented programming (OOP) concepts class object inheritance
class ATM1():
    def __init__(self,bank,branch,location,balance=1000):
        self.bank=bank
        self.branch=branch
        self.location=location
        self._balance=balance
        self.transactions=[]
    def display(self):
        print("Bank:",self.bank)
        print("Branch:",self.branch)
        print("Location:",self.location)
    def credit(self):
        amount=float(input("Enter a amount:"))
        if amount<=0:
            print("please enter a postivie amount")
        else:
            self._balance+=amount
            self.transactions.append(f"Creited:${amount:.2f}")
        print(f"${amount:.2f} credited in your account.")

    def debit(self):
        amount=float(input("Enter amount to withdraw:"))
        if amount<=0:
            print("please enter a postivie amount")
        elif amount>self._balance:
            print("Insufficient balance.")
        else:
            self._balance-=amount
            self.transactions.append(f"Dedited:$ {amount:.2f}")
        print(f"{amount:.2f} is dedited in your account. ")
class atm2(ATM1):
    def check_balance(self):
        print(f"your current balance is {self._balance:.2f}")
    def ministatement(self):
        print("-----MINI STATEMENT------")
        if not self.transactions:
            print("No transaction found")
        else:
            for i in self.transactions:
                print(i)
        print(f"Available Balance: ${self._balance:.2f}")
class user(atm2):
    def menu(self):
        while True:
            print("\n------ ATM MENU ------")
            print("1. Credit")
            print("2. Debit")
            print("3. Balance")
            print("4. Mini Statement")
            print("5. Exit")
            choice = input("Enter your choice (1-5): ")
            if choice == '1':
                self.credit()
            elif choice == '2':
                self.debit()
            elif choice == '3':
                self.check_balance()          
            elif choice == '4':
                self.ministatement()
            elif choice == '5':
                 print("Thank you for using the ATM. Goodbye!")
                 break
            else:
                print("Invalid choice. Please try again.")
obj = user("SBI", "Ramakuppam", "Kuppam")
obj.display()
obj.menu()
