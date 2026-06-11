import mysql.connector

def get_database_connection():
    connection = mysql.connector.connect(
        host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
        user="2rFtW32FfcJ2C3j.root",
        password="Yi3724qL0xIMRxsO",         #  password
        database="student_task_manager",
        port=4000
    )
    return connection            