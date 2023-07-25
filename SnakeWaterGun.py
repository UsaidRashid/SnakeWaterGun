import random

Computer=["Snake","Water","Gun"]
n=1
u=0
b=0

while (n<=10):
    BOT=random.choice(Computer)
    user=input("ENTER S FOR SNAKE \n"
               "ENTER W FOR WATER \n"
               "ENTER G FOR GUN \n")

    if user == "S" or user=="s":
        if BOT=="Snake":
            print("ROUND TIED AS BOTH USER AND BOT CHOSE SNAKE ")
            print("UPDATED SCORES")
            print("USER SCORE : ",u)
            print("BOT SCORE : ",b)
        elif BOT=="Water":
            print("YOU WON THE ROUND AS BOT CHOSE WATER ")
            u+=1
            print("UPDATED SCORES")
            print("USER SCORE : ",u)
            print("BOT SCORE : ", b)
        elif BOT=="Gun":
            print("BOT WON THE ROUND AS IT CHOSE GUN ")
            b+=1
            print("UPDATED SCORES")
            print("USER SCORE : ",u)
            print("BOT SCORE : ",b)
        n=n+1

    elif user == "W" or user=="w":
        if BOT == "Snake":
            print("BOT WON THE ROUND AS IT CHOSE SNAKE ")
            print("UPDATED SCORES")
            b+=1
            print("USER SCORE : ", u)
            print("BOT SCORE : ", b)
        elif BOT == "Water":
            print("ROUND TIED AS BOTH USER AND BOT CHOSE WATER ")
            print("UPDATED SCORES")
            print("USER SCORE : ", u)
            print("BOT SCORE : ", b)
        elif BOT == "Gun":
            print("YOU WON THE ROUND AS BOT CHOSE GUN ")
            u += 1
            print("UPDATED SCORES")
            print("USER SCORE : ", u)
            print("BOT SCORE : ", b)
        n=n+1

    elif user == "G" or user=="g":
        if BOT == "Snake":
            print("YOU WON THE ROUND AS BOT CHOSE SNAKE ")
            u+=1
            print("UPDATED SCORES")
            print("USER SCORE : ", u)
            print("BOT SCORE : ", b)
        elif BOT == "Water":
            print("BOT WON THE ROUND AS IT CHOSE WATER ")
            b += 1
            print("UPDATED SCORES")
            print("USER SCORE : ", u)
            print("BOT SCORE : ", b)
        elif BOT == "Gun":
            print("ROUND TIED AS BOTH USER AND BOT CHOSE GUN ")
            print("UPDATED SCORES")
            print("USER SCORE : ", u)
            print("BOT SCORE : ", b)
        n=n+1

    else:
          print("PLEASE ENTER VALID KEYWORD")
