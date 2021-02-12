import copy
import pickle

# 1
class Car: pass


car1 = Car()
car1.wheels = 4
car2 = car1
car2.wheels = 3
print(car1.wheels)

car3 = copy.copy(car1)
car3.wheels = 6
print(car1.wheels)


# 2
data = ['books', 'beer', 'friends', 'eat']

save_file = open('favourite.dat', 'wb')
pickle.dump(data, save_file)
save_file.close()
load_file = open('favourite.dat', 'rb')
loaded_data = pickle.load(load_file)
load_file.close()
print(loaded_data)