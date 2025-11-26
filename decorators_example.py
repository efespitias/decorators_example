# Example of decorator 
import time 

# Defintition of the add_time decorator
def add_time(func):
    def myinner():
        time_initial = time.time()
        func()
        print(f"cooking time {(time.time()-time_initial):0.2f}")
    return myinner

@add_time
def cooking_breakfast():
  print("Cooking breakfast")
  time.sleep(2)

@add_time
def cooking_lunch():
  print("Cooking lunch")
  time.sleep(4)

if __name__ == "__main__":
    cooking_breakfast()
    cooking_lunch()
