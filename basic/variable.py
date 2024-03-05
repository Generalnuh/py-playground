x, y, z = "nuh", "generalnuh", "generalnoeh"
print(x, y, z)

x = y = z = "bento"
print(x)
print(y)
print(z)

buah = ['nanas', 'pisang', 'jambu']
x , y, z = buah
print(x, y, z)

# Global Variable
x = 'Awesome'

def sapaan():
    print('Python sungguh, ' + x)

sapaan()

print('Python sungguh, ' + x)

# Menggunakan keyword global

def awesome():
    global y
    y = 'fantastis'

awesome()
print('Python is ' + y)

# Mengubah value variable global
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)