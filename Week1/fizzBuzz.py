# -*- coding: utf-8 -*-
fizzBuzz_list = [] 
for i in range(1,100): 
    if i%15==0:
       fizzBuzz_list.append("fizzBuzz")
    if i%3 == 0: 
        fizzBuzz_list.append("fizz")
    elif i%5 ==0:
        fizzBuzz_list.append( "buzz")
    else:
        fizzBuzz_list.append("nothing")
print(fizzBuzz_list)
print("buzz", fizzBuzz_list.count("buzz"))
print("fizz", fizzBuzz_list.count("fizz"))
print("fizzBuzz", fizzBuzz_list.count("fizzBuzz"))
    

