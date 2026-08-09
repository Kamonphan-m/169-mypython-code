def create_user_profile(username, age=18, premium=False):
    # เช็กสถานะพรีเมียมด้วย Ternary Operator แบบสั้น
    user_type = "Premium User" if premium else "Standard User"
    
    # จัดรูปแบบข้อความส่งกลับ (return)
    return f"{username} (age: {age}) - {user_type}"


# --- ตัวอย่างทดสอบการเรียกใช้งาน ---
# 1. ใส่เฉพาะ username (ใช้อายุ 18 และ Standard โดยอัตโนมัติ)
print(create_user_profile("john_doe"))  
# Output: john_doe (age: 18) - Standard User

# 2. ใส่ระบุอายุ และสถานะ premium = True
print(create_user_profile("alice", age=25, premium=True))  
# Output: alice (age: 25) - Premium User

import math

def calculate_circle(radius):
    # คำนวณพื้นที่: π * r^2
    area = math.pi * (radius ** 2)
    
    # คำนวณเส้นรอบวง: 2 * π * r
    circumference = 2 * math.pi * radius
    
    # ส่งค่าคืนกลับเป็น tuple (พื้นที่, เส้นรอบวง)
    return area, circumference


# --- ตัวอย่างทดสอบการเรียกใช้งาน ---
area, circumference = calculate_circle(5)
print(f"พื้นที่: {area:.2f}, เส้นรอบวง: {circumference:.2f}")
# Output: พื้นที่: 78.54, เส้นรอบวง: 31.42