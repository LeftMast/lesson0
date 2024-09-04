def send_email(message, recipient, *, sender='university.help@gmail.com'):
    domen_maple = ('.com', '.ru', 'net')
    adresses_ = [recipient, sender]

    if ('@' not in sender) or ('@' not in recipient) or not (all(addr.endswith(domen_maple) for addr in adresses_)):
        print(f'Невозможно отправить письмо с адреса: {sender} на адрес: {recipient}')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')