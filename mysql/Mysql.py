import mysql.connector

class Mysql:

    def __init__(self):

        pass

    def database(self):

        self.connexion = mysql.connector.connect(host = "localhost",
                                                 user = "root",
                                                 password = "TioTioTio333")
                                                 
        self.cursor = self.connexion.cursor()

        user = "root"
        
        self.cursor.execute("""
        CREATE DATABASE Test_image;
        GRANT ALL PRIVILEGES ON 'test_image'.* TO
        'jbaw'@'localhost';
        """)


    def connexion(self):

        self.connexion = mysql.connector.connect(host = "localhost",
                                                 user = "jbaw",
                                                 password = "TioTioTio333",
                                                 database = "Test_image")
        self.cursor = self.connexion.cursor()

        user = "jbaw"
        self.cursor.execute("""
        USE Test_image""")




    def table_ciel_image(self):


        
        self.cursor.execute("""

        CREATE TABLE image_ciel (
        
        id INT AUTO_INCREMENT NOT NULL,
        nom VARCHAR(50) NOT NULL,
        couleur BIGINT NOT NULL,
        image BLOB NOT NULL,
        categorie VARCHAR(25),

        
        PRIMARY KEY(id) );
        

        """)
        self.connexion.commit()

    def tables_ciels_images(self):
        
        self.cursor.execute("""

        CREATE TABLE images_ciels(
        
        id INT AUTO_INCREMENT NOT NULL,
        nom VARCHAR(50) NOT NULL,
        couleur BIGINT NOT NULL,
        image BLOB NOT NULL,

        PRIMARY KEY(id),

        FOREIGN KEY id
        REFERENCES image_ciel (id) )
        ENGINE=InnoDB;
        """)

        

    def tables_matches(self):
        self.cursor.execute("""

        
        """)

    def table_objet(self):
        pass
    

    def forme_geometrique(self):
        pass
    #faire une jointure avec table objet

    def ressenti(self):
        pass
    #h/f





















    
