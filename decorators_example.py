# Example of decorator 
from collections.abc import Callable

import time 

# Defintition of the add_time as a decorator
def add_time(func):
    def myinner(*args, **kwargs):
        time_initial = time.time()
        func(*args, **kwargs)
        print(f"cooking time {(time.time()-time_initial):0.2f}")
    return myinner

@add_time
def cooking_breakfast() -> None:
  print("Cooking breakfast")
  time.sleep(2)

@add_time
def cooking_lunch() -> None:
  print("Cooking lunch")
  time.sleep(4)

@add_time
def cooking_batch(size: int, meal_type: Callable)  -> None:
  print("###############")
  for i in range(0, size):
    print(f"cooking_batch {i}")
    meal_type()
  print("###############")


if __name__ == "__main__":
    cooking_batch(5, cooking_lunch )
    cooking_lunch()
