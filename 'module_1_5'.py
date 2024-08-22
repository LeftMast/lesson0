from lib2to3.fixes.fix_tuple_params import tuple_name

immutable_var = 1,2,3, True, 'a','b', 'Urban'
list_ = [1,2,3, True, 'a','b',]
print(immutable_var.__sizeof__())
print(list_.__sizeof__())
immutable_var_2 = (1,2,3,4)
immutable_var_3 = tuple([1,2,3,4])
print(immutable_var)
print(immutable_var_2)
print(immutable_var_3)
print(type(immutable_var))
print(immutable_var [0])
immutable_var [0] = 200

