# Functions! ('def')
# Functions are the logic we define and apply to the our code and the definitions/ conditons they must meet
# in order for it to pass the test stage [2] and the run stage [3]. So as we can seen in the below examples, we have 3
# functions that have been defined based on the specifications of the project and the pesudocode we produced.
# As we can see, the 'def' keyword allows us to define the function name and any arguements that it must be given first.
# we can use statements that we've learnt about such as 'if-elif-else' 'while loops' simple logical and mathematical
# operators, and plenty of different key words. The key is to try and use all the tools at our disposal to figure out
# the logic we should apply, for example "would making a list in this 'def' work? or how about a dictionary"


# Basis of a test is around having controlled inputs for known outputs, and testing for these.
# I'll be testing functions and methods

def make_dough(x, y):
    if x != 'water' and y != 'flour':
        return'not dough'
    elif x != 'flour' and y != 'flour':
        return 'not dough'
    elif 'water' in [x, y] and 'flour' in [x, y]:
        return 'dough'

def bake_dough(x):
    if x != 'dough':
         return 'Not Naan'
    elif x == 'dough':
        return 'Naan'

def factory_run(x, y):
    if x != 'water' and y != 'flour':
        return'Not Naan'
    elif x != 'flour' and y != 'flour':
        return 'Not Naan'
    elif 'water' in [x, y] and 'flour' in [x, y]:
        return 'Naan'

# make a test for make_dough
    # to make dough it will take in "water" and "flour"
        # call the function(give it the controlled arguements} then either says true or false.



# Testing statements:
# ///////////////////////////////////////////////////////////////////////////////////
# print("testing_make_dough with 'water' and 'flour'. Expected --> 'dough'")
# print(make_dough("water", "flour") == "dough")
# print('got:', make_dough('water','flour'))
#
# print("testing_make_dough with 'water' and 'egg'. Expected --> 'not dough'")
# print(make_dough("water", "egg") == "not dough")
# print('got:', make_dough('water','egg'))
#
# # when i pass in cement and water, or anything else .... I should get: not dough
#
# # make test for bake_dough
#     # then with the dough, we should be able to put it in the oven
# print("testing_bake_dough with 'dough'. Expected --> 'Naan'")
# print(bake_dough('dough') == "Naan")
# print('got:', bake_dough('dough'))
#
# print("testing_bake_dough with 'dough'. Expected --> 'Not Naan'")
# print(bake_dough('tissues') == "Not Naan")
# print('got:', bake_dough('tissues'))


# when bake_dough is passed something other that 'dough' it should output: not naan

# bake_dough('Chicken') == 'Not Naan'

# make test for factory_run
# print ("testing_factory_run with 'water' and 'flour'. Expected ----> 'Naan'")
# print(factory_run("water", "flour") == "Naan")
# print("got:", factory_run('water', 'flour'"))

# print ("testing_factory_run with 'ice' and 'flour'. Expected ----> 'Not Naan'")
# print (factory_run('ice','flour') == 'Not Naan'
# print ("got:", factory_run('ice','flour'"))

# print(factory_run('ice','flour') == "Not Naan")
# //////////////////////////////////////////////////////////////////////////////////////////////


# So when prodcuing test, follow a similar syntax to the make_dough and bake_dough functions and print statements used to test it.