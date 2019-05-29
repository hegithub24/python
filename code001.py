
# %%
import tushare as ts
import tushare
from selenium import webdriver
dr = webdriver.Chrome()
dr.implicitly_wait(10)
dr.get("https://www.baidu.com")
print(dr.title)
dr.quit()

# %%
df = tushare.realtime_boxoffice()
print(df)


# %%
"""每日票房."""
# df = ts.day_boxoffice() # 获取昨天的数据
df = ts.day_boxoffice('2019-5-1')  # 指定日期
print(df)

# %%
"""实时新闻"""
ts.get_latest_news(2)  # 默认获取最近80条新闻数据，只提供新闻类型、链接和标题
# ts.get_latest_news(top=5,show_content=True) #显示最新5条新闻，并打印出新闻内容

# %%


class TestA():
    def __method(self):
        print("This is a method from class TestA")

    def method(self):
        return self.__method()


class TestB(TestA):
    def __method(self):
        print("This is a method from class TestB")


ca = TestA()
cb = TestB()
ca.method()
cb.method()

# %%


def deco(func):
    def _deco():
        print("before myfunc() called.")
        func()
        print("  after myfunc() called.")
    return _deco


@deco
def myfunc():
    print(" myfunc() called.")
    return "OK"


myfunc()
myfunc()

# %%


class MyClass:
    '''I simple example class'''
    val1 = 'Value 1'
    val4 = 1

    def __init__(self):
        self.val2 = 'Value 2'
        self.__val3 = 'Value 3'

    def func3(self):  # 定义实例方法
        print('val1 : ', self.val1)
        print('val2 : ', self.val2)
        print('instance method cannot access __val3')
        print('val4 : ', self.val4)
        self.val4 = ((self.val4 + 1))

    @classmethod  # 定义类方法
    def func2(cls):
        print('val1 : ', cls.val1)
        print('class method cannot access val2')
        print('class method cannot access __val3')
        print('val4 : ', cls.val4)
        cls.val4 = ((cls.val4 + 1))

    @staticmethod  # 定义静态方法
    def func():
        print('val1 : ', MyClass.val1)
        print('static cannot access val2')
        print('static method cannot access __val3')
        print('val4 : ', MyClass.val4)
        MyClass.val4 = ((MyClass.val4 + 1))

    @property  # 私有实例变量get属性
    def val3(self):
        return self.__val3

    @val3.setter  # 私有实例变量set属性
    def val3(self, value):
        self.__val3 = value

    @val3.deleter  # 私有实例变量del属性
    def val3(self):
        del self.__val3


print('-------------------MyClass.func()------------------')
MyClass.func()


x = MyClass()
print('-------------------x.func()------------------')
x.func()
print('-------------------x.func2()------------------')
x.func2()
print('-------------------x.func3()------------------')
x.func3()

print('')
print('MyClass().val3 : ', MyClass().val3)  # 类调用property
MyClass().val3 = 'New Value'  # 类调用setter
print('after "MyClass().val3 = New Value" val3 :', MyClass().val3)

print('')
print('val3 : ', x.val3)  # 实例调用property
x.val3 = 'New Value'  # 实例调用setter
print('after "x.val3 = New Value" val3 :', x.val3)
del x.val3  # 实例调用deleter
print('after "del x.val3"  val3 : ', x.val3)

#%%
# 导入pylot 模块，并起别名 plt
from matplotlib import pyplot as plt
# 设置 x 轴坐标为[1,2,3], y 轴坐标为[3,2,1]
plt.plot([1,2,3],[3,2,1])
#画图
plt.show()

#%%
from matplotlib import pyplot as plt
height=[161,170,182,175,173,165]
weight=[50,58,80,70,69,55]

#画图
plt.scatter(height,weight,alpha=0.7)
#设置 x 轴标签
plt.xlabel('Height')
#设置 y 轴标签
plt.ylabel('Weight')
# 添加标题
plt.title("sctter demo")
# 图形显示
plt.show()

#%%
