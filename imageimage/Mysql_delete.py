import mysql.connector

class delete_data:

    def delete(self):
        
        self.connexion = mysql.connector.connect(host="localhost",
                                                 user="jbaw",
                                                 password="TioTioTio333",
                                                 database="pur_beurre")
                                    

        self.cursor = self.connexion.cursor()

        user = "jbaw"

        self.cursor.execute("""
        SET NAMES 'utf8';
        """)

        user = "root"
        self.cursor.execute("""
        DROP DATABASE pur_beurre""")

        
if __name__ == "__main__":

    delete = delete_data()
    delete.delete()
