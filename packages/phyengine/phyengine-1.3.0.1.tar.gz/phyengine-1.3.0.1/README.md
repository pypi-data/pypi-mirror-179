# **About**
This library can help you program some simple kinematics processes and get some important (maybe) data from it
# **Getting saterted**
## **Installing**
To install phyengine, run following command in command prompt:

```
pip install phyengine
```

## **Importing**

!!!IMPORTANT!!! You need to use a bit special import to use all features:

```
from phyengine import MathEngine
from phyengine import MainEngine
from phyengine import DynamicObjectManager
```

You can also use ususal import

```
import phyengine
```

but you will have to use phyengine.MathEngine instead of simple MathEngine e.t.c

# **Basic acknowledge**
## **Vectors**
Phyengine can work with 2d vectors. General syntax to create vector object is

```
MathEngine.Vector(<coordx>, <coordy>)
```

For example:

```
first = MathEngine.Vector(2, 3)
```

To get coord of vector, try this:

```
print(first.x)
print(first.y)

# Output:
# 2
# 3
```

Also, you can print vector:

```
print(first)

# Output:
# Vector object with coords (2, 3)
```

### **Operations with vectors**

**Addition/Substracting**

```
a = MathEngine.Vector(2, 3)
b = MathEngine.Vector(3, -7)

res1 = a + b
res2 = a - b
print(res1)
print(res2)

# Output:
# Vector object with coords (5, -4)
# Vector object with coords (-1, 10)
```

**Multiplying/Dividing vector by int/float**

```
a = MathEngine.Vector(5, 6)
b = 1.2
c = 2

res1 = a * b
res2 = a / c
print(res1)
print(res2)

# Output:
# Vector object with coords (6, 7.2)
# Vector object with coords (2.5, 3)
```

**Iterating by vector**

Iterating by vector is equal to iterating by tuple (vector.x, vector.y)

```
a = MathEngine.Vector(5, 6)

for i in a:
    print(i)

# Output:
# 5
# 6
```

**Getting absolute value of vector**

Absolute value of vector is calculated as sqrt(vector.x^2 + vector.y^2)

```
a = MathEngine.Vector(3, 4)

print(abs(a))

# Output:
# 5
```

**Getting unit vector**

Unit vector is a vector, which absolute value is 1 and has the same direction as given

```
a = MathEngine.Vector(3, 4)

e = a.unit
print(e)

# Output:
# Vector object with coords (0.6, 0.8)
```

## **Creating window**

So, let`s create our first window! General syntax to do it is:

```
window = MainEngine.BasicWindow(<width>, <height>, <ping>, <scale>)
```

where:

    width: integer - width of window (pixels)
    height: integer - height of window (pixels)
    ping: integer (30 by default) - time in ms between screen updating. The more ping is, the rarelier screen will be updated but the more stable it will be
    scale: float (1 by default) - number that will show how many pixels are in one meter (scale = 10 mean that every 10 pixels program will understand as 1 imaginary meter)

For example:

```
window = MainEngine.BasicWindow(600, 600, 5, 100)
```

But to show window you need to add next command:

```
window = MainEngine.BasicWindow(600, 600, 5, 100)
window.start()
```

## **Creating objects on screen**
