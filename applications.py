import sys
import traceback
import logging
import python_db


mysql_username = 'dpvaughn'  # please change to your username
mysql_password = 'nofoo0Ie'  # please change to your MySQL password

try:
    python_db.open_database('localhost', mysql_username,
                            mysql_password, mysql_username)  # open database
    Major = ""
    StudentID = ""
    JobID = ""

    res = python_db.applications(Major, StudentID, JobID)
    res = res.split('\n')  # split the header and data for printing
    print("<br/>" + "<br/>")
    print("<br/>" + "Table APPPLICATIONS before:"+"<br/>" +
          res[0] + "<br/>"+res[1] + "<br/>")
    for i in range(len(res)-2):
        print(res[i+2]+"<br/>")
        
    # display STUDENTS table from value passed from PHP for Majors
    try:
        Major = sys.argv[1]
    except:
        Major == ""

    try: 
        StudentID = sys.argv[2]
    except:
        StudentID = ""

    try:
        JobID = sys.argv[3]
    except:
        JobID = ""

    res = python_db.applications(Major, StudentID, JobID)

    res = res.split('\n')  # split the header and data for printing
    print("<br/>" + "<br/>")
    print("<br/>" + "Table APPPLICATIONS after:"+"<br/>" +
          res[0] + "<br/>"+res[1] + "<br/>")
    for i in range(len(res)-2):
        print(res[i+2]+"<br/>")
    python_db.close_db()  # close db
except Exception as e:
    logging.error(traceback.format_exc())
