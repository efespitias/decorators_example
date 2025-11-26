# Example of decorator 

import time 

def add_time(func):
    def myinner():
        time_initial = time.time()
        
        func()
        # time_initial = time.ctime(1627908313.717886)
        print(f"cooking time {(time.time()-time_initial):0.2f}")

    return myinner


@add_time
def cooking():
  print("cooking !")
  time.sleep(2)

cooking()





    





