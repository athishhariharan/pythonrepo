# for loop exercise with list
# author: prabha subbaian
import pdb

# create list

fruits = ["orange", "banana", "pear", "apple"]
ball_color = ["red", "green", "yellow"]
#print(fruits)
#pdb.set_trace()
i = 0
for ball in ball_color:
    if ball == "red":
        while i < 5:
            print("Ball color", ball)
            i = i +1 
