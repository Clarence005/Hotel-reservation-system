from abc import ABCMeta,abstractstaticmethod
import cx_Oracle
#Singleton pattern
class Dbconnectivity:
    __instance = None
    @staticmethod
    def check():
        if(Dbconnectivity.__instance == None):
            Dbconnectivity()
        return Dbconnectivity.__instance
    
    def __init__(self):
        if(Dbconnectivity.__instance!= None):
            raise "Already a connectivity exist"
        else:
            try:
                oracle_connection_string = 'system/clarence@localhost:1521/XE'
                self.connection = cx_Oracle.connect(oracle_connection_string)
                self.cursor = self.connection.cursor()
                Dbconnectivity.__instance = self
            except cx_Oracle.DatabaseError as e:
                error, = e.args
                print("Oracle-Error-Code:", error.code)
                print("Oracle-Error-Message:", error.message)
        
    def insert_user(self,u_id,u_name,password,email,ph_no):
        query = f"insert into hotel_user values('{u_id}','{u_name}','{password}','{email}','{ph_no}')"
        self.cursor.execute(query)
        self.connection.commit()

