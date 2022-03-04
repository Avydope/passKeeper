
while True:
    var = 1
    if (var == 1):
        master_pass = input ("User Validation: ")
        var = 0
        break
    else: 
        quit

''' SETUP: to run ONCE  '''
'''file = open("Login.txt","w")
file.write (master_pass)
file.close()''' 

def add():
    name = input("Account username: ")
    passw = input("Account password: ")
    with open('passwords.txt','a') as f:
        f.write(name + " : " + passw + "\n")

def view():
    with open('passwords.txt','r') as f:
        for line in f.readlines():
            print(line)

def mainplan(): 
    while True:
        option = input ("Add new password or view existing ones? (add, view), press q to quit : ")
        if option == "q":
            print("Thank you! ")
            break
        if option == "add":
            add()
        elif option == "view":
            view()
        else:
            print("Invalid option")
            continue 


Flag = 0
''' to run everytime after SETUP '''
fo = open("Login.txt", "r")
file_content = fo.read()
if master_pass == file_content:
    Flag = 1
else: 
    Flag = -1


if Flag == 1:
    print('Access Granted')
    mainplan()
elif Flag == 0:
    print('Main validation set')
else:
    print('Access Denied')
    quit






