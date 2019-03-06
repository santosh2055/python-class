class rectangle():
    def __init__(self,breadth,length):
      self.breadth = breadth
      self.length = length

    def area(self):

        return self.breadth*self.length

length  = int(input("Enter length of rectangle:"))
breadth = int(input("Enter breadth of rectangle:"))

obj = rectangle(length,breadth)
print("Area of rectangle:", obj.area())