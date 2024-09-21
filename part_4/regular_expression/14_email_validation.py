"""
[local_part]@[domain_part]
toon@gmail.com
"""

import re

email_regex = r'^[a-zA-Z.]+@[a-zA-Z.]+\.[a-z]{2,}$'

def validate_email(email):
    if len(email) > 320:
        return False

    local_part, domain_part = email.split('@')

    if len(local_part) > 64:
        return False

    if len(domain_part) > 255:
        return False

    if re.match(email_regex, email):
        return True
    else:
        return False


input_email = "toon.apiwat@mydomain.co.th"
is_email_valid = validate_email(input_email)

if is_email_valid == True:
    print("Your email is valid.")
else:
    print("Your email is not valid.")