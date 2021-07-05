n=int(input())
phoneBook={}

for i in range(0,n):
    nameAndPhoneNo=(input()).split(" ")
    name=nameAndPhoneNo[0]
    phone=nameAndPhoneNo[1]
    phoneBook[name]=phone
while True:
    try:
        search=input()
        if search in phoneBook:
            phone=phoneBook[search]
            print(search+"="+str(phone))
        else: print("Not found")
    except:
        break