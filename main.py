#MAGIC/DUNDER METHODS
class Student:

  def __init__(self, name):  #called when an object is created
    self.name = name

  def __str__(self):  #Returns a string representation of the object
    return f"str: My name is {self.name}"

  def __repr__(self):  #Returns a string representation of the object
    return f"repr: My name is {self.name}"

  def __len__(self):  #Returns the length of the object
    return len(self.name)

  def __call__(self):  #Allows an object to be called as a function
    print("This function is used to create for call")


s = Student("Tahmid")
print(str(s))
print(repr(s))
print(len(s))
s()