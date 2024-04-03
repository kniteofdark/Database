import mysql.connector
from tabulate import tabulate



def open_database(hostname, user_name, mysql_pw, database_name):
    global conn
    conn = mysql.connector.connect(host=hostname,
                                   user=user_name,
                                   password=mysql_pw,
                                   database=database_name
                                   )
    global cursor
    cursor = conn.cursor()


def printFormat(result):
    header = []
    for cd in cursor.description:  # get headers
        header.append(cd[0])
    print('')
    print('Query Result:')
    print('')
    return (tabulate(result, headers=header))  # print results in table format

# select and display query

def executeSelect(query):
    cursor.execute(query)
    res = printFormat(cursor.fetchall())
    return res


def insert(table, values):
    query = "INSERT into " + table + " values (" + values + ")" + ';'
    cursor.execute(query)
    conn.commit()


def nextId(table):
    query = "select IFNULL(max(ID), 0) as max_id from " + table
    cursor.execute(query)
    result = cursor.fetchall()[0][0]
    return 1 if result is None else int(result) + 1


#Insert a new student
def insert_Student(StudentID, StudentName, Major):
    query = "INSERT INTO STUDENTS (StudentID, StudentName, Major) VALUES (" + StudentID + ", '" + StudentName + "', '" + Major + "')"
    cursor.execute(query)
    conn.commit()

#Insert a new Job
def insert_Job(JobID, CompanyName, JobTitle, Salary, DesiredMajor):
    query = "INSERT INTO JOBS (JobID, CompanyName, JobTitle, Salary, DesiredMajor) VALUES (" + JobID + ", '" + CompanyName + "', '" + JobTitle + "', " + Salary + ", '" + DesiredMajor + "')"
    cursor.execute(query)
    conn.commit()

#Insert a new Application
def insert_Application(StudentID, JobID):
    query = "INSERT INTO APPLICATIONS (StudentID, JobID) VALUES (" + StudentID + ", " + JobID + ")"
    cursor.execute(query)
    conn.commit()

#Prints out students based on major
def student_Majors(Major):
    if (Major == "ALL"):
        query = "SELECT * FROM STUDENTS"
    else:
        query = "SELECT * FROM STUDENTS WHERE Major = '" + Major + "';"
    cursor.execute(query)
    res = printFormat(cursor.fetchall())
    return res

#Prints our jobs based on major
def job_Majors(Major):
    if (Major == "ALL"):
        query = "SELECT * FROM JOBS"
    else:
        query = "SELECT * FROM JOBS WHERE DesiredMajor = '" + Major + "'"
    cursor.execute(query)
    res = printFormat(cursor.fetchall())
    return res

#Prints out applications based on major, student id, or job id
def applications(Major, StudentID, JobID):
    
    #For showing all applications
    if (Major == "" and StudentID == "" and JobID == ""):
        query = "SELECT STUDENTS.StudentName, JOBS.CompanyName, JOBS.Salary, STUDENTS.Major FROM STUDENTS INNER JOIN APPLICATIONS ON STUDENTS.StudentID = APPLICATIONS.StudentID INNER JOIN JOBS ON APPLICATIONS.JobID = JOBS.JobID;"
    
    #For showing applications by Major
    if (Major != "" and StudentID == "" and JobID == ""):
        query = "SELECT STUDENTS.StudentName, JOBS.CompanyName, JOBS.Salary, STUDENTS.Major FROM STUDENTS INNER JOIN APPLICATIONS ON STUDENTS.StudentID = APPLICATIONS.StudentID INNER JOIN JOBS ON APPLICATIONS.JobID = JOBS.JobID WHERE STUDENTS.Major = '" + Major + "';"
   
    #For showing applications by StudentID
    if (Major == "" and StudentID != "" and JobID == ""):
        query = "SELECT STUDENTS.StudentName, JOBS.CompanyName, JOBS.Salary, STUDENTS.Major FROM STUDENTS INNER JOIN APPLICATIONS ON STUDENTS.StudentID = APPLICATIONS.StudentID INNER JOIN JOBS ON APPLICATIONS.JobID = JOBS.JobID WHERE STUDENTS.StudentID = " + StudentID + ";"
    
    #For showing applicaitons by JobID
    if (Major == "" and StudentID == "" and JobID != ""):
        query = "SELECT STUDENTS.StudentName, JOBS.CompanyName, JOBS.Salary, STUDENTS.Major FROM STUDENTS INNER JOIN APPLICATIONS ON STUDENTS.StudentID = APPLICATIONS.StudentID INNER JOIN JOBS ON APPLICATIONS.JobID = JOBS.JobID WHERE JOBS.JobID = " + JobID + ";"
    cursor.execute(query)
    res = printFormat(cursor.fetchall())
    return res

def executeUpdate(query):  # use this function for delete and update
    cursor.execute(query)
    conn.commit()

def close_db():  # use this function to close db
    cursor.close()
    conn.close()




# ##### Test #######
# mysql_username = 'dpvaughn' # please change to your MySQL username
# mysql_password ='nofoo0Ie'  # please change to your MySQL password
# open_database('localhost',mysql_username,mysql_password,mysql_username) # open database   

# flag = True
# while flag:
#     print("\nMenu:\n\
#             1) Add Student\n\
#             2) Add Job\n\
#             3) Add Application\n\
#             4) View Student Majors\n\
#             5) View Job Majors\n\
#             6) View Application\n")

#     menu_choice = input("Please select 1-6\n")
#     if (menu_choice == '1'):
#         sid = input("StudentID: ")
#         name = input("StudentName: ")
#         major = input("Major: ")
#         insert_Student(sid,name,major)
#     if (menu_choice == '2'):
#         jid = input("JobID: ")
#         name = input("CompanyName: ")
#         title = input("JobTitle: ")
#         salary = input("Salary: ")
#         major = input("DesiredMajor: ")
#         insert_Job(jid,name,title,salary,major)
#     if (menu_choice == '3'):
#         sid = input("StudentID: ")
#         jid = input("JobID: ")
#         insert_Application(sid,jid)
#     if (menu_choice == '4'):
#         major = input("Major: ")
#         print(major)
#         student_Majors(major)
#     if (menu_choice == '5'):
#         major = input("Major: ")
#         job_Majors(major)
#     if (menu_choice == '6'):
#         choice = input("Show by Major, StudentID, or JobID (1,2,3)")
#         if (choice == '1'):
#             major = input("Major: ")
#             sid = ""
#             jid = ""
#         if (choice == '2'):
#             major = ""
#             sid = input("StudentID: ")
#             jid = ""
#         if (choice == '3'):
#             major = ""
#             sid = ""
#             jid = input("JobID: ")
#         applications(major,sid,jid)
#     if (menu_choice == '7'):
#         close_db()
#         flag = False
