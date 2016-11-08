#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module loads the values into the pets database"""

import sqlite3 as lite
import sys

con = None

try:
    con = lite.connect('pets.db')
    cur = con.cursor()


    cur.execute('''INSERT INTO person VALUES(1,'James','Smith',41),
        (2,'Diana','Greene',23),
        (3,'Sara','White',27),
        (4,'William','Gibson',23);''')
    cur.execute('''INSERT INTO pet VALUES(1,'Rusty','Dalmation',4,1),
        (2,'Bella','AlaskanMalamute',3,0),
        (3,'Max','CockerSpaniel',1,0),
        (4,'Rocky','Beagle',7,0),
        (6,'Spot','Bloodhound',2,1);''')
    cur.execute('''INSERT INTO person_pet VALUES(1,1),
        (1,2),
        (2,3),
        (2,4),
        (3,5),
        (4,6);''')
    con.commit()

except lite.Error, e:

    print "Error %s:" % e.args[0]
    sys.exit(1)

finally:

    if con:
        con.close()
