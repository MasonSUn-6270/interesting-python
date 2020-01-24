"""
先示范一下，不带open打开文件的情况

"""


class A:
    def __init__(self, num: int):
        try:
            self.num = int(num)
            self.word = '.' * (self.num)
        except TypeError:
            print("请重新定义--num")

    def __enter__(self):
        self.word += '....'
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.word = self.word[:-4]

    def show(self, text: str):
        print(f'{self.word}{text}')


with A(6) as f:
    f.show('hi~')
    with f:
        f.show('hi,again')
        with f:
            f.show('hi, my friend')
        f.show('hi,4')
f.show('?')

'''
..........hi~
..............hi,again
..................hi, my friend
..............hi,4
......?
'''

"""
带open打开文件的情况，其实也很简单，只是多了open(,)语句

"""


class OpenFile:
    def __init__(self):
        self.filename = './示范环境/sample.txt'

    def __enter__(self):
        return open(self.filename, 'r')

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


with OpenFile() as f:
    print(f.read())
'hello world'
