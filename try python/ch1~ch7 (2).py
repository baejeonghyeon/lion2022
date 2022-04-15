import random
import time
a = 0
while True:
  print(random.choice(['된장찌개', '치킨', '떡볶이', '라면', '감자튀김']))
  print("이 문장")
  time.sleep(1)
  a = a + 1
  if a == 10:
    break
