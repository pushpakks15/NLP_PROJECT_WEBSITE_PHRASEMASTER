#We are going to use file to store our entries
import json
class Database:

    def insert_entry(self,name,email,password):
        with open("db.json" ,"r") as f:
            database=json.load(f)
        if email in database:
            return 0
        if len(email)<10:
            return 0
        else:
            database[email]=[name,password]
            with open("db.json","w") as wf:
                json.dump(database,wf,indent=4)
            return 1

    def check_login(self,email,password):
        with open("db.json","r") as f:
            database=json.load(f)
        if email in database:
            if database[email][1]==password:
                return 1
            else:
                return 0
        else:
            return 0

