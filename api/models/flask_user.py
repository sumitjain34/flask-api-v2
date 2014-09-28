from flask.ext.login import UserMixin

class FlaskUser(UserMixin):
    def __init__(self, email,password):
        self.email =email
        self.password = password

    