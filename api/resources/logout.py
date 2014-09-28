from flask.ext.login import login_required,logout_user,current_user
from flask.ext.restful import Resource


class Logout(Resource):

	@login_required
	def get(self):
		print "inside logout get"
		print current_user.email
		logout_user()
		
		response={'message':'you are logged out','error_code':0}
		return response

	def post(self):
		response={'message':'Wrong request type','error_code':1}
		return response
	