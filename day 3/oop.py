class student:

    def __init__(self,name):
        self.name=name
      
    def greet(self):
        return f"hello {self.name}"

stu_obj=student('samiyas') #create object
print(stu_obj.greet())


class passengers():
    def __init__(self):
        self.name
        self.passport_no
    def __str__(self):
        return self.name


class flight():
    def __init__(self):
        self.destination
        self.departure
        self.passengers=[]
        self.capacity
    def add_passengers(self,name,passport_num):
        obj=passengers(name,passport_num)
        if self.capacity<=self.passengers.count():
            return f"flight is full"
        else:
            self.passengers.append(obj)
            return f"passenger {name} added to flight"
       
       
        





  