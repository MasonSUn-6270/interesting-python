class A:
    def a(self):
        return self._var

    def b(self, value: int):
        print(f'我是set')
        self._var = value

    def c(self, ):
        del self._var

    def __name__(self):
        pass

    _ = property(a, b, c)  # 变量名 _ = property : 对A方法的 _ 属性 使用property方法


A()._ = 10
A().x = 10
'我是set'


class A:
    def a(self):
        return self._var

    def b(self, value: int):
        print(f'我是set')
        self._var = value

    def c(self, ):
        del self._var

    def __name__(self):
        pass

    _ = property(a, b, c)
    x = property(a, b, c)


A()._ = 10
A().x = 10
'''
我是set
'''
