def add(*n):
    result = 0
    for i in n:
        result += i
    return result
#
# answer = add(1,2,3,4,5,6,7,8,9,10)
# print(answer)

def calculate(n, **kwargs):
    n += kwargs["add"]
    print(n)
    n -= kwargs["sub"]
    print(n)
    n *= kwargs["multi"]
    print(n)
    n /= kwargs["div"]
    print(n)


calculate(10, add=10, sub=5, multi=6, div=10)


class Car:
    def __init__(self, **kw):
        self.brand = kw.get("brand")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")
        self.mileage = kw.get("mileage")
        self.price = kw.get("price")


my_car = Car(brand="Chevrolet", model="Impala 1967", seats=4, colour="Black", mileage=20, price=8000000)
print(my_car.brand, my_car.colour, my_car.model)

kuber_car = Car(brand="Nissan", colour="Black")
print(kuber_car.brand, kuber_car.colour, kuber_car.model)
