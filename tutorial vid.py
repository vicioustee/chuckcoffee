name="Tinaye"

age=23

actual_age=23.98

math=6**7+9-10*8/12
results=age + actual_age +math

print(results)


print("Hello, welcome to Vicious tee coffee!!!!!!!!!")

name=input("what is your name?")


if name == "Ben" or name=="Patricia":
    evilstatus =input("are you evil?\n")
    good_deeds=int(input("how many good deeds have you done today?\n"))
    if evilstatus=="yes" and good_deeds<4:
     print("You are not welcome here " + name +",Get out of here")
     exit()
    else:
       print("Oh u one of the good Bens come on in")
else:
    print("Hello " + name + ",thank you for coming in today")



#print("good day  how are you ")

menu="Black coffee , Espresso,Latte, Cappucino , Frappucino"

order=input(name+ ",what would you like our menu today?Here is what we are serving.\n"+menu)



quantity=int(input("how many coffees would you like\n"))

if order=="frapuccino":
   pricec= 15
elif order == "Black coffee":
   price = 3
elif order=="Latte":
   price=6
elif order=="Black coffee":
   price=3
elif order=="Cappucino":
   price=12
else:
   print("sorry we dont have this here")
   price=0


print(price)
   
total= price*int(quantity)

print("thank you . your total is:$ " + str(total))

print("Sounds good " + name + ", we'll have your  " + order + " ready for you in a moment.")


