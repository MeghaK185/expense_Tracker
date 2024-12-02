print('                 EXPENSE TRACKER          ')
print("      -----------------------------------    ")

dict={}
option=0
budget=0
s=0
while option<=7:
      print("--ENTER--")
      print("1.INITIAL AMOUNT")
      print("2.ADD INITIAL AMOUNT")
      print("3.ENTER EXPENSE")
      print("4.VIEW EXPENSE")
      print("5.EDIT EXPENSE")
      print("6.DELETE EXPENSE")
      print("7.EXIT")
      try:
            while True:
                  option=int(input("Enter your option:"))
                  if option>0:
                        break
                  else:
                        print("Enter values between 1-7")
            if option==1:
                  if budget!=0:
                        print("Budget is already entered!!!")
                  else:
                        budget=int(input("Enter your budget:"))
                        print(" ")
                        print("Initial Amount=  ",budget)
                        print("EXPENSE-","  AMOUNT")
                        print("--------","--------")
                        for i,j in dict.items():
                              print(i,"     ",j)
                  print("-----------------")
                  print("Balance: ",budget)
            elif option == 2:
                  while True:
                        try:
                              add_amount = int(input("Enter the amount to be added: "))
                              if add_amount > 0:
                                   break
                              else:
                                   print("invalid input. try again!!!! ")

                        except:
                              print("Invalid input. Please enter a valid number.")
                  budget += add_amount
                  print("Current budget is",budget)
            elif option==3:
                  if budget==0:
                        print("You must enter the budget first!")
                  
                  bal=0
                  for i,j in dict.items():
                        bal=bal+j
                  bal=budget-bal
                  if bal==0:
                        print("Your budget is low!")
                  else:
                        while True:
                              exp_name=input("Enter expense:")
                              if exp_name=="":
                                    print("You must enter a value first")  
                              else:
                                    break

                        while True:
                              try:
                                    exp_amt=int(input("Enter the amount of expense:"))
                                    if exp_amt>0:
                                          break
                                    else:
                                          print("invalid input!!!!")
                              except:
                                    print("Invalid input. Please enter a valid integer for the expense amount.")

                  if bal<exp_amt:
                        print("Your budget is low.Try after adding new budget!!!")      
                  else:
                        dict[exp_name]=exp_amt
                        bal=0
                        print("Initial amount: ",budget)
                        print("EXPENSE-","  AMOUNT")
                        print("--------","--------")
                        for i,j in dict.items():
                              print(i,"     ",j)
                              bal=bal+j
                        print("-----------------")
                        print("Balance: ",budget-bal)

            elif option==4:
                  print("Initial amount: ",budget)
                  print("EXPENSE-","  AMOUNT")
                  print("--------","--------")
                  for i,j in dict.items():
                        print(i,"     ",j)
                  print("---------------")
                  print("Balance: ",budget)
            elif option==5:
                  if budget==0:
                        print("You must enter the budget first!")
                  else:
                        old_name=input("Enter the expense you want to edit:")
                        if old_name in dict:
                              while True:
                                    new_name=input("change to:")
                                    if new_name in dict:
                                          print("item already exists. enter another name!!")
                                    else:
                                          if new_name=="":
                                                print("You must Enter a value first!!!")
                                          else:
                                                break
                  dict[new_name]=dict[old_name]  
                  dict.pop(old_name)
                  print("edited succesfully...")
            elif option==6:
                  if budget==0:
                        print("You must enter the budget first!")
                  else:
                        while True:
                              name=input("Enter expense to be deleted:")
                              if name=="":
                                    print("You must enter a value first!!!")
                              else:
                                    break
                        if name in dict:
                              dict.pop(name)
                              print("deleted successfully.")
                              bal=0
                              print("   ")
                              print("Initial amount: ",budget)
                              print("EXPENSE-","  AMOUNT")
                              print("--------","--------")
                              for i,j in dict.items():
                                    print(i,"     ",j)
                                    bal=bal+j
                              print("---------------")
                              print("Balance: ",budget-bal)
            else: 
                  if option==7:
                        print("exiting......")
                        break
      except:
            print("Enter a valid value.")      
