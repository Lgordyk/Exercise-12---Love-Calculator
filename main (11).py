# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

countfort = name1.lower().count("t")+name2.lower().count("t")
countforr = name1.lower().count("r")+name2.lower().count("r")
countforu = name1.lower().count("u")+name2.lower().count("u")
countfore1 = name1.lower().count("e")+name2.lower().count("e")
countforl = name1.lower().count("l")+name2.lower().count("l")
countforo = name1.lower().count("o")+name2.lower().count("o")
countforv = name1.lower().count("v")+name2.lower().count("v")
countfore2 = name1.lower().count("e")+name2.lower().count("e")

total_for_true = countfort+countforr+countforu+countfore1
total_for_love = countforl+countforo+countforv+countfore2
combined = str(total_for_true) + str(total_for_love)

if int(combined) < 10 or int(combined) > 90:
    print(f"Your score is {combined}, you go together like coke and mentos.")
elif int(combined) >=40 and int(combined) <=50:
    print(f"Your score is {combined}, you are alright together.")
else:
    print(f"Your score is {combined}.")




