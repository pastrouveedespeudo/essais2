import mysql.connector 

class MYSQL:

    def data(self):
        
        self.connexion = mysql.connector.connect(host="localhost",
                                                 user="root",
                                                 password="TioTioTio333")

        self.cursor = self.connexion.cursor()

        user = "root"

        self.cursor.execute("""
        CREATE DATABASE imageimage""")

    def connexion(self):
        
        self.connexion = mysql.connector.connect(host="localhost",
                                                 user="jbaw",
                                                 password="TioTioTio333",
                                                 database="pur_beurre")
        self.cursor = self.connexion.cursor()

        user = "root"
        self.cursor.execute("""
        USE pur_beurre""")


    def categorie(self):
        user = "jbaw"

        self.cursor.execute("""

        CREATE TABLE Categorie(
        id INT UNSIGNED NOT NULL AUTO_INCREMENT,
        nom VARCHAR(25) NOT NULL,

        PRIMARY KEY(id))
        
        ENGINE = InnoDB;
        """)


    def objet(self):

        user = "jbaw"

        self.cursor.execute("""

        CREATE TABLE Objet(
        id INT UNSIGNED NOT NULL AUTO_INCREMENT,
        categorie VARCHAR(25) NOT NULL,
        nom VARCHAR(25) NOT NULL,
        description TEXT,
        
        PRIMARY KEY(id))
        
        ENGINE = InnoDB;
        """)

    def liaison_objet_cat(self):
        
        user = "jbaw"

        self.cursor.execute("""

        CREATE TABLE Liaison(
        id_objet INT UNSIGNED NOT NULL,
        id_categorie INT UNSIGNED NOT NULL,

        PRIMARY KEY(id_objet, id_categorie)
        
        FOREIGN KEY (id_objet)
        REFERENCES Objet(id)

        FOREIGN KEY (id_categorie)
        REFERENCES Cateforie(id)

        ENGINE = InnoDB;
        """)
        












