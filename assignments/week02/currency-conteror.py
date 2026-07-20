# Question 2: Currency Converter
EXCHANGE_RATE = 35.5

print("Select conversion direction:")
print("1: THB to USD")
print("2: USD to THB")
choice = input("Enter choice (1 or 2): ")


amount = float(input("Enter amount: "))


if choice == '1':
    result = amount / EXCHANGE_RATE
    print(f"\nFormula: USD = THB / {EXCHANGE_RATE}")
    print(f"Result: {amount:.2f} THB = {result:.2f} USD")

elif choice == '2':
    result = amount * EXCHANGE_RATE
    print(f"\nFormula: THB = USD * {EXCHANGE_RATE}")
    print(f"Result: {amount:.2f} USD = {result:.2f} THB")
else:
    print("Invalid choice! Please select 1 or 2.")