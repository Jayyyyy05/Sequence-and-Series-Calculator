# Arithmetic
def Arithmetic_explicit(a, n, d):
    return a + ((n - 1) * d)

def Arithmetic_sum(a, n, d):
    return (n / 2) * ((2 * a) + ((n - 1) * d))

# Geometric
def Geometric_explicit(a, n, r):
    return a * (r ** (n-1))

def Geometric_sum(a, n, r):
    return a * (r ** (n - 1))/(r - 1)

def Geometric_Infinite(a, r):
    return a / (1 - r)

# Choice
while True:
    choice = input("1. Arithmetic\n2. Geometric\nInput: ")
    print()

    #Arithmetic
    if choice == "1":
        Achoice = input("1. Finding nth term\n2. Finding sum of n terms\nInput: ")
        print()

        if Achoice == "1":
            print("Formula: a + (n - 1) * d")
            a = float(input("Input the first term (a): "))
            n = int(input("The total number of terms (n): "))
            d = float(input("Common difference (d): "))
            
            print(f"The nth term is: {Arithmetic_explicit(a, n, d)}")
            
        elif Achoice == "2":
            print("Formula: n / 2 * (2 * a + (n - 1) * d)")
            a = float(input("Input the first term (a): "))
            n = int(input("The total number of terms (n): "))
            d = float(input("Common difference (d): "))
            
            print(f"The sum of nth terms is: {Arithmetic_sum(a, n, d)}")

    #Geometric
    elif choice == "2":
        Gchoice = input("1. Finding nth term\n2. Finding sum of n terms\n3. Sum of infinite series \nInput: ")
        print()
        
        if Gchoice == "1":
            print("Formula: a * r^(n-1)")
            a = float(input("Input the first term (a): "))
            n = int(input("The total number of terms (n): "))
            r = float(input("Common ratio (r): "))
            
            print(f"The sum of nth terms is: {Geometric_explicit(a, n, r)}")
            
        elif Gchoice == "2":
            print("Formula: a * r ** n - 1 / r - 1")
            a = float(input("Input the first term (a): "))
            n = int(input("The total number of terms (n): "))
            r = float(input("Common ratio (r): "))
            
            print(f"The sum of nth terms is: {Geometric_sum(a, n, r)}")  

        elif Gchoice == "3":
            print("Formula: a / (1 - r)")
            a = float(input("Input the first term (a): "))
            n = float(input("The total number of terms (n): "))
            
            print(f"The sum of infinite terms is: {Geometric_Infinite(a, r)}")  
        
print()