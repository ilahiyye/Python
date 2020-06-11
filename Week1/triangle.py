if __name__ == '__main__':

    number = int(input('length triangle: '))
    simvol = input('input simvol: ')
    
    for i in range(0, number):
        
      print(" "*(number-i) + simvol*i + simvol*(i+1))
            
