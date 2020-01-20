import functools

"能将被装饰丢失的元数据弄回来，装饰到闭包中"


class Kongjian():
    @staticmethod
    def upper_sugar(func):
        """
        俺是一个装饰器，我使用闭包会定义一个函数，并返回这个函数对象本身
        :param func: 初始函数对象
        :return: 处理后的函数对象
        """

        @functools.wraps(func)
        def temp():
            return func().upper()

        return temp

    @staticmethod
    def upper_sugar_lambada_version(func):
        pass


class Easy(object):

    @staticmethod
    @Kongjian.upper_sugar
    def example():
        return 'adassda'


print(Easy.example())
'ADASSDA'
print(Easy.example.__name__)
'example'
print(str.__name__)
'str'
