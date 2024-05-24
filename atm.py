#we will make a simple atm using python today.

print("Welcome to Abc bank Atm")
amount=10000
while True:
 pin=int(input("Enter Your Pin Here:"))
 if pin==1234:
    option1=int(input("Select The Following from The options Given Below:\n1.Withdraw\n2.Deposit\n3.Balance Inquiry\n4.Exit:"))
    if option1==1:
        withamt=int(input("Enter the Amount to Withdraw:"))
        if withamt<=amount:
            amount=amount-withamt
            print("Amount successfully withdraw.Bal Left",amount)
        else:
            print("Not Enough Balance In Your Account.")
            
    if option1==2:
        depoamt=int(input("Enter The amount to be deposited:"))
        amount=amount+depoamt
        print("Your amount successfully deposited,Current Acc Balance:",amount)
        
    if option1==3:
        print(amount)
    
    if option1==4:
        print("Thanks For visiting us..Come again.")
        break    

        

