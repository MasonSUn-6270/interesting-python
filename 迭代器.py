def foo():
    for i in range(6):
        yield i


print(foo().__next__())
'0'
print(foo().__iter__())
'<generator object haha at 0x038E00B0>'


class RepeaterAolige:
    def __init__(self):
        self.roam = '奥利给！'

    def __iter__(self):
        return self

    def __next__(self):
        return self.roam



a = RepeaterAolige()
# for i in a: print(i)     ### 无限循环 ，请勿尝试
"""
奥利给！
奥利给！
奥利给！
奥利给！
奥利给！
奥利给！
奥利给！
奥利给！
奥利给！
......
"""

class RepeaterAoligePlus:
    def __init__(self):
        self.roam = '奥利给！'
        self.count = 1
    def __iter__(self):
        return self

    def __next__(self):
        if self.count < 10:
            self.count += 1
            self.roam += '!'
            return self.roam
        else:
            raise StopIteration
a=RepeaterAoligePlus()
for i in a:print(i)
'''
奥利给！!
奥利给！!!
奥利给！!!!
奥利给！!!!!
奥利给！!!!!!
奥利给！!!!!!!
奥利给！!!!!!!!
奥利给！!!!!!!!!
奥利给！!!!!!!!!!
'''