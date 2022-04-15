# foods = ["된장찌개", "피자", "제육볶음", "된장찌개"]
# foods_set = set(foods)
# print(foods)
# print(foods_set) #집합은 순서가 정해져 있지 않음

menu1 = set(["된장찌개", "피자", "제육볶음"])
menu2 = set(["된장찌개", "떡국", "김밥"])

menu3 = menu1 | menu2 #합집합
print(menu3)

menu4 = menu1 & menu2 #교집합
print(menu4)

menu5 = menu1 - menu2 #차집합
print(menu5)