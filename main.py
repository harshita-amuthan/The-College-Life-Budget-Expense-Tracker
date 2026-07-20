budget=float(input("Enter your budget:"))
expenses=[]
while True:
    print("----Budget Expense Tracker----")
    print("1.Add Expenses")
    print("2.View Budget Summary")
    print("3.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        catergory=input("Catergory of Expense:")
        amount=int(input("Enter amount spent:"))
        expenses.append({"catergory":catergory,"amount":amount})
    elif choice==2:
            total_spent=sum(i["amount"] for i in expenses)
            balance=budget-total_spent
            print("----Expense Summary----")
            for i in expenses:
                print(f"-{i['catergory']}:{i['amount']}")
            print(f"\n Total Budget: {budget}")
            print(f"Total spent: {total_spent}")
            print(f"Balance: {balance}")
    elif choice==3:
        print("Goodbye!")
        break
    else:
        print("Enter a valid choice")