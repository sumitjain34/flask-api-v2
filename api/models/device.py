from mongoengine import *
from datetime import datetime

class Device(Document):
	imei=StringField(unique=True)