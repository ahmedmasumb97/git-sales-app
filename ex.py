
import random



# rimport random

random = (([str(random.randint(0,9)) for i  in range(6)]))
print(random)


import random

number = [random.randint(0,9) for i in range(6)]
print(''.join(str(number)))

fruits  = ['9', '5', '2']
print(''.join(str(fruits)))