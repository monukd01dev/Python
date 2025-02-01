d = {'key':'value'}
print(d)

d = dict([('one',1),('two',2),('three',3),('four',4)]) #basically providing dict_items
print(d)

lKeys = ['five','six','seven','eight']
e = dict.fromkeys(lKeys)
print(e)

e = dict.fromkeys(lKeys,'shiv')
print(e)

e['inifinity'] = 'shiv'

print(e)

print(d.update(e))
print(d)
two = 'two'
del d[two]
print(d)
# del d
# print(d)

print(d.popitem())
print(d.pop('one'))# value

print(e.clear(),e)
print(d.clear(),d)