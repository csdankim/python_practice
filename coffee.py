# coffee.py

coffee = 10
while True:
    money=int(input("insert coin: "))
    if money==300:
        print("give coffee")
        coffee-=1
        print("remained coffee is %d" % coffee)
    elif money>300:
        print("give change %d and coffee" % (money-300))
        coffee-=1
        print("remained coffee is %d" % coffee)
    else:
        print("return money, no give coffee")
        print("remained coffee is %d" % coffee)
    if not coffee:
        print("run out of coffee, stop selling")
        break
