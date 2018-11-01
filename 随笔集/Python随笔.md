```Python
类中的__init__(self)函数
主要是用来给实例化的对象绑定一些属性。
self表示的是实例化的对象本身。
```

封装数据

```Python
class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def show_data(self):
        print(self.name,self.age)
  
zs = Student("zs",12)
zs.show_data()

实例变量可以通过调用类中的方法来，直接操作对象内部的数据，无需知道方法内部的实现细节。
```

访问限制，将变量私有化 __name 是一个私有的变量

```Python
私有化的好处是防止乱改数据。
如果要修改数据，通过调用方法来修改数据，可以创建一个函数def set_data(self,name):
    self.__name = name
外部通过调用该函数进行修改，好处是可以在加上条件，使得修改是可以控制的。
```

继承

```Python
继承的好处，子类可以直接拥有父类的属性和方法。
子类还可以（重写，增加）通过父类继承的属性和方法。

```

多态

```Python
def run_twice(animal):
    animal.run()
    
只要类中含有run方法，run_twice函数就可以执行。python是一种动态数据类型。
还有一种理解是：animal作为父类，拥有run方法，那么他的子类会继承父类中的run方法，所以run_twice函数传入的参数是来自animal的子类，那就可以调用run方法。所以animal的子类可以无限的增加，而不用修改run_twice函数中的代码。
Python中的多态体现的不是很强烈，如果Car类中也有run方法，run_twice函数也可以使用，run_twicw函数本来是写给animal类的，但是Car类也能使用。静态语言和动态语言的区别。
```

slots方法限制属性的添加

```python
__slots__  限制实例的属性
只对当前类有用，对该类的子类没有用。
```





