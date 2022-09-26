from dataclasses import dataclass
def sum_list(random_list)->int:
    if random_list:
        return random_list[0] + sum_list(random_list[1:])
    else:
        return 0

def mult_list(random_list)->int:
    if random_list:
        return random_list[0] * mult_list(random_list[1:])
    else:
        return 1

def check_age(dogs, age):
    if dogs:
        if dogs[0].age == age:
            return dogs[0].name
        else:
            return check_age(dogs[1:], age)
    else:
        return None

print(sum_list([1,2,3]))
print(mult_list([1,2,4]))

@dataclass
class Dog:
    name: str
    age: int
    
d1 = Dog("Fido", 6)
d2 = Dog("Nemo", 3)
d3 = Dog("Bob", 1)
pack = [d1, d2, d3]
print(pack)

print(check_age(pack, 1))