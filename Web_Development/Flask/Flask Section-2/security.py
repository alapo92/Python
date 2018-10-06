# importing werkzeug to get the safe str cmp
# which is a safe string compare function that deals with all sorts of encoding issues
from werkzeug.security import safe_str_cmp
from user import User

users = [
   User(1, 'bob', 'asdf')
]
# created to have an index on bob
username_mapping = {u.username: u for u in users}   # set comprehension
#username_mapping = {
#    'bob': {
#        'id': 1,
#        'username': 'bob',
#        'password': 'asdf'
#    }
#}

userid_mapping = {u.id: u for u in users}

# useful for not iterating over our list all the time
print(userid_mapping[1])
print(username_mapping['bob'])


def authenticate(username, password):
    user = username_mapping.get(username, None)   # .get accesses a dictionary and lets us set a default
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
