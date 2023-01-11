#1)
#print("Arvuta peast! ...4*100-55")
#o_vastus=4*100-55
#vastus=int(input("Lahenda ülesanne ..."))
#k=1
#while vastus!=o_vastus:
#    print("Viga! Sisesta Õige vastus on ...", )

#    vastus=int(input("Sisesta vastus ..."))
#    k+=1
#while True:
#    print("Õige vastus! Katsed oli ...",k )
#    break

#2)
#x=0
#while True:
#    if x%2==1:
#        print(x, end=" ")
#    x+=1
#    if x==30: break
#print("for:")
#for x in range(0,30,1):
#    if x%2==1: print(x, end="")

print("*** NUMBRIDEGA MÄNGUD ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = (abs(int(input("Sisestage täisarv => "))))# sulud panesin
        break
    except ValueError:
         print("See ei ole täisarv")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Nulliga pole mõtet midagi peale hakata")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Määrake, kui palju paaris ja mitu paaritu numbrit on arvus")
    print()
    c=b=a#panin võrdus märk
    paaris =0#kustutasin võrdlus märk
    paaritu = 0#kustutasin võrdlus märk
    while b > 0:#panin : märk
            if b % 2 == 0:#panin võrdus märk
                    paaris += 1# teisiti panin =+
            else:
                    paaritu += 1 # teisiti panin =+
            b = b // 10
    print("Paarisarvud:",paaris)# panin koma
    print("paarituid numbreid:",paaritu)# teisiti panin =+
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Pöörake * sisestatud number")
    print()
    b=0
    while a > 0:#panin : märk
        number = a % 10
        a = a // 10
        b = b * 10
        b =+ number
    print("*Tagurpidi* number", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Syracuse hüpoteesi testimine")
    print()
    if c % 2 == 0:
        print("с - paarisarv. Jagame 2-ga.")
    else:
        print("с - paaritu number. Korrutage 3-ga, lisage 1 ja jagage 2-ga.")
    while c != 1:
            if c % 2 == 0:
                    c = c / 2
            else:
                    c = (3*c + 1) / 2 
            print(round(c), end="") 
            break
    print()
    print("on tõestatud")
