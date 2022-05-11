# gmail에 들어가서 설정해줘야 한다.
# 톱니바퀴 -> 전달 및 POP/MAP -> IMAP 사용으로 바꾸기



import smtplib # 내장 라이브러리
from email.message import EmailMessage
import re


def sendEmail(addr):
  reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
  if bool(re.match(reg, addr)):
    smtp.send_message(message)
    print('메일 발송 완료')
  else:
    print('잘못된 형식입니다.')


#이메일 만들기
message = EmailMessage() #MIME형식으로 전환
message.set_content("공부중입니다.")
message['Subject'] = '제목'
message['From'] = '###@gmail.com'
message['To'] = '###@gmail.com'
# subjet, from, to등 header에 값을 지정해주려면 대괄호 사용해야 한다.


#이미지 가져오기
with open('codelion.png', 'rb') as image:
  image_file = image.read()

import imghdr # 이미지의 유형 판단해주는 것

image_type = imghdr.what('codelion', image_file)
message.add_attachment(image_file, maintype = 'image', subtime = image_type)

# 3. SMTP: 이메일 서버로 전달, 다른 이메일 서버로 전달할 때 사용
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465
smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) # 메일 서버에 연결하는 함수 (서버 주소, 포트 번호)
# SMTP_SSL - 보안 문제 뚫어줌

smtp.login('fkdlenem@gmail.com', 'password')

sendEmail("fkdlenem@gmail.com")
smtp.quit()



# MIME: 전자우편을 위한 표준 포맷, 텍스트를 MIME 형태로 변형하여 전송해야 함.
# ^: 정규표현식의 시작, $: 정규표현식의 끝