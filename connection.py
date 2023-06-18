import pymysql


def connect():
    conn = pymysql.connect(
        host='localhost',


        database='criminal_dbms',
        user='root',
        password='system',
    )
    return conn

def verifyemail(email):
    if '@' in email and '.' in email:
        return "valid"
    else:
        return "invalid"


def verifymobile(mobile):
    if len(mobile) == 10 and mobile.isdigit():
        if mobile[0] in "9876":
            return "valid"
        else:
            return "invalid"
    else:
        return "invalid"