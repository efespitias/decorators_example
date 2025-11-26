# Example of decorator 
def add_time(func):
    def myinner():
        print("time")
        func()
    return myinner


@add_time
def cooking():
  print("cooking !")

cooking()





    





