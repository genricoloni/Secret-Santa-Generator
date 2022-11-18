#funzione che raccoglie una listra di nomi, la duplica e assegna un nome ad un altro
import random
def fun():
    x = input("Quante persone ")
    x = int(x)

    y = list(range(x))

    back = list(range(x))

    for i in range(x):
        y[i] = input()
        back[i] = y[i]

    z = list(range(x))

    count = x

    print(count)

    for i in range(x):
        w = random.randrange(0,count)
        if z[i] == y[w]:
            count += 1
            continue
        z[i] = y[w]
        
        print(back[i], "->",z[i])
        y.remove(y[w])
        count -= 1
        
        


fun()