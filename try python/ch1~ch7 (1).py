import random

# lunch = random.choice(["된장찌개","피자","제육볶음"])
# dinner = random.choice(["김밥","쫄면","돈까스"])

# information = {"고향": "수원", "취미": "영화관람", "좋아하는 음식": "국수"}
# print(information)
# print(information.get("취미"))

# information = {"특기": "피아노", "사는곳": "서울"}
# print(information.get("특기"))
# print(information.get("사는곳"))

information = {"고향": "수원", "취미": "영화관람","좋아하는 음식": "국수"}
foods = ["된장찌개", "피자", "제육볶음"]

# dictionary
information["특기"] = "피아노"
information["사는곳"] = "서울"
print(information)

del information["좋아하는 음식"]
print(information)

print(len(information))

information.clear()
print(information)

# list
print(foods[1])
print(foods[2])
print(foods[-1])
foods.append("김밥")
print(foods)

del foods[1]
print(foods)