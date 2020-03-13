from sys import argv

if len(argv) != 2:
    print('Wrong Argv num')
    exit(1)
script_name, one = argv  # 将传入的参数赋值进行使用
print(f'the param is {one}')

'''
在terminal 里 python t.py xxxxx  调用
'''
