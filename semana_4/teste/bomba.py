import time

for i in [10,9,8,7,6,5,4,3,2,1]:
    print(i)
    time.sleep(1)
    if i == 1:
        print('BOOM')

