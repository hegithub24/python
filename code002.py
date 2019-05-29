"""Matplotlib模块的练习。
Matplotlib是一个主要用于绘制二维图形的Python库。
Matplolib最初主要模仿Matlab的画图命令，又独立于Matlab。
"""

#%%
"""使用Matplotligb画一个简单直线图"""
# 导入pylot 模块，并起别名 plt
from matplotlib import pyplot as plt
# 设置 x 轴坐标为[1,2,3], y 轴坐标为[3,2,1]
plt.plot([1,2,3],[3,2,1])
#画图
plt.show()

#%%
"""绘制身高-体重的散点图"""
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
"""无相关性的散点图."""
import numpy as np
import matplotlib.pyplot as plt

#设置随机数种子
np.random.seed(10)
#使用Numpy的随机函数，产生X轴和Y轴的数据，具有相同长度的数据
N= 100
x = np.random.randn(N)
y=np.random.randn(N)
#画图
plt.scatter(x,y)
# 图形显示
plt.show()

#%%
"""显示 y = 2 x +1 的图形."""
import matplotlib.pyplot as plt
import numpy as np

# 生成等区间的Numpy数组ndarray，从-1到1分成50份。
x = np.linspace( -1 , 1, 50  )
#线程方程为y = 2x + 1
y = 2 * x + 1

# 设置X轴标签
plt.xlabel('X')
# 设置Y轴标签
plt.ylabel('Y ')
# 画图
plt.plot(x,y)
# 图形显示
plt.show()

#%%
"""曲线图."""
import matplotlib.pyplot as plt
import numpy as np

# 设置X轴标签
plt.xlabel('X')
# 设置Y轴标签
plt.ylabel('Y ')

# 取5个点可以看到折线的效果
#x = np.linspace( -1 , 1, 5 )
x = np.linspace( -1 , 1, 50  )

# 线程方程为y = x ** 2 
y = x**2

# 画图
plt.plot (x,y)
# 图形显示
plt.show()

#%%
"""柱状图."""
import numpy as np
from matplotlib import pyplot as plt

# 柱的个数，生成一个数组，从0到4
index = np.arange(5)
#柱的高度
y=[20,10,30,25,15]

#  画图，生成5个高度为y，柱的宽度为0.5，颜色是红色的柱体
p1 = plt.bar(x=index, height=y , width=0.5 , color='r' )
# 添加图的标题
plt.title("bar demo")
plt.show()

#%%
"""水平柱状图。"""
import numpy as np
import matplotlib.pyplot as plt

N = 5
# 柱的高度
y=[20,10,30,25,15]
# 柱的个数
index = np.arange(N)

#  画图，生成5个高度为y，方向是水平的，柱的宽度为0.8，颜色是蓝色的柱体
p2 = plt.bar(x=0,bottom=index, width=y,height=0.8,orientation ='horizontal' )
# 添加图的标题
plt.title("bar demo")
plt.show()

#%%
from wxpy import *
bot = Bot()
bot.file_helper.send("Hello World!")
print("ending")