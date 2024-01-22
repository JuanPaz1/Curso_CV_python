import random
import time
c = random.randint(0, 10)
d = random.randint(0, 10)
while c != d:
    print(c)
    c = random.randint(0, 10)
    d = random.randint(0, 10)
    print('c:{} \nd:{}'.format(c, d))
    time.sleep(0.5)