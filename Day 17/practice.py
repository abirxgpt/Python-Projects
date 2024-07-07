# These Files were just for Practice and learn About Classes and how to work on the classes and how to make classes
class User:
    def __init__(self, user_id, user_name):
        print("New User Created")
        self.id = user_id
        self.username = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1


user1 = User("001", "abirs")
user2 = User("002", "jerry")
print(user1.followers)
print(user2.followers)
print(user1.following)
print(user2.following)


user1.follow(user2)


print(user1.followers)
print(user2.followers)
print(user1.following)
print(user2.following)

# class Car:
#
#     def __init__(self, seats, tyres, mileage):
#         self.seats = seats
#         self.tyre = tyres
#         self.milage = mileage
#     def is_a_race_car(self):
#         self.seats = 2
#         self.milage = self.milage/2
#
# car1 = Car(4, 4, 100)
# print(car1.seats)
# print(car1.milage)
# car1.is_a_race_car()
# print(car1.seats)
# print(car1.milage)
