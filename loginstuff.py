import hashlib
import pandas as pd
import smtplib
import string
import random

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
        print("User already there! Try log in")
    
    else:
        password = str(input("Enter Password: "))
        encripass = hashlib.sha256(password.encode()).hexdigest()

        newdata = pd.DataFrame({'u':[username], 'p':[encripass]})
        newdata.to_csv('D:/.GitHub/privacymanageralpha/loginstuff.csv', mode='a', index=False, header=False)

def getindex(username):
    userlist = getuserlist()

    pindex = 0
    for i in userlist:
        if i == username:
            break
        pindex = pindex+1
    return pindex

def getmailcode(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def forgot():
    username = str(input("Enter Username: "))

    if userexists(username):

        mailcode = getmailcode()
        message = 'Your code is ' + mailcode

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("pythonproject.github@gmail.com", "rohithimanshu")
        s.sendmail("pythonproject.github@gmail.com", username, message)
        s.quit()

        usercode = str(input("Enter Code from email: "))
        if usercode == mailcode:
            pindex = getindex(username)

            password = str(input("Enter New Password: "))
            encripass = hashlib.sha256(password.encode()).hexdigest()

            maindata = pd.read_csv('D:/.GitHub/privacymanageralpha/loginstuff.csv')
            maindata.iloc[pindex,1]=encripass
            maindata.to_csv('D:/.GitHub/privacymanageralpha/loginstuff.csv', index=False)
        else:
            print("WRONG CODE")

    else:
        print("User dosent exist")



def choice():

    ch = int(input("1. Sign up\n2. Log in\n3. Forgot\n4. Exit\n"))

    if ch == 1:
        savenew()
    if ch == 2:
        verify()
    if ch == 3:
        forgot()
    if ch == 4:
        exit()

    choice()
    
choice()

