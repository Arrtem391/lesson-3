import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

sender_email = os.getenv('login_yandex')
sender_name = "Артём"
recipient_email = "kudinowartem22@gmail.com"
recipient_name = "Илюха"
site = 'https://dvmn.org/profession-ref-program/spytf/1WJiV/'

password = os.getenv('password_yandex')
server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(sender_email, password)

letter = """From: %sender_email%
To: %recipient_email%
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""

letter = letter.replace('%sender_email%', sender_email).replace('%recipient_email%', recipient_email).replace('%website%', site).replace('%friend_name%', recipient_name).replace('%my_name%', sender_name)

server.sendmail(sender_email, 'kudinowartem22@gmail.com', letter.encode('utf-8'))
server.quit()
