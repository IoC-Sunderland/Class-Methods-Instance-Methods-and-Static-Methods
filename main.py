class MyClass:
    def instance_method(self):
        return 'Instance method called', self

    @classmethod
    def class_method(cls):
        return 'class method called', cls

    @staticmethod
    def static_method():
        return 'static method called'

a = MyClass()

print(a.instance_method())
print(a.class_method()) # Only has access to the class itself NOT the object instance

print(a.static_method())
print('\n')

print(MyClass.static_method())
print(MyClass.class_method())
#print(MyClass.instance_method())
