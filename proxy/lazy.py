# -*-coding:utf-8-*-
'''
Created on 2017年7月24日

@author: houguangdong
'''


class LazyProperty:
    def __init__(self, method):
        self.method = method
        self.method_name = method.__name__
        print 'function overriden: {}'.format(self.method)
        print "function's name: {}".format(self.method_name)
    
    def __get__(self, obj, cls):
        if not obj:
            return None
        value = self.method(obj)
        print 'value {}'.format(value)
        setattr(obj, self.method_name, value)
        return value
    

class Test:
    def __init__(self):
        self.x = 'foo'
        self.y = 'bar'
        self._resource = None

    @LazyProperty
    def resource(self):
        print 'initializing self._resource which is: {}'.format(self._resource)
        print '1111'
        self._resource = tuple(range(5))  # 假设这一行的计算成本比较大
        return self._resource


def main():
    t = Test()
    print t.x
    print t.y
    # 做更多的事情...
    print t._resource
    print t._resource
    

class SensitiveInfo:
    def __init__(self):
        self.users = ['nick', 'tom', 'ben', 'mike']
    
    def read(self):
        print 'There are {} users: {}'.format(len(self.users), ''.join(self.users))

    def add(self, user):
        self.users.append(user)
        print 'Added user {}'.format(user)
    

class Info:
    '''SensitiveInfo的保护代理'''
    def __init__(self):
        self.protected = SensitiveInfo()
        self.secret = '123456'
    
    def read(self):
        self.protected.read()
    
    def add(self, user):
        sec = raw_input("what is the secret?")
        if sec == '123456': 
            self.protected.add(user) 
        else:
            print "That's wrong!"
        
def main1():
    info = Info()
    while True:
        print '1. read list |==| 2. add user |==| 3. quit'
        key = str(input('choose option: '))
        if key == '1':
            info.read()
        elif key == '2':
            name = input('choose username: ')
            info.add(name)
        elif key == '3':
            exit()
        else:
            print 'unknown option: {}'.format(key)
        

if __name__ == '__main__':
    main()
    main1()