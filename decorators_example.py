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
def cooking():
  print("cooking !")
  time.sleep(2)

if __name__ == "__main__":
    cooking()
