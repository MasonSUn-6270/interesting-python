from collections import defaultdict

dd = defaultdict(list)
dd['a'].append('hi')
print(dd)
'''
defaultdict(<class 'list'>, {'a': ['hi']})
'''

dd = defaultdict(str)
dd['a'] += '1'
print(dd)
'''
defaultdict(<class 'str'>, {'a': '1'})
'''

dd = defaultdict(dict)
dd['a']['key'] = 'value'
print(dd)
'''
defaultdict(<class 'dict'>, {'a': {'key': 'value'}})
'''
