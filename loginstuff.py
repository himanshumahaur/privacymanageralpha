from collections import UserList
import hashlib
import pandas as pd

def getuserlist():
    maindata = pd.read_csv('D:/.GitHub/privacymanageralpha/loginstuff.csv')
    userlist = maindata['u'].values.tolist()
    return userlist


def userexists(username):
    userlist = getuserlist()

    if username in userlist:
        return True
    else:
        return False


def savenew():

    username = str(input("Enter Username: "))
    password = str(input("Enter Password: "))
  
    encripass = hashlib.sha256(password.encode())

    newdata = pd.DataFrame({'user':[username], 'pass':[encripass.hexdigest()]})
    newdata.to_csv('D:/.GitHub/privacymanageralpha/loginstuff.csv', mode='a', index=False, header=False)

savenew()

