import os, time, random, hashlib
database = {}

try:
  f = open("database.txt", "r")
  database = eval(f.read())
  f.close()
except:
  f = open("database.txt", "w")
  f.close()

def hash_password(password, salt):
    return hashlib.sha256(f"{password}{salt}".encode()).hexdigest()

def createUser():
  time.sleep(1)
  os.system("clear")
  username = input("Username: ")
  password = input("Password: ")
  if username in database:
    print("ERROR: Username exists")
    return

  salt = random.randint(1000, 9999)
  hash = hash_password(password,salt)
  
  database[username] = {"password": hash, "salt": salt}

  print("User added")

def login():
  time.sleep(1)
  os.system("clear")
  username = input("Username: ")
  password = input("Password: ")
  if username not in database:
    print("ERROR: Username does not exists")
    return

  salt = database[username]["salt"]
  hash = hash_password(password,salt)
  

  if database[username]["password"]==hash:
    print("Logged in")
  else:
    print("Username or password incorrect")


while True:
  menu = input("1: New User\n2: Login\n> ")
  if menu == "1":
    createUser()
  elif menu == "2":
    login()
  else:
    print("Error: Please enter a valid input.")
  f = open("database.txt", "w")
  f.write(str(database))
  f.close()  



