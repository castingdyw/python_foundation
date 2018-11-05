class Dog(object):
    def work(self):
        pass


class Dog1(Dog):
    def work(self):
        print('dog1工作')


class Dog2(Dog):
    def work(self):
        print('dog2工作')


class Person(object):
    def work_dog(self, dog):
        print('人开始让:', end = '')
        dog.work()

p = Person()
dog1 = Dog1()
dog2 = Dog2()
dog1.work()

p.work_dog(dog1)
