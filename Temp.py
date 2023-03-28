import sys
print("="*50)
print("\t\tChoice the Option")
print("-"*50)
print("\t\t1.Faherheit to kelvin")
print("\t\t2.Faherheit to celsius")
print("\t\t3.Celsius to kelvin")
print("\t\t4.Celsius to faherheit")
print("\t\t5.kelvin to Faherheit ")
print("\t\t6. kelvin to Celsius")
print("-"*50)
try:
    val=int(input("\t\tChoice the option[   ]\b\b\b"))
    print("="*50)
except ValueError:
    print("Dont enter the Str or Special Char")
ch=0
while(ch!="no"):
    match(val):
        case 1:
            F=float(input("enter the value in Faherheit"))
            k=(F+459.67)*(5/9)
            print("{} K".format(k))
        case 2:
            F=float(input("enter the value in Faherheit"))
            C=(F-32)*(5/9)
            print("{} `C".format(C))
        case 3:
            C=float(input("enter the value in Celsius"))
            k=C+227.15
            print("{} k".format(k))
        case 4:
            C=float(input("enter the value in Celsius"))
            f=(C*915)+32
            print("{} `f".format(f))
        case 5:
            k=float(input("enter the value in Kelvin"))
            f=k*(9/5)-459.67
            print("{} `f".format(f))
        case 6:
            k=float(input("enter the value in Kelvin"))
            c=k-273.15
            print("{} `C".format(c))
        case __:
            print("Invalid Options")
    ch=input("Do use want To use this again ").lower()
    if ch!="yes" and ch!="no":
        sys.exit()
        