# here we run the factory (functions)
from naan_factory_functions import *

print( "Welcome to my naan factory!")
produce1= input("What is the first produce you want?")
produce2 = input("Second produce?")

output1 = make_dough(produce1, produce2)
final_output = bake_dough(output1)

print("Well done! You made some:", final_output)
