import sys
import traceback
import logging
import python_db


mysql_username = 'dpvaughn'  # please change to your username
mysql_password = 'nofoo0Ie'  # please change to your MySQL password

try:
    python_db.open_database('localhost', mysql_username,
                            mysql_password, mysql_username)  # open database
    res = python_db.executeSelect('SELECT * FROM JOBS;')
    res = res.split('\n')  # split the header and data for printing
    print("<br/>" + "Table JOBS before:"+"<br/>" +
          res[0] + "<br/>"+res[1] + "<br/>")
    for i in range(len(res)-2):
        print(res[i+2]+"<br/>")

    # Insert new JOB
    JobID = sys.argv[1]
    CompanyName = sys.argv[2]
    JobTitle = sys.argv[3]
    Salary = sys.argv[4]
    DesiredMajor = sys.argv[5]

    python_db.insert_Job(JobID, CompanyName, JobTitle, Salary, DesiredMajor)

    res = python_db.executeSelect('SELECT * FROM JOBS;')
    res = res.split('\n')  # split the header and data for printing
    print("<br/>" + "<br/>")
    print("<br/>" + "Table JOBS after:"+"<br/>" +
          res[0] + "<br/>"+res[1] + "<br/>")
    for i in range(len(res)-2):
        print(res[i+2]+"<br/>")
    python_db.close_db()  # close db
except Exception as e:
    logging.error(traceback.format_exc())
