#Imports
from bson import json_util

class UserService():
    
    def __init__(self, userRepository):
        self.userRepository = userRepository