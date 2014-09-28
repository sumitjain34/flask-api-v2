from flask.ext.restful import Api,Resource,reqparse
from api.utils.validators import email
from api.utils.validators import password
from api.utils.user_helper import generate_user_id
from api.utils.user_helper import generate_access_token
from api.utils.dbhelper import save_user
from flask import abort

class Register(Resource):
    def __init__(self):
        self.reqparser=reqparse.RequestParser()
        self.reqparser.add_argument('email',type=email,required=True,location='form')
        self.reqparser.add_argument('password',type=password,required=True,location='form')
        super(Register,self).__init__()

    def post(self):
        
        args=self.reqparser.parse_args()
        email=args.get('email',None)
        password=args.get('password',None)
        # user_id=generate_user_id()
        access_token=generate_access_token()
        try:
            response=save_user(email,password,access_token)
            
        except Exception as e:
            response={'message':str(e),'error_code':1}
        return response
        
    def get(self):
        response={'message':'Wrong request type','error_code':1}
        return response,404