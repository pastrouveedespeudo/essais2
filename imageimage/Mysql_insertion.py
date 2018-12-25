# -*- coding: utf-8 -*-

import mysql.connector

class Insertion:
    """We can insert products into tables"""

    def __init__(self, oinput):
        """We initializing connexion"""

        code.cle(self)
        
        self.oinput = input("cle ?")
        if self.oinput != self.cle:
            quit()
        
        self.connexion = mysql.connector.connect(host="localhost",
                                                 user="jbaw",
                                                 password="TioTioTio333",
                                                 database="pur_beurre")

        self.cursor = self.connexion.cursor()

        self.cursor.execute("""
        SET NAMES 'utf8';
        """)

    def insertion_table(self):
        pass
