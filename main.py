from features import search_date,sort_date,add_data,delete_data
transaction=[ {"date":"10-8-2021","amount":2000,"desc":"fruits"}, 
              {"date":"12-8-2021","amount":3000,"desc":"vegetables"},
              {"date":"18-8-2021","amount":4000,"desc":"groceries"},
              {"date":"20-8-2021","amount":2500,"desc":"bills"},
              {"date":"25-8-2021","amount":1000,"desc":"medicalexpenses"} ]
flag=True 
while flag:
    print("1.ADD")
    print("2.SEARCH")
    print("3.SORT")
    print("4.DELETE")
    print("5.DISPALY")
    print("6.STOP")
    choice=int(input("enter the choice:"))
    if choice==1:
        print("-"*50)
        print("Adding Data")
        print("-"*50)
        transactions=add_data(transaction)
        print("-"*50)
    elif choice==2:
        print("-"*50)
        print("Searching Data")
        print("-"*50)
        transactions=search_date(transaction,target)
        print("-"*50)
    elif choice==3:
        print("-"*50)
        print("Sorting  Data")
        print("-"*50)
        transactions=sort_date(transaction)
        print("-"*50)
    elif choice==4:
        print("-"*50)
        print("Deleting Data")
        print("-"*50)
        transactions=delete_data(transaction)
        print("-"*50)
    elif choice==5:
        print("-"*50)
        print("Displaying  Data")
        print("-"*50)
        print(transaction)
        print("-"*50)
    elif choice==6:
        print("-"*50)
        print("Exiting Application")
        flag=False
        print("-"*50)
    else:
        print("-"*50)
        print("Please enter the corretc choice")
        print("-"*50)
