import sys
import traceback
import logging
import python_db


mysql_username = 'dpvaughn'  # please change to your username
mysql_password = 'nofoo0Ie'  # please change to your MySQL password

try:
    python_db.open_database('localhost', mysql_username,
                            mysql_password, mysql_username)  # open database
                            
    res = python_db.executeSelect('SELECT * FROM STUDENTS;')
    res = res.split('\n')  # split the header and data for printing

    print("<br/>" + "Table STUDENTS before:"+"<br/>" +
          res[0] + "<br/>"+res[1] + "<br/>")
    for i in range(len(res)-2):
        print(res[i+2]+"<br/>")
    # display STUDENTS table from value passed from PHP for Majors
    Major = sys.argv[1]

    # res = python_db.executeSelect("SELECT * FROM STUDENTS WHERE Major = '" + Major + "';")
    res = python_db.student_Majors(Major)

    res = res.split('\n')  # split the header and data for printing
    print("<br/>" + "<br/>")
    print("<br/>" + "Table STUDENTS after:"+"<br/>" +
          res[0] + "<br/>"+res[1] + "<br/>")
    for i in range(len(res)-2):
        print(res[i+2]+"<br/>")
    python_db.close_db()  # close db
except Exception as e:
    logging.error(traceback.format_exc())
