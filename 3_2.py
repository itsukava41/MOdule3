def send_email(message, recipient, sender = 'university.help@gmail.com'):
    domen = ('.com', '.ru', '.net')
    domen_ok = recipient.endswith(domen,-4) == sender.endswith(domen, -4)
    if recipient.count('@') == 1 and sender.count('@') == 1:
        if domen_ok is not True:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        elif sender == recipient:
            print('Невозможно отправить самому себе')
        elif sender == 'university.help@gmail.com':
            print(f'Письмо успешно отправлено с адреса {sender} на {recipient}')
        else:
            print(f'НЕСТРАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на {recipient}')
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')