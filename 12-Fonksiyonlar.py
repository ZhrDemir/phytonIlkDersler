def ekranaYaz():
    print("Merhaba")


ekranaYaz()

def ekranaYaz(isim):
    print(isim + " selam ")
    
ekranaYaz("zehra")
    
def karesiniAl(sayi):
    return sayi**2

print (karesiniAl(11))

def defaultPar(isim="zehra"):
    print(f"Merhaba {isim}")
    
defaultPar()
defaultPar("ayse")  
      