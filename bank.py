'''
This is a simple banking system python program
'''
class Bank:
    bank_account_numbers=[]
    customer_account_relation={}

    def account_exist(self,account_number): # to check if the given account number exist
        if account_number in self.bank_account_numbers:
            return True
        else:
            return False

    def deposit(self,account_number): # to deposit amount
        print("Enter the amount to deposit ")
        deposit_amount=int(input())
        total_balance=0
        acc_deatil=self.customer_account_relation[account_number]
        if 'balance' in acc_deatil.keys():
            total_balance=acc_deatil['balance']
        total_balance=total_balance+deposit_amount
        acc_deatil.update({"balance":total_balance})
        self.customer_account_relation.update({account_number:acc_deatil})
        return total_balance


    def generate_account_number(self,customer_name,customer_address): # to create new account
        if (len(self.bank_account_numbers)==0):
            self.bank_account_numbers.append(1)
        else:
            last_acc = self.bank_account_numbers[-1]
            last_acc=last_acc+1
            self.bank_account_numbers.append(last_acc)
        account_number =self.bank_account_numbers[-1]
        for i in self.bank_account_numbers:
            print(i)
        customer_dist = {}
        customer_dist.update({'name': customer_name})
        customer_dist.update({"address":customer_address})
        self.customer_account_relation.update({account_number:customer_dist})
        return(account_number)



    def check_balance(self,account_number): # to check balance
        acc_deatil = self.customer_account_relation[account_number]
        total_balance=0
        if 'balance' in acc_deatil.keys():
            total_balance = acc_deatil['balance']
        return (total_balance)


    def withdraw(self,account_number): # to withdraw amount
        print("Enter the amount to withdraw")
        amount_withdraw=int(input())
        acc_deatil = self.customer_account_relation[account_number]
        total_balance = 0
        if 'balance' in acc_deatil.keys():
            total_balance = acc_deatil['balance']
        total_balance=total_balance-amount_withdraw
        acc_deatil.update({'balance':total_balance})
        self.customer_account_relation.update({account_number:acc_deatil})
        return (total_balance)


while True:
    try:
        # welcome session
        session=Bank()
        print("Welcome!!!")
        print("1. Open a new Account")
        print("2. Check existing Account")
        user_input=int(input())

        if(user_input==1): # if user want to open new account
            print("Enter name-", end=" ")
            customer_name=str(input())
            print("Enter address-",end=" ")
            customer_address=str(input())
            print("You will need to deposit minimum 500 rupees in you account")
            print("1. To deposit")
            print("2. Cancel and go back")
            customer_input=int(input())

            if(customer_input==1): # deposit in new account
                customer_account_number = session.generate_account_number(customer_name,customer_address)
                customer_balance=session.deposit(customer_account_number)
                print("Blanace for account number {} is - {}".format(customer_account_number,customer_balance))
                continue
            elif(customer_input==2): # go to previous menu
                print("Going back to previous menu.")
                continue
            else:
                print("Invalid input.")
                print("Going back to previous menu.")
                continue
        elif(user_input==2): # access  existing account
            print("Enter customer id-",end=" ")
            customer_id = int(input())
            if(session.account_exist(customer_id)==False):
                print("This account dose not exist.")
                continue
            while True: # existing account menu
                print("Customer Menu-")
                print("1. Check Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Exit")
                customer_action=int(input())


                if(customer_action==1):# check balance
                    customer_balance=session.check_balance(customer_id)
                    print("Balance for customer id {} is {}".format(str(customer_id),str(customer_balance)))
                    continue
                elif(customer_action==2):# deposit
                    customer_balance=session.deposit(customer_account_number)
                    print("Blanace for account number {} is - {}".format(customer_account_number,customer_balance))
                    continue
                elif(customer_action==3):#withdraw
                    customer_balance=session.withdraw(customer_account_number)
                    print("Blanace for account number {} is - {}".format(customer_account_number,customer_balance))
                    continue
                elif(customer_action==4):#exit
                    break
                else:
                    print("Invalid input.")
                    print("Going back to previous menu.")
        else:
            print("Invalid input.")
            print("Going back to previous menu.")
            continue
    except ValueError:
        print("ERROR!!! Not a number")
        print("         Please enter a valid account number.",end="\n\n\n")

        continue


