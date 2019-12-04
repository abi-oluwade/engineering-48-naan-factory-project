# Tests! (print)
# test go here for the separation of concerns.
# here we run the factory (functions) as it is messy to keep our functions, test and production code in the same 
# environment this second stage is where we produce the 'print' statements to ensure the functions are operating
# properly.


from naan_factory_functions import *

# make_dough Tests!
print("testing_make_dough with 'water' and 'flour'. Expected --> 'dough'")
print(make_dough("water", "flour") == "dough")
print('got:', make_dough('water','flour'))

print("testing_make_dough with 'water' and 'egg'. Expected --> 'not dough'")
print(make_dough("water", "egg") == "not dough")
print('got:', make_dough('water','egg'))

# bake_dough Tests!
print("testing_bake_dough with 'dough'. Expected --> 'Naan'")
print(bake_dough('dough') == "Naan")
print('got:', bake_dough('dough'))

print("testing_bake_dough with 'dough'. Expected --> 'Not Naan'")
print(bake_dough('tissues') == "Not Naan")
print('got:', bake_dough('tissues'))

# factory_run Tests!
print("testing_factory_run with 'water' and 'flour'. Expected ----> 'Naan'")
print(factory_run("water", "flour") == "Naan")
print("got:", factory_run('water', 'flour'))

print("testing_factory_run with 'ice' and 'flour'. Expected ----> 'Not Naan'")
print(factory_run('ice','flour') == 'Not Naan')
print('got:', factory_run('ice', 'flour'))