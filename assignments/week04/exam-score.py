# 1. รับคะแนนสอบของนักเรียน 5 คน และเก็บลงใน list
scores = []
for i in range(1, 6):
    score = float(input(f"Enter score of student {i}: "))
    scores.append(score)

print() 

# 2. ใช้ for loop และ condition (if-else) เพื่อตรวจสอบคะแนน
for i in range(len(scores)):
    # แปลงคะแนนเป็นจำนวนเต็มกรณีที่เป็นเลขลงตัว (เพื่อให้ตรงกับตัวอย่างหน้าจอ)
    score_display = (
        int(scores[i]) if scores[i].is_integer() else scores[i]
    )

    if scores[i] >= 50:
        result = "ผ่าน"
    else:
        result = "ไม่ผ่าน"

    print(f"Student {i + 1}: {score_display} -> {result}")