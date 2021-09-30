import datetime
import random

class personInfo :

    def __init__(self,name,lastname,nationalCode,phoneNumber) :
      self.name=name
      self.lastname=lastname
      self.phone=phoneNumber
      self.nationalCode = nationalCode
      self.role=""
    
    def printInfo(self):
      print("--------------------------------")
      print("Personal Information")
      print(f"NAME : {self.name}")
      print(f"Lastname : {self.lastname}")
      print(f"National code : {self.nationalCode}")
      print(f"Phone : {self.phone}")

class newAccount(personInfo) :

      def __init__(self, name, lastname, nationalCode, phoneNumber,deposit,time):
          super().__init__(name, lastname, nationalCode, phoneNumber)
          self.deposit = deposit
          self.time = time
          self.accountType = ""
          self.accountNumber= random.randint(100000000000,99999999999999)

      def accountTypeChoice(self) :
          account = ["Savings account","Current loan account","Short term deposit account","Long-term deposit account"]
          while 1 == 1 :
               print("Please choice your Account Type :")
               print("1) Savings account")
               print("2) Current loan account")
               print("3) Short term deposit account")
               print("4) Long-term deposit account")
               choice = input()
               choices=["1","2","3","4"]
               if choice in choices :
                   choice = int(choice) -1
                   self.accountType = account[choice]
                   break 

      def showAccount(self):
          super().printInfo() 
          print("--------------------------------")
          print("Account Information")
          print(f"Deposit value (toman) : {self.deposit}")
          print(f"Deposit Type : {self.accountType}")
          print(f"Account Number : {self.accountNumber}")  
          print(f"Account Foundation Date :\n{self.time}")

class newloan (personInfo):

    def __init__(self, name, lastname, nationalCode, phoneNumber,loanValue):
          super().__init__(name, lastname, nationalCode, phoneNumber)
          self.loanValue = loanValue
          self.date = datetime.datetime.now()
          self.loanType = ""
          self.Guaranter= {
                "GuaranterName" : [],
                "GuaranterFullname" : [],
                "GuaranterNationalCode" : [],
                "phone" : []
          }
      
    def newGuaranter(self) :
        name = ""
        while 1 == 1 :
            name = input("Name : ")
            correct = 0
            for item in name :
              if item.isnumeric() :
                   correct -=- 1
            if correct == 0 : break
            else : print("Wrong Inpute !\n( Name doesn't have Number )")
        lastName = ""
        while 1 == 1 :
            lastName = input("Last Name : ")
            correct = 0
            for item in lastName :
                  if item.isnumeric() :
                        correct -=- 1
            if correct == 0 : break
            else : print("Wrong Inpute !\n( Last Name doesn't have Number )")
            nationalCode = ""
        while 1 == 1 :
               nationalCode = input("National Code : ")
               correct = 0
               for item in nationalCode :
                   if item.isalpha() :  correct -=- 1
               if correct == 0 and len(nationalCode) == 10 : break
               elif correct != 0 :print("Wrong Inpute !\n( National Code doesn't have character )")
               elif len(nationalCode) != 10 : print("Wrong Inpute !\n( National Code range error )")

        phone = ""
        while 1 == 1 :
               phone = input("Phone Number : ")
               correct = 0
               for item in phone :
                    if item.isalpha() : correct -=- 1
               if correct == 0 and len(phone) == 11 and phone[0] == "0" : break
               elif correct != 0 : print("Wrong Inpute !\n( Phone number doesn't have character )")
               elif len(phone) != 11 : print("Wrong Inpute !\n( Phone number range error )")
               elif phone[0] != 0 :  print("Wrong Inpute !\n( Phone number starts with \"0\" )")

        self.Guaranter['GuaranterName'].append(name)
        self.Guaranter['GuaranterFullname'].append(lastName)
        self.Guaranter['GuaranterNationalCode'].append(nationalCode)
        self.Guaranter['phone'].append(phone)
    
    def loanTypeChoice(self):
        while 1==1 :
            print("Please choice your Loan Type :")
            print("1) Marriage Loan\n2) Mortgage\n3) Commodity Loan\n4) Car Loan")
            choice = input()
            choices=["1","2","3","4"]
            loanList=["Marriage Loan","Mortgage","Commodity Loan","Car Loan"]
            if choice in choices :
                   choice = int(choice) -1
                   self.loanType = loanList[choice]
                   break 

    def loanshow(self):
          super().printInfo() 
          print("--------------------------------")
          print("Loan Information")
          print(f"Loan value (toman) : {self.loanValue}")
          print(f"Loan Type : {self.loanType}")
          print("--------------------------------")
          i=0
          Guaranters = ["First","Second"]
          while i < 2 :
                print(f"{Guaranters[i]} Guaranter :")
                print(f"Guaranter Name : {self.Guaranter['GuaranterName'][i]}")
                print(f"Guaranter Fullname : {self.Guaranter['GuaranterFullname'][i]}")
                print(f"Guaranter National Code : {self.Guaranter['GuaranterNationalCode'][i]}")
                print(f"Guaranter Phone : {self.Guaranter['phone'][i]}")
                i-=-1
          if len(self.Guaranter['GuaranterName']) :
               print("Extra Guaranters :")
               while i < len(self.Guaranter['GuaranterName']) :
                    print(f"{Guaranters[i]} Guaranter :")
                    print(f"Guaranter Name : {self.Guaranter['GuaranterName'][i]}")
                    print(f"Guaranter Fullname : {self.Guaranter['GuaranterFullname'][i]}")
                    print(f"Guaranter National Code : {self.Guaranter['GuaranterNationalCode'][i]}")
                    print(f"Guaranter Phone : {self.Guaranter['phone'][i]}")
                    i-=-1        
          print(f"Loan Date :\n{self.date}")

class application(personInfo):
     def __init__(self, name, lastname, nationalCode, phoneNumber,username,password):
         super().__init__(name, lastname, nationalCode, phoneNumber)
         self.username=username
         self.password=password
         self.phoneNumber=phoneNumber
         self.date = datetime.datetime.now()
     
     def forget(self) :
         phone = ""
         while 1 == 1 :
               phone = input("Please enter your Phone Number : ")
               correct = 0
               for item in phone :
                    if item.isalpha() : correct -=- 1
               if correct == 0 and len(phone) == 11 and phone[0] == "0" and phone == self.phoneNumber : break
               elif correct != 0 : print("Wrong Inpute !\n( Phone number doesn't have character )")
               elif len(phone) != 11 : print("Wrong Inpute !\n( Phone number range error )")
               elif phone[0] != 0 :  print("Wrong Inpute !\n( Phone number starts with \"0\" )")
               elif phone != self.phoneNumber : print("Wrong Inpute !\n( invalid Number )")
         print(f"SMS For {self.phoneNumber} :\nusername : {self.username}\npassword :{self.password}\nPlease keep this informations !")
         self.login

     def login(self) :
        print("log in :")
        while 1==1 :
           print("User name :")
           loginUsername=input()
           if loginUsername == self.username :  break
           else : 
               print("its wrong !\n1)Try Again\netc.forget your username ?")
               choice = input()
               if choice != "1"  :
                   self.forget()  
        while 1==1 :
          print("password :")
          loginPassword=input()
          if loginPassword in self.password :break
          else :
               print("its wrong !\n1)Try Again\netc.forget your password ?")
               choice = input()
               if choice != "1"  :
                   self.forget() 
        self.menu() 

     def menu(self):
        while 1 == 1:
          print("what do you want Sir/Madam ?\n1) New Account\n2) Take Loan")  
          choice = input()
          if choice == "1" : newAccountFunc()
          elif choice == "2" : newloanFunc()

     def showAccount(self):
          super().printInfo()  
          print(f"Account Foundation Date :\n{self.date}")


def main():
    while 1 == 1:
        print("Welcome to our BANK ")
        print("1) New Account")
        print("2) Take Loan")
        print("3) Mobile Application")
        print("4) EXIT")
        choice = input()
        if choice == "1" : newAccountFunc()
        elif choice == "2" : newloanFunc()
        elif choice == "3" : applicationFunc()
        elif choice == "4" : break

def newAccountFunc() :
    print("please enter Your \" Personal Details \" :")
    name = ""
    while 1 == 1 :
        name = input("Name : ")
        correct = 0
        for item in name :
            if item.isnumeric() : correct -=- 1
        if correct == 0 : break
        else : print("Wrong Inpute !\n( Name doesn't have Number )")
    
    lastName = ""
    while 1 == 1 :
        lastName = input("Last Name : ")
        correct = 0
        for item in lastName :
            if item.isnumeric() : correct -=- 1
        if correct == 0 : break
        else : print("Wrong Inpute !\n( Last Name doesn't have Number )")
    
    nationalCode = ""
    while 1 == 1 :
        nationalCode = input("National Code : ")
        correct = 0
        for item in nationalCode :
            if item.isalpha() : correct -=- 1 
        if correct == 0 and len(nationalCode) == 10 : break
        elif correct != 0 : print("Wrong Inpute !\n( National Code doesn't have character )")
        elif len(nationalCode) != 10 : print("Wrong Inpute !\n( National Code range error )")

    phone = ""
    while 1 == 1 :
        phone = input("Phone Number : ")
        correct = 0
        for item in phone :
            if item.isalpha() : correct -=- 1
        if correct == 0 and len(phone) == 11 and phone[0] == "0" : break
        elif correct != 0 : print("Wrong Inpute !\n( Phone number doesn't have character )")
        elif len(phone) != 11 : print("Wrong Inpute !\n( Phone number range error )")
        elif phone[0] != 0 : print("Wrong Inpute !\n( Phone number starts with \"0\" )")
    
    print("please enter Your \" Account Details \" :")
    deposit = input("Deposit amout (toman) :")

    person = newAccount(name,lastName,nationalCode,phone,deposit,datetime.datetime.now())
    person.accountTypeChoice()
    person.showAccount()

    exitChoice = input("Press any key to EXIT !")
    if exitChoice or exitChoice == "0" : main() 

def newloanFunc() :
    print("please enter Your \" Personal Details \" :")
    name = ""
    while 1 == 1 :
        name = input("Name : ")
        correct = 0
        for item in name :
            if item.isnumeric() : correct -=- 1
        if correct == 0 : break
        else : print("Wrong Inpute !\n( Name doesn't have Number )")
    
    lastName = ""
    while 1 == 1 :
        lastName = input("Last Name : ")
        correct = 0
        for item in lastName :
            if item.isnumeric() : correct -=- 1
        if correct == 0 : break
        else : print("Wrong Inpute !\n( Last Name doesn't have Number )")
    
    nationalCode = ""
    while 1 == 1 :
        nationalCode = input("National Code : ")
        correct = 0
        for item in nationalCode :
            if item.isalpha() : correct -=- 1
        if correct == 0 and len(nationalCode) == 10 : break
        elif correct != 0 : print("Wrong Inpute !\n( National Code doesn't have character )")
        elif len(nationalCode) != 10 : print("Wrong Inpute !\n( National Code range error )")

    phone = ""
    while 1 == 1 :
        phone = input("Phone Number : ")
        correct = 0
        for item in phone :
            if item.isalpha() : correct -=- 1
        if correct == 0 and len(phone) == 11 and phone[0] == "0" : break
        elif correct != 0 : print("Wrong Inpute !\n( Phone number doesn't have character )")
        elif len(phone) != 11 : print("Wrong Inpute !\n( Phone number range error )")
        elif phone[0] != 0 : print("Wrong Inpute !\n( Phone number starts with \"0\" )")
    
    print("please enter Your \" Account Details \" :")
    loanvalue = input("Loan amout (toman) : ")

    person = newloan(name,lastName,nationalCode,phone,loanvalue)

    Guaranters = ["First","Second"]
    i=0
    while i<2 :
        print(f"Please enter the {Guaranters[i]} Guaranter :")
        person.newGuaranter()
        i-=-1

    while 1==1 :
        print("1) Extra Guaranters\netc.Exit")
        choice = input()
        if choice == "1" : person.newGuaranter()
        else : break
    
    person.loanTypeChoice()
    person.loanshow()
    
    exitChoice = input("Press any key to EXIT !")
    if exitChoice or exitChoice == "0" : main() 
 
def applicationFunc():
    print("please enter Your \" Personal Details \" :")
    name = ""
    while 1 == 1 :
        name = input("Name : ")
        correct = 0
        for item in name :
            if item.isnumeric() : correct -=- 1
        if correct == 0 : break
        else : print("Wrong Inpute !\n( Name doesn't have Number )")
    
    lastName = ""
    while 1 == 1 :
        lastName = input("Last Name : ")
        correct = 0
        for item in lastName :
            if item.isnumeric() : correct -=- 1
        if correct == 0 : break
        else : print("Wrong Inpute !\n( Last Name doesn't have Number )")
    
    nationalCode = ""
    while 1 == 1 :
        nationalCode = input("National Code : ")
        correct = 0
        for item in nationalCode :
            if item.isalpha() : correct -=- 1
        if correct == 0 and len(nationalCode) == 10 : break
        elif correct != 0 : print("Wrong Inpute !\n( National Code doesn't have character )")
        elif len(nationalCode) != 10 : print("Wrong Inpute !\n( National Code range error )")

    phone = ""
    while 1 == 1 :
        phone = input("Phone Number : ")
        correct = 0
        for item in phone :
            if item.isalpha() : correct -=- 1
        if correct == 0 and len(phone) == 11 and phone[0] == "0" : break
        elif correct != 0 : print("Wrong Inpute !\n( Phone number doesn't have character )")
        elif len(phone) != 11 : print("Wrong Inpute !\n( Phone number range error )")
        elif phone[0] != 0 : print("Wrong Inpute !\n( Phone number starts with \"0\" )")
    
    print("please enter Your \" Account Details \" :")
    username=input("username : ")
    while 1==1 :
         print("please enter your username again :")
         usernameCheck=input()
         if usernameCheck == username : break    
         else : print("its wrong !")
    while 1==1 :
        print("your password Should have :\n1) Upper and Lower Case and Number\n2)Password Character Range (6,20) ")
        password=input("Password : ")
        correctUpper = False
        correctLower = False
        hasNumber = False

        for item in password :
            if item.isnumeric : hasNumber = True
            if item.isupper : correctUpper = True
            if item.islower : correctLower = True
        
        if hasNumber == True and correctUpper == True and correctLower == True and len(password) > 6 and 20>len(password): break
        if correctUpper == False : print("your password Should have Upper case Character")
        if correctLower == False : print("your password Should have Lower case Character")
        if hasNumber == False : print("your password Should have Lower case Character")
        if len(password) < 6 or 20<len(password) : print("Range ERROR !")  
    while 1==1 :
         print("please enter your password again :")
         passwordCheck=input()
         if passwordCheck == password : break    
         else : print("its wrong !")
    
    person = application(name,lastName,nationalCode,phone,username,password)
    person.showAccount()
    while 1==1:
        Choice = input("Press any key to Use Application !")
        if Choice or Choice == "0" : person.login()
        exitChoice = input("Press any key to EXIT !")
        if exitChoice or exitChoice == "0" : break

    main()

main()