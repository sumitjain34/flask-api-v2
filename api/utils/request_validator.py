import time
import hmac
import hashlib

def generate_auth(data):
    
    key='41DE849FA6F7B66EF867AFC9B2455'
    digest_maker=hmac.new(key,'',hashlib.sha1)
    digest_maker.update(data)
    digest=digest_maker.hexdigest()
    return digest

def check_timestamp(request_timestamp):
	# if difference in timestamps is more than 3 min then invalid request
	current_timestamp=int(time.time())
	if current_timestamp-request_timestamp>180: 
		return False
	else:
		return True

def check_signature(request,endpoint):
	print "%%%%%%%%%%%%%%%%%%%%%%% Checking signature %%%%%%%%%%%%%%%%%%%%%%%"
	host='api.lens.com'
	if request.method=="GET":
		params=''
		for key in request.values.keys():
			params=params+'%'+key+'%'+request.values.get(key)
		print params	
		data_for_auth='GET%'+host+'%/'+endpoint+params
		server_digest=generate_auth(data_for_auth)
		if server_digest==request.headers.get('Authorization'):
			return True
		else:
			return False
		print data_for_auth

def validate_request(request,endpoint='register'):
	print "%%%%%%%%%%%%%%%% Validating Request %%%%%%%%%%%%%%%%%%%%%"
	request_timestamp=int(request.values.get('ts'))
	status=check_timestamp(request_timestamp)
	if status:
		status=check_signature(request,endpoint)
		if status:
			return {'status':status,'message':'valid request'}
		else:
			return {'status':status,'message':'invalid signature'}
	else:
		return {'status':status,'message':'replayed request'}


	

