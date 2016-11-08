#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module queries the pets database"""

import sqlite3 as lite
import sys

person_ID = raw_input("Input Person ID: ")
con = lite.connect('pets.db')

with con:

    cur = con.cursor()

    cur.execute("SELECT * FROM pet "
                "INNER JOIN person_pet"
                "ON pet.id = person_pet.pet_id"
                "INNER JOIN person"
                "ON person_pet.person_id = person.id"
                "WHERE person.id = ?", (person_ID))
    rows = cur.fetchall()
    for row in rows:
        print "%s %s %s %s" % (row["id"], row["first_name"], row["last_name"], row["age"])
        print "%s %s %s %s %s" % (row["id"], row["name"], row["breed"], row["age"], row["dead"])