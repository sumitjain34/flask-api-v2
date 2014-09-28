'''
Created on: 16th Aug 2014
@author: Sumit Jain
'''
import time
import random
import socket
import hashlib
import string

def generate_user_id():
    user_id=''.join(random.choice(string.hexdigits) for _ in range(24)).lower()
    
    # user_id='123'
    return user_id

def generate_access_token():
    """
    Generates a universally unique access_token.
    Any arguments only create more randomness.
    """
    t = long( time.time() * 1000 )
    r = long( random.random()*100000000000000000L )
    try:
        a = socket.gethostbyname( socket.gethostname() )
    except:
        # if we can't get a network address, just imagine one
        a = random.random()*100000000000000000L
    data = str(t)+'%'+str(r)+'%'+str(a)
    access_token = hashlib.sha1(data).hexdigest()
    return access_token

def generate_user_json(user):
    user_json={}
    user_json['firstName']=user['first_name']
    user_json['middleName']=user['middle_name']
    user_json['lastName']=user['last_name']
    user_json['email']=user['email']
    user_json['otherEmails']=user['other_emails']
    user_json['birthDate']=user['birth_date']
    user_json['gender']=user['gender']
    user_json['avatarThumbUrl']=user['avatar_thumb_url']
    user_json['avatarUrl']=user['avatar_url']
    user_json['contactNumbers']=user['contact_numbers']
    user_json['address']=user['address']
    user_json['organisation']=user['organisation']
    user_json['designation']=user['designation']
    user_json['socialProfiles']=user['social_profiles']
    return user_json

