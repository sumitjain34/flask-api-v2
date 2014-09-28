from api import db
from datetime import datetime

class User(db.Document):
    access_token=db.StringField(unique=True)
    first_name=db.StringField()
    middle_name=db.StringField()
    last_name=db.StringField()
    email=db.EmailField(unique=True,required=True)
    other_emails=db.ListField(db.DictField())
    password=db.StringField(required=True,min_length=8)
    birth_date=db.DateTimeField()
    gender=db.StringField(choices=['m','f'])
    avatar_thumb_url=db.URLField()
    avatar_url=db.URLField()
    contact_numbers=db.ListField(db.DictField())
    address=db.ListField(db.DictField())
    organisation=db.StringField()
    designation=db.StringField()
    social_profiles=db.ListField(db.DictField())
    created_at=db.DateTimeField(default=datetime.now)

    def get_id(self):
        print "inside get id"
        return unicode(self.id)

    def is_anonymous(self):
        return True

    def is_active(self):
        print "Inside is active"
        return True

    def is_authenticated(self):
        print "inside Authenticating"
        return True

    def get_auth_token(self):
        print "inside get auth token"
        return make_secure_token(self.email, key='deterministic')