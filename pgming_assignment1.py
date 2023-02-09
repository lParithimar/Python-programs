#first Program 
print("Hello Python")

#second program
while True:
    print("Enter two nos to do arithmetic operation ['q' to quit]")
    try:
        no1=input("enter the first number")
        if no1=='q' or no1=='Q':
            break
        else:
            no1=float(no1)
        no2=float(input("enter the second number"))
        choice=int(input("enter '1' for addition and '2' for division"))
        if choice==1:
            print(f"The addition of {no1} and {no2} is {no1+no2}")
        elif choice==2:
            print(f"The division of {no1} and {no2} is {no1/no2}")
        else:
            print(f"Please enetr 1 or 2")
    except Exception as e:
        print(f"Please enter a valid no {e}")



#Third Program
class Triangle_Area():
    indicator1=str()
    indictor2=str()
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        print(f"The area of a triangle of base={self.base} and height={self.height} is {0.5*self.base*self.height}")
        while True:
            try:
                
                choice=input("Do you want to calculate area for other triangle  ['q' to quit] ")
                if choice in ['q','Q']:
                    break
                else:
                    print(f"Please enter Base and Height of a triangle to compute area")
                    self.base=input("Eneter base of a triangle")
                    self.height=input("Enetr the height")
                    if self.base.isnumeric():
                        self.base=float(self.base)
                        
                    else:
                        Triangle_Area.indicator1='base'

                    if self.height.isnumeric():
                        self.height=float(self.height)
                    else:
                        Triangle_Area.indicator2='height'
                    print(f"The area of a triangle of base={self.base} and height={self.height} is {0.5*self.base*self.height}")

                    
                
            except Exception as e:
                if Triangle_Area.indicator1=='base':
                    print(f"Please enter valid base")
                    Triangle_Area.indicator1=''
                if Triangle_Area.indicator2=='height':
                    print(f"Please enter a valid height")
                    Triangle_Area.indicator2=''


t=Triangle_Area(5,10)
t.area()




#fourth program

class Swap_two_variables():
    def __init__(self,value1,value2):
        self.value1=value1
        self.value2=value2
        

    def swap(self):
        print(f"Before swapping value1={self.value1} and value2={self.value2}")
        self.value1,self.value2=self.value2,self.value1
        print(f"After swapping value1={self.value1} and value2={self.value2}")

        while True:
            choice=input("Do you want to proceed further [Enetr 'q' to quit ]")
            if choice in ['q','Q']:
                break
            else:
                val1=input(f"Enter a value for a variable one")
                val2=input(f"Enter a value for a variable two")
                print(f"Before swapping value1={val1} and value2={val2}")
                val1,val2=val2,val1
                print(f"After swapping value1={val1} and value2={val2}")


swp=Swap_two_variables(10,"year")
swp.swap()




#Fifth program

import random

class Random_no_generator():
    def random_no(self):
        while True:
            print(random.random())
            choice=input("Enter [q to quit]")
            if choice in ['q','Q']:
                break

R=Random_no_generator()
R.random_no()


