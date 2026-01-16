import psycopg2 # to connect db,request and fetch
db_name = "TaskListDB"
db_user = "tasklist_user"
db_pass = "abc123"
db_host = "localhost"

def getTaskList():
    conn = psycopg2.connect(dbname=db_name,user = db_user,password = db_pass,host = db_host)
    cur = conn.cursor() # cursor is a bridge between db and python
    cur.execute('SELECT task_name,is_active FROM public."TaskList"')
    tasklist = cur.fetchall()
    cur.close
    conn.close
    return tasklist