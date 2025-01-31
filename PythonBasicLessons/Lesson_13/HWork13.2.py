# Class "Digital counter"
class Counter:

   def __init__(self, current=1, min_value=0, max_value=10): # Initiation by attributes of the class Counter object. Instance attributes.
       self.current = current
       self.min_value = min_value
       self.max_value = max_value

   def set_current(self, start):            # method of setting the start value of the counter
       if start < self.min_value or start > self.max_value:
           raise ValueError(f" Exception. The limit has been reached")         #Maximum or minimum reached
       self.current = start

   def set_max(self, max_max):          # method of setting the max value of the counter
        self.max_value = max_max

   def set_min(self, min_min):          # method of setting the min value of the counter
       self.min_value = min_min

   def step_up(self):
       self.set_current(self.current + 1)       # the step_up method increments the counter by 1

   def step_down(self):
       return self.set_current(self.current - 1)        # the step_down method decrements the counter by 1

   def get_current(self):
       return self.current


counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
print(counter.get_current())

assert counter.get_current() == 10, 'Test1'         # setting the start value of the counter
try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e)  # Достигнут максимум
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)                                  # setting the min value of the counter
counter.step_down()
counter.step_down()
counter.step_down()
print(counter.get_current())
assert counter.get_current() == 7, 'Test3'          # setting the start value of the counter
try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e)  # Досягнут мінімум
assert counter.get_current() == 7, 'Test4'
print(counter.get_current())



