from flask.ext.restful import Resource,reqparse
from api import login_manager
from api.utils.validators import email
from api.utils.validators import password
from flask.ext.login import login_user,current_user
from api.utils.dbhelper import user_login
from api.models.flask_user import FlaskUser
from api.models.user import User


# @login_manager.user_loader
class Login(Resource):
    def __init__(self):
        print "Initializing user "
        self.reqparser=reqparse.RequestParser()
        self.reqparser.add_argument('email',required=True,type=email,help='Please provide email',location='form')
        self.reqparser.add_argument('password',required=True,type=password,help='Please provide password',location='form')
        super(Login,self).__init__()

    def post(self):
        print "inside post method"
        args=self.reqparser.parse_args()
        email=args.get('email',None)
        password=args.get('password',None)
        response=user_login(email,password)
        if response['error_code']==0:
            user=response['user']
            print "successfull login"
            login_user(user)
            print "logged in"
            response={'message':'You are logged in','error_code':0,'access_token':current_user.access_token,'user_id':unicode(current_user.id)}
        return response

    def get(self):
        response={'message':'Wrong request type','error_code':1}
        return response,404

    # @login_manager.user_loader
    # def load_user(userid):
    #     print "Looooooading user"
    #     print userid
    #     user=User.objects.get(id=userid)
    #     print user.id
    #     return user

    @login_manager.request_loader
    def load_user_from_request(request):
        print "Loading user from request"
        access_token=request.headers.get('Authorization')
        if access_token:
            print "fetching user"
            user=User.objects(access_token=access_token)
            if user:
                return user[0]
        return None

    # @login_manager.header_loader
    # def load_user_from_header(header_val):
    #     print "Loading  user from headers"
    #     print header_val
    #     return header_val

    @login_manager.unauthorized_handler
    def unauthorized():
        # do stuff
        response={'message':'You are not logged in','error_code':1}
        return response