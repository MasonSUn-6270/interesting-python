class A():
    nick_name = 'apple'

    @classmethod
    def test(cls):
        return f'[my name is {cls.__name__}\n' \
               f'my object is {cls}\n' \
               f'my nick name is {cls.nick_name}]'

    def __repr__(self):
        return 'i am __repr__'

    def __str__(self):
        return 'i am __str__'


print(A.__name__)
a = A()
print(a.__class__.__name__)
"""
A
A
"""
print(A.test())
"""
[my name is A
my object is <class '__main__.A'>
my nick name is apple]
"""
print(f'{a!r}')
"""
i am __repr__
"""
print(a)
"""
i am __str__
"""
