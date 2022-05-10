from googletrans import Translator

#1. 완성
# translator = Translator()
# # sentence = "좋은 아침이에요"
# sentence = input("번역을 원하는 문장을 입력하세요 : ")
# result = translator.translate(sentence, dest="en")
# detect = translator.detect(sentence)

# print("\n============= 번역 결과 ============\n")
# print(detect.lang,":", result.origin)
# print(result.dest,":", result.text)
# print("\n====================================\n")


#3. 언어 감지하기
translator = Translator() # 번역기 만들기
# sentence = "안녕하세요 코드라이언입니다."
sentence = input("언어를 감지할 문장을 입력해주세요 : ")
detected = translator.detect(sentence) # 문장을 감지
print(detected.lang) # 무슨 언어인지 판별

#4: 번역하기 1
result = translator.translate(sentence,'en') # (문장, 어떤언어로?, 소스텍스트의 언어(생략가능))
print(result)

#5. 번역하기 2
print(detected.lang, ":", sentence)
print(result.dest, ":", result.text)