name=str(input("what is ur name:"))
gender=str(input("what is ur gender"))
weight=float(input("what is ur weight:"))
height=float(input("what is ur height:"))
age=int(input("what is ur age:"))

def bmi():
   
    bmi=weight/(height*height)
print(bmi())

def bmr():
    if gender == "male":

        bmr1=88.362+(13.397*weight)+(4.799*height)-(5.677*age)
    if gender == "female":
        bmr2= 447.593+(9.247*weight)+(3.098*height)-(4.330*age)
    
    print(bmr())


    


