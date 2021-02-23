import dbm

db = dbm.open("websites", "c")
db['www.python.org'] = "Python home page"
print(db['www.python.org'])
db.close()
