#to test this script open Python Interperter and copy/paste
import sys
sys.path.append('D:\Python Test Scripts') #change the directory name to where you have the API script
import api
testingApi = api.ApiRequests('test token') #This is where the Variable for the API is instantiated and used through the script
testingApi.retrieveToken()
testingApi.callApi()