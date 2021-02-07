def add(*args):
     #print shows the tuple
     print(type(args))
     #loop through the tupple
     #declare var sum
     sum=0
     for n in args:
         #prints each number  in the tupple
         # print(n)
         sum +=n
     return sum

# can add any number of values to add
print(add(3, 4, 5))
