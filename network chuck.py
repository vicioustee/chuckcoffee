



   
if 2> 3:
    print("Yep its true")
    print("sure its still true")
else:
    print("nop no true")

name=input("what is your name?")


menu="Black coffee , Espresso,Latte, Cappucino , Frappucino"

order=input(name+ ",what would you like our menu today?Here is what we are serving.\n"+menu)



quantity=int(input("how many coffees would you like\n"))

#set the price for coffee
if order=="frapuccino":
   price = 15

if order=="Latte":
   price = 6


if order=="Black coffee":
   price = 3

   
if order=="Cappucino":
   price = 12

   print("price")

camping_List= ["tent","sleeping bags", "water ",
   "raspberry", "coffee", "knife", "ethernet" "cable",
   "flash drive", "beard oil", "marshmallows"]


camping_site=["crystal lake",404,89.3,True]

me=camping_List[-1]
print(me)

camping_List.extend(["toilet paper","bidet"])
print(camping_List)

camping_List.insert(-1,"toilet")
print(camping_List)

print(camping_List.pop(0))
print(camping_List)

