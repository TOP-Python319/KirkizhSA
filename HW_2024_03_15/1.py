email = input("Введите Email")

if '@' in email and '.' in email[email.find('@'):]:
    print('да')
else:
    print('нет')