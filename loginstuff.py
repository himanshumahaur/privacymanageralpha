import hashlib
import pandas as pd

def getuserlist():
    maindata = pd.read_csv('D:/.GitHub/privacymanageralpha/loginstuff.csv')
    userlist = maindata['u'].values.tolist()
    return userlist

def getpasslist():
    maindata = pd.read_csv('D:/.GitHub/privacymanageralpha/loginstuff.csv')
    passlist = maindata['p'].values.tolist()
    return passlist

def userexists(username):
    userlist = getuserlist()

    if username in userlist:
        return True
    else:
        return False

def passexists(password):
    passlist = getpasslist()

    if password in passlist:
        return True
    else:
        return False

def verify():
    username = str(input("Enter Username: "))

    if userexists(username):
        password = str(input("Enter Password: "))
        encripass = hashlib.sha256(password.encode()).hexdigest()
        if passexists(encripass):
            print("Sucess")
        else:
            print("Wrong password")
    else:
        print("User dosent exist")


def savenew():

    username = str(input("Enter Username: "))

    if userexists(username):
        print("User already there!")
    
    else:
        password = str(input("Enter Password: "))
  
        encripass = hashlib.sha256(password.encode()).hexdigest()

        newdata = pd.DataFrame({'u':[username], 'p':[encripass]})
        newdata.to_csv('D:/.GitHub/privacymanageralpha/loginstuff.csv', mode='a', index=False, header=False)

def choice():

    ch = int(input("1. Sign up\n2. Log in\n3. Exit\n"))

    if ch == 1:
        savenew()
    if ch == 2:
        verify()
    if ch == 3:
        exit()

    choice()
    
choice()

