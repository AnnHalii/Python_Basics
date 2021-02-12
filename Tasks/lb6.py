import sys

# 1
def moon_weight(weight, counter):
    for i in range(weight, weight+counter):
        print(i*0.165)


moon_weight(60,15)

# 2
def moon_weight_1(weight, counter, year):
    for i in range(weight, weight+year):
        print(counter+i*0.165)


moon_weight_1(60, 1, 5)

# 3
def moon_weight():
    print("Please enter the starting weight:")
    weight = int(sys.stdin.readline())
    print("Please enter the increase per year:")
    counter = float(sys.stdin.readline())
    print("Please enter the number of years:")
    year = int(sys.stdin.readline())
    return (weight+year) * counter


print(moon_weight())


