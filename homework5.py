immutable_var = 1, 2, True, 'Urban'
print(immutable_var)
# immutable_var [0] = 100 # кортеж относится к неизменяемым типам данных
mutable_list = [1, 3, True, 'Urban']
print(mutable_list)
mutable_list.append(False)
print(mutable_list)
mutable_list.remove(1)
print(mutable_list)
mutable_list [0] = 300
print(mutable_list)
