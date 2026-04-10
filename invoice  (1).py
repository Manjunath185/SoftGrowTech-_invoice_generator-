def generate_invoice():
    print("===== INVOICE GENERATOR =====")

    name = input("Enter customer name: ")
    items = []
    total = 0

    n = int(input("Enter number of items: "))

    for i in range(n):
        item_name = input("Item name: ")
        price = float(input("Item price: "))
        qty = int(input("Quantity: "))

        amount = price * qty
        total += amount

        items.append((item_name, price, qty, amount))

    print("\n----- INVOICE -----")
    print(f"Customer: {name}")
    print("-------------------")

    for item in items:
        print(f"{item[0]} | ₹{item[1]} x {item[2]} = ₹{item[3]}")

    print("-------------------")
    print(f"Total Amount: ₹{total}")
    print("-------------------")


generate_invoice()