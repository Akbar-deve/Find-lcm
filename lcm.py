#defining a function find_lcm with x and y parameter
def find_lcm(x,y):
    #check which one is greater 
    if x>y:greater = x
    else:greater = y
    while True:
        if greater%x == 0 and greater%y == 0:
            lcm = greater
            break
        greater+= 1
    print(f'lcm of n1= {x} and n2 = {y} is {greater}')

#declearing inputs
n1=int(input("enter n1 value--> "))
n2=int(input("enter n2 value--> "))
#function calling 
find_lcm(n1,n2)

