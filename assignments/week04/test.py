# รับชื่อจริง (หรือข้อความ)จากผู้ใช้
# นับจำนวนสระทั้งหมดในข้อความนั้นว่ามีกี่ตัว(a,e,i,o,u)

# ตัวอย่างหน้าจอ
# what is your name? : Kamonphan
# Your text have 3 vowels

text = input("what is your name? : ")

vowel_count = 0

for char in text.lower():
    if char in ['a', 'e', 'i', 'o', 'u']:
        vowel_count += 1

print(f"Your text have {vowel_count} vowels")