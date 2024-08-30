# searching expenses by date (linear search)

def search_date(transaction,target):
    for n in transaction:
        if n["date"]==target:
            return n


 # sorting the dates based on  amount without using sort() function and using bubble sort
def sort_date(transactions):
    n=len(transaction)
    for i in range(n):
        for j in range(0,n-1):
            if int(transaction[j]["amount"])>(transaction[j+1]["amount"]):
                transaction[j],transaction[j+1]=transaction[j+1],transaction[j]
    return transactions
 
# Add data (taking input from the user--date,amount,description)
def  add_data(transaction):
    date=input("Enter the date: ")
    amount=int(input("Enter the amount: "))
    description=input("Enter the description: ")
    
    new_transaction={ "date":date,"amount":amount, "desc":description}
    transaction.append(new_transaction)
    return transaction


# Delete a dictionary based on date
def delete_data(transaction):
    date=input("Enter the search date:")
    for i in transaction:
        if i["date"]==date:
            transaction.remove(i)
        return transaction
