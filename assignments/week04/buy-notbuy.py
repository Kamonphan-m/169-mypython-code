# 1. รับราคาสินค้าจำนวน 6 รายการ และเก็บลงใน list
prices = []
print("Enter prices of 6 items:")
for i in range(1, 7):
    price = float(input(f"Item {i}: "))
    # แปลงเป็นจำนวนเต็มหากเป็นเลขลงตัว เพื่อให้ตรงกับตัวอย่างหน้าจอ
    if price.is_integer():
        price = int(price)
    prices.append(price)

print()

# 2. รับงบประมาณรวม 1 ค่า
budget = float(input("Enter total budget: "))
if budget.is_integer():
    budget = int(budget)

print()

# 3. ตรวจสอบสินค้าทีละรายการตามลำดับ
current_total = 0
bought_items = []

for i in range(len(prices)):
    item_price = prices[i]
    
    # ถ้ายอดใช้จ่ายสะสม + ราคาสินค้าชิ้นปัจจุบัน <= งบประมาณ
    if current_total + item_price <= budget:
        status = "buy"
        current_total += item_price
        bought_items.append(item_price)
    else:20
    status = "cannot buy"
        
    print(f"Item {i + 1} = {item_price} -> {status}")
    print(f"Current total = {current_total}")
    print()

# 4. แสดงผลสรุปรายการสินค้าที่ซื้อได้ ยอดใช้จ่ายรวม และงบประมาณคงเหลือ
remaining_budget = budget - current_total

print(f"Bought items: {bought_items}")
print(f"Total spent: {current_total}")
print(f"Remaining budget: {remaining_budget}")