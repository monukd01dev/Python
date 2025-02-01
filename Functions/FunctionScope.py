# 2 scopes 
# outside of the function -> global scope 
# inside of function -> local scope 
    # data shadowing happen priorites given to the local variables -> reading cause you cannot modify global variable through function but you can modify mutables like list and dictionary
    # modification to the global variable is not possible only possible if they are mutable like list and dictionary 
        # you required global keyword to modify the global variable and if nested function then nonlocal keyword will allow you to modify variable
        #locals() return all the local variable in which this is called
        #globals() return all the globals variable 

my_global_var = 22
my_global_list = [1,2]

def changeGlobal () :
    my_global_var = 23 #it will do nothing
    my_global_list.append(3)# that will do

changeGlobal()
print(my_global_var,my_global_list)

def iWillChange () : 
    global my_global_var
    my_global_var = 44

iWillChange()
print(my_global_var)

#! Why global is Required for Reassignment?
# Python separates variables into local and global scopes:

# By default, variables assigned inside a function are local to that function.
# To reassign a global variable inside a function, Python needs explicit permission (via global) to avoid accidental overwrites.