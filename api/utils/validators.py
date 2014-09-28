'''
created on : 16-Sep-2014
@author: Sumit Jain
'''

import re
from errors import ValidationError

def vaild_email(email):
	if re.match(r"^[a-zA-Z0-9._]+\@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}$", email)!=None:
		return True
	else:
		return False

def email(email):
	if vaild_email(email):
		return email
	else:
		raise ValidationError("{} is not a valid email",email)

def password(password):
	if len(password)<8:
		raise ValidationError("Password length must be 8 ")
	else:
		return password
