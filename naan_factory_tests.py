# test go here for the separation of concerns.
# here we run the factory (functions)
from naan_factory_functions import *

print("testing_make_dough with 'water' and 'flour'. Expected --> 'dough'")
print(make_dough("water", "flour") == "dough")
print('got:', make_dough('water','flour'))

print("testing_make_dough with 'water' and 'egg'. Expected --> 'not dough'")
print(make_dough("water", "egg") == "not dough")
print('got:', make_dough('water','egg'))

print("testing_bake_dough with 'dough'. Expected --> 'Naan'")
print(bake_dough('dough') == "Naan")
print('got:', bake_dough('dough'))

print("testing_bake_dough with 'dough'. Expected --> 'Not Naan'")
print(bake_dough('tissues') == "Not Naan")
print('got:', bake_dough('tissues'))