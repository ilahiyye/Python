
def triangle(n=4, s="*"):
    for i in range(0, n):
        print(" "*(n-i) + s*i + s*(i+1))

number = int(input('length triangle: '))
simvol = input('input simvol: ')

triangle(number, simvol)
    
    
            
