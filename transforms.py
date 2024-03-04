import sympy
from sympy import *
from sympy.plotting import plot


t= symbols('t',real = True)
s= symbols('s',real = True)
a,n,b = symbols('a n b')

while(True):
    print("\n")
    print("__________________________________________________\n")
    print(" LAPLACE TRANSFORM AND INVERSE LAPLACE TRANSFORM")
    print("__________________________________________________\n")
    print("1. Laplace transform")
    print("2. Inverse laplace transform")
    print("3. Exit")
    ch = int(input("\nEnter your choice: "))
    print("__________________________________________________")
    
    if (ch==1):
        while(True):
            print("\nLaplace Transform of: ")
            print("    1. Standard functions")
            print("    2. Heaviside or DiracDelta functions")
            choice = int(input("\nEnter your choice: "))
            
            if(choice==1):
                eq = eval(input("\nEnter expression in terms of 't':\n"))
                break
            
            elif(choice==2):
                eq = eval(input("\nEnter expression in terms of 'Heaviside' of 't' / 'DiracDelta' of 't':\n"))
                break
            
            else:
                print("** ENTER A VALID CHOICE! **")
            
        res = laplace_transform(eq,t,s,noconds=True)
        print("\nAfter Laplace transform:")
        print(res)
        plot(eq,title='Before transformation')
        plot(res,title='After transformation')
        print("\n************************************************")
    
    
    elif(ch==2):
        eq = eval(input("\nEnter expression in terms of 's':\n"))
        res = inverse_laplace_transform(eq,s,t)
        res_t = res.subs(DiracDelta(t), 0).subs(Heaviside(t), 1)
        print("\nAfter Inverse Laplace transform:")
        print(res_t)
        plot(eq,title='Before transformation')
        plot(res_t,title='After transformation')
        print("\n************************************************")

    elif(ch==3):
        break
    
    else:
        print("\n ** ENTER A VALID OPTION! **")

