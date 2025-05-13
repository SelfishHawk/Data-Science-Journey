while True:
    name=input("Enter customer Name:- ")
    address=input("Enter customer Address:-")
    mobile=int(input("Enter customer mobile no.:-"))
    total=0
    while True:
        item=input("Enter the item name:-")
        quantity=int(input("Enter the quantity:-"))
        cost=float(input("Enter price per piece in Dollars:-"))
        total+=(quantity*cost)
        again=input("another one (yes/no)")
        if(again=="No" or again=="no"):
            break
    print("-"*40)
    print("Customer Name ",name)
    print("Customer address ",address)
    print("Customer Mobile no. ",mobile)
    print("Total Amount:-",total)
    print("-"*40)
    another=input("New coustomer (yes/no)")
    if(another=="no" or another=="No"):
        break
