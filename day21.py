# class Animal:
#     def __init__(self):
#         self.num_eyes=2

#     def breathe(self):
#         print("Inhale,exhale.")


# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
#     def swim(self):
#         print("moving in water")

# nemo=Fish()
# nemo.swim()   
# nemo.breathe()         
# print(nemo.num_eyes)


#slicing
piano_keys=["a","b","c","d","e","f","g"]
print(piano_keys[2:5])
print(piano_keys[::2])
print(piano_keys[::-1])