def my_nid(fName,Date_of_birth,Gender,Address):

    print(fName + " " +Date_of_birth+ " " +Gender+ " "+Address)

my_nid("Tajfiya", "3rd april 2004","Female","Rajshahi")    



#class task

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth

my_rectangle = Rectangle(10, 5)
print("Area of the rectangle:", my_rectangle.calculate_area())
