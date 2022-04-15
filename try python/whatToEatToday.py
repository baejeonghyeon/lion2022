import time
import random

lunch = ["된장찌개", "피자", "제육볶음", "짜장면"]
print(lunch)
while True:
  
  item = input("음식을 추가해주세요")
  if item == "q":
    break
  
  lunch.append(item)
  print(lunch)

#집합으로 변화
set_lunch = set(lunch)

while True:
  print(set_lunch)
  item = input("음식을 삭제해주세요")
  if item == "q":
    break
  set_lunch = set_lunch - set([item])

print(set_lunch, "중에서 선택합니다")
for i in range(5, 0, -1):
  print(str(i))
  time.sleep(1)
  
print(random.choice(list(set_lunch)))

