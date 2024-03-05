from copy import deepcopy

x = dict(username = "admin", machines = ['foo', 'bar', 'baz'])
y = deepcopy(x)
y['username'] = 'mlh'
y['machines'].remove('bar') 
print(x)
print(y)

