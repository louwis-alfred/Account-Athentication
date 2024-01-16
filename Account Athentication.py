#Index         0       1        2
username = ["Lebron","Stephen","Wade"]
password = ["Leb123","Steph123","wade123"]
 
currentU = input("Username : ")
currentP = input("Password : ")

for x in range(len(username)):
    if currentU == username[x] and currentP == password[x]:
        print("Welcome, " + username[x])
        break
else:

    print("Account not found")
    