from api.models.user import User
import user_helper
import traceback
from errors import ValidationError
from errors import NotUniqueError


# def db_connected():
    # try:
    #     DATABASE_NAME='lens_database'
    #     connect(DATABASE_NAME)
    #     return True
    # except Exception as e:
    #     print "Database not connected"
    #     print traceback.format_exc(e)
    #     return False
    # return True


def get_user(user_id):
    try:
        cursor=User.objects(user_id=user_id)
        if cursor:
            user=cursor[0]
            user_json=user_helper.generate_user_json(user)
            response={'message':'Cool Profile','error_code':0,'user':user_json}
        else:
            response={'message':'No user with this id','error_code':1}
    except Exception as e:
        response={'message':'no data in database','error_code':1}
        print traceback.format_exc(e)
    return response

def save_user(email,password,access_token):
    try:
        user=User(email=email,password=password,access_token=access_token).save()
        response={'message':'You are registered','error_code':0,'access_token':access_token,'user_id':unicode(user.id)}
    except Exception as e:
        print traceback.format_exc(e)
        response={'message':'this email aleady exists','error_code':1}
        raise NotUniqueError("This email already exists")
    return response

# def create_user(email,password):
#     user_id=user_helper.generate_user_id()
#     access_token=user_helper.generate_access_token()
#     response=save_user(email,password,user_id,access_token)
#     return response

def user_login(email,password):
    try:
        print "--------------------------- Trying to log in -------------------------------"
        cursor=User.objects(email=email)
        if cursor:
            user=cursor[0]
            if user.password==password:
                response={'message':'You are logged in','error_code':0,'user':user}
            else:
                response={'message':'wrong password','error_code':1}
        else:
            response={'message':'wrong email','error_code':1}
    except Exception as e:
        print traceback.format_exc(e)
        response={'message':'no data in database','error_code':1}
    return response
    

    


    
