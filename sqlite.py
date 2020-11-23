# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 02:45:37 2020

@author: mathiam
"""
import sqlite3
from OOP import player
conn = sqlite3.connect("Player.db")

cu = conn.cursor()

cu.execute("""CREATE TABLE Player(
        id integer PRIMARY KEY AUTOINCREMENT,
        prenom text,
        nom text,
        age integer,
        wage real,
        position text
    )
    """)

cu.execute("INSERT INTO Player(prenom, nom, age, wage, position) VALUES ('Abdoulaye','Fall',23,300000,'position')")


p1 = player("Patrick", "Mahomes II", 25, 258631, "quarterback")
p2 = player("Odell","Beckham Jr.",28, 286351,"wide receiver")

cu.execute("INSERT INTO Player (prenom, nom, age, wage, position) VALUES (?,?,?,?,?)", (p1.prenom, p1.nom, p1.age, p1.wage, p1.position))

cu.execute("INSERT INTO Player (prenom, nom, age, wage, position) VALUES (?,?,?,?,?)", (p2.prenom, p2.nom, p2.age, p2.wage, p2.position))

conn.commit()

cu.execute("SELECT * FROM Player")
print(cu.fetchall())
#conn.close()


cu.execute("SELECT * FROM player ORDER BY age DESC")
print(cu.fetchall())
conn.close()
