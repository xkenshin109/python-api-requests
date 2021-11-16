#This is the cleaner way to create a Class for the API to use as a Variable
import requests
class ApiRequests(object):
    apiAuthenticationToken = "<<Token Here>>"
    def __init__(self, token):
        #self is for the class object being instantiated and is needed for all methods following
        #token parameter will be the token to set on the object and only is contained in this instance of the object
        self.apiAuthenticationToken = token
        print('Token Passed in: ' + token)
        print('Token Stored into Property: ' + self.apiAuthenticationToken)
    def callApi(self):
        #self is for the class object being instantiated and is needed for all methods following
        response = requests.get("http://api.open-notify.org/astros.json")
        print(response)
    def retrieveToken(self):
        #self is for the class object being instantiated and is needed for all methods following
        #here you will make the call to retrieve the token
        #if you have a static token set in the constructor
        print(self.apiAuthenticationToken)