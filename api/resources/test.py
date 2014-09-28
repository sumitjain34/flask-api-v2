from flask.ext.restful import Resource,reqparse
from api import login_manager
from flask.ext.login import login_required,current_user

class Test(Resource):
    
    @login_required
    def get(self):
    	print "inside test get method"
    	print current_user.email
        response={'message':'this is a test get url','user':current_user.email}
        return response,200

    @login_required
    def post(self):
    	print "inside test post method"
        print current_user.email
        response={'message':'this is a test post url','user':current_user.email}
        return response, 200
