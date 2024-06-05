def Surface(a,n):
    S=0
    x=1
    h=(a-1)/n
    for i in range(1,n):
        S=S+(1/x)
        x=x+h
    return S*h

def Calcul(a,n):
    pas=0.000001
    epsilon=0.000001
    
    while(1-Surface(a,n)>epsilon):
        a=a+pas
    return a
    
def main():
    a=float(input("Donnez a:"))
    n=int(input("Donnez le nombre des rectangles:"))
    e=Calcul(2.7,n)
    print("Le nombre d'Euler est:{}".format(e))

if __name__=="__main__":
    main()