import re

def email_parsing(email_address):
    re_email = re.compile(r'(?P<username>([\w]+))@(?P<domain>[^&]+\.\w+)', re.IGNORECASE)
    if not re_email.match(email_address):
        raise ValueError(f"wrong email: {email_address}")
    print(re_email.match(email_address).groupdict())

for i in ['someone@geekbrains.ru', 'someone@geekbrainsru', 'som&eone@geekbrainsru']:
    try:
        email_parsing(i)
    except ValueError as error:
        print(error)