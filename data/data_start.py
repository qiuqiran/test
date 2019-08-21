# -*- coding:utf-8 -*-
import numpy as np #为了方便使用numpy 采用np简写
import pandas as pd
import matplotlib.pyplot as plt
# 黑体 替换sans-serif字体,解决中文乱码问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']=False # 若不添加，无法在图中显示负号


class len_np():
    '''
    学习Numpy
    '''
    path = 'E:\kew/test\data/train.csv'

    def one(self):
        '''
        Numpy 的创建 array
        :return:
        '''

        a = np.array([2,23,4]) #创建数组
        print(a)

        # b = np.array([2,3,6],dtype=np.int)
        # print(b.dtype)
        # c = np.array([5,6,9],dtype=np.int32)
        # print(c.dtype)
        # d = np.array([5,6,7,8],dtype=np.float)
        # print(d.dtype)
        # f = np.array([7,1,3],dtype=np.float32)
        # print(f.dtype)

        # 创建特定数据
        # a = np.array([[1,2,3],[9,6,8]]) # 2d 矩阵 2行3列
        # print(a)
        #
        # b = np.zeros((3,4))# 数据全为0，3行4列 创建全零数组
        # print(b)
        #
        # c = np.ones((3,4),dtype=np.int)#创建全一数组, 同时也能指定这些特定数据的 dtype， # 数据为1，3行4列
        # print(c)

        # d = np.empty((3,4))#创建全空数组, 其实每个值都是接近于零的数,数据为empty，3行4列
        # print(d)

        # d = np.arange(10,20,2) # 创建连续数组 10-19 的数据，2步长
        # print(d)

        # d = np.arange(12).reshape((3,4)) # 创建连续数组 改变数据的形状 3行4列
        # print(d)

        # d = np.linspace(1,10,20) # 创建线段型数据 开始端1，结束端10，且分割成20个数据，生成线段
        # print(d)


        # d = np.linspace(1,10,20).reshape((5,4)) # 创建线段型数据 开始端1，结束端10，且分割成20个数据，生成线段  # 更改shape 改变数据的形状
        # print(d)

    def two(self):
        '''
        Numpy 基础运算1
        :return:
        '''
        #----------------------一维矩阵-----------------------------------
        # 二者都是1行4列的矩阵
        # a = np.array(([10,20,30,40]))
        # b = np.arange(4)
        # print(a,'\n',b,'\n','二者都是1行4列的矩阵')

        # 两个矩阵之间的减法
        # c = a - b
        # print(c)
        # 两个矩阵之间的加法
        # c = a + b
        # print(c)
        # 两个矩阵之间的乘法
        # c = a * b
        # print(c)
        # 两个矩阵之间的除法
        # c = a / b
        # print(c)
        # 二次方
        # c = a ** 2
        # print(c)
        # sin函数
        # c = 10*np.sin(a)
        # print(c)
        # 逻辑判断
        # print(b == 3)

        #--------------多维矩阵---------------------------------------------
        # a=np.array(([1,1],[0,1]))
        # b=np.arange(4).reshape(2,2)
        # print(a, '\n', b, '\n', '二者都是2行2列的矩阵')
        #
        # # Numpy中的矩阵乘法分为两种， 其一是前文中的对应元素相乘，其二是标准的矩阵乘法运算，即对应行乘对应列得到相应元素：
        # # E:\kew\test\data\dot算法.png 计算方法
        # c=np.dot(a,b)
        # print(c)
        # cc=a.dot(b)
        # print(cc)

        #  sum(), min(), max()的使用
        a=np.random.random((2,4))#随机生成数字生成一个2行4列的矩阵
        print(a)
        # 对应的便是对矩阵中所有元素进行求和，寻找最小值，寻找最大值的操作。
        c=np.sum(a)
        d=np.min(a)
        e=np.max(a)
        print(c,d,e)

        # 如果你需要对行或者列进行查找运算，就需要在上述代码中为 axis 进行赋值。
        # # 0: 对行进行操作; 1: 对列进行操作
        c1 = np.sum(a,axis=1)
        d1 = np.min(a,axis=1)
        e1 = np.max(a,axis=1)
        print(c1, d1, e1)

    def three(self):
        '''
        Numpy 基础运算2
        :return:
        '''
        # a=np.arange(2,14).reshape(3,4)
        # print(a)
        # # 对应着求矩阵中最小元素和最大元素的索引。相应的，在矩阵的12个元素中，
        # # 最小值即2，对应索引0，最大值为13，对应索引为11。
        # print(np.min(a))
        # print(np.argmin(a))
        # print(np.max(a))
        # print(np.argmax(a))
        # # 统计中的均值
        # print(np.mean(a))
        # print(np.average(a))
        # # 求解中位数
        # print(np.median(a))
        # # 累加函数
        # print(np.cumsum(a))
        # # 相应的有累差运算函数
        # print(np.diff(a))
        # # nonzero()函数：
        # print(np.nonzero(a))


        a = np.arange(14,2,-1).reshape((3,4))
        print(a)
        # 排序
        # print(np.sort(a))
        # 矩阵的转置/倒过来
        # print(np.transpose(a))
        # clip(Array,Array_min,Array_max)，用于让函数判断矩阵中元素是否有比最小值小的或者比最大值大的元素，
        # 并将这些指定的元素转换为最小值或者最大值。
        print(np.clip(a,5,8))

    def four(self):
        '''
        Numpy 索引
        :return:
        '''
        a = np.arange(3,15).reshape((3,4))
        # print(a)
        # print(a[2])
        # print(a[2][0:3])
        # for row in a.T:
        #     print(row[0:2])
        # 这一脚本中的flatten是一个展开性质的函数，将多维的矩阵进行展开成1行的数列。
        # 而flat是一个迭代器，本身是一个object属性。
        print(a.flatten())
        for i in a.flat:
            print(i)

    def five(self):
        '''
        Numpy array 合并
        :return:
        '''
        #对于一个array的合并，我们可以想到按行、按列等多种方式进行合并。
        # a=np.array([1,1,1])
        # b=np.array([2,2,2])
        # # 上下合并
        # c=np.vstack(((a, b)))
        # print(c)
        # # 从打印出的结果来看，A仅仅是一个拥有3项元素的数组（数列），而合并后得到的C是一个2行3列的矩阵。
        # print(a.shape,c.shape)

        # 左右合并
        # d=np.hstack((a,b))
        # print(d)

        # 此时我们便将具有3个元素的array转换为了1行3列以及3行1列的矩阵了。
        # print(a[np.newaxis,:])
        # print(a[np.newaxis,:].shape)
        # print(a[:,np.newaxis])
        # print(a[:,np.newaxis].shape)

        # 结合着上面的知识，我们把它综合起来：
        a = np.array([1, 2, 3])[:,np.newaxis]
        b = np.array([4, 5, 6])[:,np.newaxis]
        # print(a)
        # print(b)
        # #
        # c = np.vstack((a,b))
        # # print(c)
        # d = np.hstack((a,b))
        # print(d)
        # print(c,'\n333333333333333',d)
        # print(c.shape,d.shape)
        # 当你的合并操作需要针对多个矩阵或序列时，借助concatenate函数可能会让你使用起来比前述的函数更加方便：
        # axis参数很好的控制了矩阵的纵向或是横向打印，相比较vstack和hstack函数显得更加方便。
        # 0: 对行进行操作; 1: 对列进行操作
        c=np.concatenate((a,b,b,a),axis=0)
        c=np.concatenate((a,b,b,a),axis=1)
        print(c)

    def six(self):
        '''
        Numpy array 分割
        :return:
        '''
        # 创建数据
        a=np.arange(12).reshape((3,4))
        print(a)
        # #纵向分割axis=1 4列
        # print(np.split(a,4,axis=1)) # 4是指分个分割
        # #横向分割axis=0 3列
        # print(np.split(a,3,axis=0)) # 3是指分个分割

        # 不等量分割
        # print(np.array_split(a,3,axis=1))

        # 其他的分割方式
        # print(np.vsplit(a,3))

    def seven(self):
        '''
        Numpy copy & deep copy
        :return:
        '''
        a = np.arange(4)
        print(a)
        # = 的赋值方式会带有关联性
        b=a
        c=a
        d=b
        a[0]=11
        b[0]=12

        # copy() 的赋值方式没有关联性
        f=a.copy()
        a[3]=6

        print(a,b,c,d,f)

class len_pd():
    '''
    学习Pandas
    '''
    path = 'E:\kew/test\data/train.csv'

    def one(self):
        '''

        :return:
        '''

        #Series
        #Series的字符串表现形式为：索引在左边，值在右边。由于我们没有为数据指定索引。
        # 于是会自动创建一个0到N-1（N为长度）的整数型索引。
        # s=pd.Series([1,3,6,np.nan,44,1])
        # print(s)
        # f = pd.Series(np.arange(40))
        # print(f)

        #DataFrame
        # datas=pd.date_range('20160101',periods=7)
        # df=pd.DataFrame(np.random.rand(7,4),index=datas,columns=['a','b','c','d'])
        # print(df)
        #
        # # print(df['b'])
        # #创建一组没有给定行标签和列标签的数据
        # df1 = pd.DataFrame(np.arange(12).reshape((3,4)))
        # print(df1)

        # 还有一种生成 df 的方法
        df2 = pd.DataFrame({'A': 1.2,
                            'B': pd.Timestamp('20130102'),
                            'C': pd.Series(6, index=list(range(4)), dtype='float32'),
                            'D': np.array([9] * 4, dtype='int32'),
                            'E': pd.Categorical(["test1", "train2", "test3", "train4"]),
                            'F': 'foo'})
        # print(df2)
        # #看对列的序号
        # print(df2.index)
        # # 每种数据的名称也能看到
        # print(df2.columns)
        # #只想看所有df2的值
        # print(df2.values)
        #道数据的总结
        print(df2.describe())
        #如果想翻转数据
        print(df2.T)
        #如果想对数据的 index 进行排序并输出:
        print(df2.sort_index(axis=1,ascending=False))
        # 如果是对数据 值 排序输出:
        print(df2.sort_values(by='B'))

    def two(self):
        '''
        Pandas 选择数据
        :return:
        '''
        #我们建立了一个 6X4 的矩阵数据。
        dates=pd.date_range('20190528',periods=6)
        df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['a','b','c','d'])
        print(df)
        # print(df['20190528':'20190530'])


        #根据标签 loc
        # print(df.loc['20190601'])
        # print(df.loc[:,['a','b']])
        # print(df.loc['20190529',['c','d']])

        #根据序列 iloc
        # print(df.iloc[5,0])#5是第几行，0是第几个
        # print(df.iloc[3:5,1:3])#前面是几行3，4行，后面是几列，1，2列

        #根据混合的这两种 ix
        # print(df.ix[:3,['a','c']])

        #通过判断的筛选
        print(df[df.a>19])

    def three(self):
        '''
        Pandas 设置值
        :return:
        '''
        #创建数据
        h = pd.date_range('20190529',periods=4)
        df=pd.DataFrame(np.arange(16).reshape((4,4)),index=h,columns=['ben','kew','wen','bili'])
        print(df)

        #根据位置设置 loc 和 iloc
        #我们可以利用索引或者标签确定需要修改值的位置。
        # df.iloc[2,2]=1111
        # df.loc['20190529','b'] = 2222
        # print(df)

        #根据条件设置
        #如果现在的判断条件是这样, 我们想要更改B中的数, 而更改的位置是取决于 A 的.
        #  对于A大于4的位置. 更改B在相应位置上的数为0.
        # df.ben[df.kew>5] = 90
        # print(df)

        #按行或列设置
        #如果对整列做批处理, 加上一列 ‘F’, 并将 F 列全改为 NaN, 如下:
        df['bili'] = np.nan
        print(df)

        #添加数据
        # 用上面的方法也可以加上 Series 序列（但是长度必须对齐）。
        df['wen0']=pd.Series([1,2,3,4],index=pd.date_range('20190529',periods=4))
        print(df)

    def four(self):
        '''
        Pandas 处理丢失数据
        :return:
        '''

        #创建含 NaN 的矩阵
        #有时候我们导入或处理数据, 会产生一些空的或者是 NaN 数据,
        # 如何删除或者是填补这些 NaN 数据就是我们今天所要提到的内容.

        dates=pd.date_range('20190529',periods=7)
        df=pd.DataFrame(np.arange(28).reshape((7,4)),index=dates,columns=['ben','kew','wen','bili'])
        df.iloc[0,1]=np.nan
        df.iloc[1,2]=np.nan
        print(df)

        # 如果想直接去掉有 NaN 的行或列, 可以使用 dropna
        # f=df.dropna(
        #     axis=1,  # 0: 对行进行操作; 1: 对列进行操作
        #     how='any'  # 'any': 只要存在 NaN 就 drop 掉; 'all': 必须全部是 NaN 才 drop
        # )
        # print(f)
        #如果是将 NaN 的值用其他值代替, 比如代替成 0:
        f=df.fillna(value=99)
        print(f)

        #判断是否有缺失数据 NaN, 为 True 表示缺失数据:
        g=df.isnull()
        print(g)
        #检测在数据中是否存在 NaN, 如果存在就返回 True:
        print(np.any(df.isnull())==True)

    def five(self):
        '''
        Pandas 导入导出
        :return:
        '''
        #读取csv
        data=pd.read_csv(self.path)
        # print(data)
        # print(np.any(data.isnull()==True))
        #将资料存取成pickle
        data.to_pickle('student.pickle')

    def six(self):
        '''
        Pandas 合并 concat
        :return:
        '''
        #axis (合并方向)
        # axis=0是预设值，因此未设定任何参数时，函数默认axis=0。
        # 定义资料集
        # df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
        # df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
        # df3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['a', 'b', 'c', 'd'])
        # # concat纵向合并
        # res=pd.concat([df1,df2,df3],axis=0)
        # # print(res)
        # #ignore_index (重置 index)
        # res=pd.concat([df1,df2,df3],axis=0,ignore_index=True)
        # print(res)

        #join (合并方式)
        # 定义资料集
        # df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
        # df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['b', 'c', 'd', 'e'], index=[2, 3, 4])
        # # print(df1,'\n',df2)
        # #有相同的column上下合并在一起，其他独自的column个自成列，原本没有值的位置皆以NaN填充。
        # # res = pd.concat([df1, df2], axis=0, join='outer',sort=False)
        # # print(res)
        # #只有相同的column合并在一起，其他的会被抛弃。
        # res = pd.concat([df1, df2], axis=0, join='inner', ignore_index=True)
        # print(res)

        #join_axes (依照 axes 合并)
        # 定义资料集
        # df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
        # df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['b', 'c', 'd', 'e'], index=[2, 3, 4])
        #
        # # 依照`df1.index`进行横向合并
        # # res = pd.concat([df1, df2], axis=1, join_axes=[df1.index])
        # res = pd.concat([df1,df2],axis=1,)
        # print(res)


        #append (添加数据) append只有纵向合并，没有横向合并。
        # 定义资料集
        df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
        df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
        df3 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
        s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])

        # 将df2合并到df1的下面，以及重置index，并打印出结果
        # res=pd.concat([df1,df2],axis=0,ignore_index=True)
        # res=df1.append(df2,ignore_index=True)
        # print(res)
        # 合并多个df，将df2与df3合并至df1的下面，以及重置index，并打印出结果
        # res=df1.append([df2,df3],ignore_index=True)
        # print(res)
        # 合并series，将s1合并至df1，以及重置index，并打印出结果
        res=df1.append(s1,ignore_index=True)
        print(res)

    def seven(self):
        '''
        Pandas 合并 merge
        :return:
        '''
        #依据一组key合并
        # 定义资料集并打印出
        # left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
        #                      'A': ['A0', 'A1', 'A2', 'A3'],
        #                      'B': ['B0', 'B1', 'B2', 'B3']})
        # right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
        #                       'C': ['C0', 'C1', 'C2', 'C3'],
        #                       'D': ['D0', 'D1', 'D2', 'D3']})
        # print(left)
        # print(right)
        #
        # # 依据key column合并，并打印出
        # res=pd.merge(left,right,on='key')
        # print(res)
        #
        #依据两组key合并
        #合并时有4种方法how = ['left', 'right', 'outer', 'inner']，预设值how='inner'。
        # 定义资料集并打印出
        # left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
        #                      'key2': ['K0', 'K1', 'K0', 'K1'],
        #                      'A': ['A0', 'A1', 'A2', 'A3'],
        #                      'B': ['B0', 'B1', 'B2', 'B3']})
        # right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
        #                       'key2': ['K0', 'K0', 'K0', 'K0'],
        #                       'C': ['C0', 'C1', 'C2', 'C3'],
        #                       'D': ['D0', 'D1', 'D2', 'D3']})
        #
        # print(left)
        # print(right)
        # # 依据key1与key2 columns进行合并，并打印出四种结果['left', 'right', 'outer'合集, 'inner'交集]
        # res=pd.merge(left,right,on=['key1','key2'],how='right')
        # print(res)

        # Indicator
        #indicator=True会将合并的记录放在新的一列。
        # # 定义资料集并打印出
        # df1 = pd.DataFrame({'col1': [0, 1], 'col_left': ['a', 'b']})
        # df2 = pd.DataFrame({'col1': [1, 2, 2], 'col_right': [2, 2, 2]})
        # print(df1)
        # print(df2)
        #
        # res=pd.merge(df1,df2,on='col1',how='outer',indicator='合并来源')
        # print(res)

        #依据index合并
        # # 定义资料集并打印出
        # left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
        #                      'B': ['B0', 'B1', 'B2']},
        #                     index=['K0', 'K1', 'K2'])
        # right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
        #                       'D': ['D0', 'D2', 'D3']},
        #                      index=['K0', 'K2', 'K3'])
        # print(left)
        # print(right)
        # # 依据左右资料集的index进行合并，how='outer',并打印出
        # res=pd.merge(left,right,left_index=True,right_index=True,how='inner')
        # print(res)

        #解决overlapping的问题
        # 定义资料集
        boys = pd.DataFrame({'三班': ['ben', 'li', 'Ku'], 'age': [1, 2, 3]})
        girls = pd.DataFrame({'三班': ['ben', 'wen', 'zhang'], 'age': [4, 5, 6]})
        print(boys)
        print(girls)

        # 使用suffixes解决overlapping的问题
        res = pd.merge(boys, girls, on='三班', suffixes=['_boy', '_girl'], how='inner')
        print(res)

    def eight(self):
        '''
        Pandas plot 出图
        :return:
        '''

        #Pandas plot 出图
        #这次我们讲如何将数据可视化. 首先import我们需要用到的模块，
        # 除了 pandas，我们也需要使用 numpy 生成一些数据，
        # 这节里使用的 matplotlib 仅仅是用来 show 图片的, 即 plt.show()。

        #今天我们主要是学习如何 plot data
        #创建一个Series
        # 随机生成1000个数据
        # data = pd.Series(np.random.randn(1000),index=np.arange(1000))
        # # print(data)
        # # 为了方便观看效果, 我们累加这个数据
        # s = data.cumsum()
        # # s = np.cumsum(data)
        # # pandas 数据可以直接观看其可视化形式
        # #熟悉 matplotlib 的朋友知道如果需要plot一个数据，我们可以使用 plt.plot(x=, y=)，
        # # 把x,y的数据作为参数存进去，但是data本来就是一个数据，所以我们可以直接plot。
        # s.plot()
        # plt.show()

        #Dataframe 可视化
        data = pd.DataFrame(
            np.random.randn(1000,4),
            index=np.arange(1000),
            columns=['a','b','c','d']
        )
        # print(data)
        s = data.cumsum()
        # s.plot()
        # plt.show()
        # 因为有4组数据，所以4组数据会分别plot出来。plot
        # 可以指定很多参数，具体的用法大家可以自己查一下
        #http://pandas.pydata.org/pandas-docs/version/0.18.1/visualization.html

        #除了plot，我经常会用到还有scatter，这个会显示散点图，
        # 首先给大家说一下在 pandas 中有多少种方法bar，hist，box，kde，area，scatter，hexbin
        #但是我们今天不会一一介绍，主要说一下 plot 和 scatter. 因为scatter只有x，y两个属性，我们我们就可以分别给x, y指定数据
        # ax = data.plot.scatter(x='a',y='b',cl)
        ax = s.plot.scatter(x='a', y='b', color='DarkBlue', label='Class1')
        s.plot.scatter(x='a', y='c', color='LightGreen', label='Class2', ax=ax)
        plt.show()
        #这就是我们今天讲的两种呈现方式，一种是线性的方式，一种是散点图。

class train():
    '''
    https://mp.weixin.qq.com/s/LTDgIkcGogk3Iuh8VfA-8g
    用 Python 实现机器学习的教程
    泰坦尼克：从灾难中进行机器学习（https://www.kaggle.com/c/titanic）

    这就是众所周知的泰坦尼克号。这是一场发生在 1912 年的灾难，
    这场灾难波及到的乘客和机组成员共 2224 人，其中 1502 人遇难死亡。
    这项 Kaggle 竞赛（或者说是教程）提供了灾难中的真实数据。
    你的任务是解释这些数据，并预测出灾难中哪些人会活下来，哪些人不会。
    '''
    def read_csv(self):
        '''
        载入数据
        :return:
        '''
        path = 'E:\kew/test\data/train.csv'
        train_df = pd.read_csv(path)
        return train_df

    def miss_data(self):
        '''
        查看缺少的数据汇总
        :return:
        '''
        train_df = self.read_csv()

        # 查看缺少数据
        # print(train_df.isnull())
        # print(np.any(train_df.isnull())==True)
        # total = train_df.isnull().sum().short_values(ascending=False)

        #判断缺失数据为false，统计数量，排序
        total = train_df.isnull().sum().sort_values(ascending=False)
        #百分比单个缺失率/缺失率总数
        percent = (train_df.isnull().sum()/train_df.isnull().count()*100).sort_values(ascending=False)
        #合并数据，生成新的 key
        ms = pd.concat([total,percent],axis=1,keys=['total','percent'])
        #过滤不需要的数据
        ms = ms[ms['percent']>0]

        #用饼图展示缺少数据的占比
        ms['total'].plot.pie(subplots=True,figsize=(6, 6))
        plt.title('缺失数据统计')
        # plt.show()
        return ms

    def clean_data(self):
        '''
        有大量的缺失。我们需要对它们进行处理，也就是所谓的数据清理（Data Cleaning）。
        我们 90% 的时间都花在这上面。我们要针对每一个机器学习项目进行大量的数据清理。
        当数据清理干净时，我们就可以轻松地进行下一步了，什么都不用担心。
        数据清理中最常用的技术是填充缺失数据。你可以用众数、平均数或中位数来填充缺失数据。
        但是根据经验来讲，分类数据只能用众数，连续数据可以用中位数或平均数。
        所以我们用众数来填充登船地数据，用中位数来填充年龄数据。
        :return:
        '''
        train_df = self.read_csv()
        # print(train_df)
        # print(ms)

        # ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
        #  'Parch', 'Ticket', 'Fare', 'Embarked']
        # Cabin 舱号，NaN 表示未知
        # 中位数 Age 年龄
        # 众数 Embarked 登船的起始地，S 表示南安普顿（Southampton），Q 表示皇后镇（Queenstown），C 表示瑟堡（Cherbourg）
        # 要改变源数据的话需要添加参数inplace = True
        # mode()是众数，0获取列众数，1获取行众数
        # median()是中位数
        train_df['Embarked'].fillna(train_df['Embarked'].mode()[0],inplace=True)
        train_df['Age'].fillna(train_df['Age'].median(),inplace=True)
        # 删除大量缺少的数据
        train_df.drop(['Cabin'],axis=1,inplace=True)
        # print(train_df.isnull().sum())
        return train_df

    def ft_data(self):
        '''
        特征工程
        我们以登船地数据为例——这是用 Q、S 或 C 填充的数据。Python 库不能处理这个，
        因为它只能处理数字。所以你需要用所谓的独热向量化（One Hot Vectorization）来处理，
        它可以把一列变成三列。用 0 或 1 填充 Embarked_Q、Embarked_S 和 Embarked_C，
        来表示这个人是不是从这个港口出发的。
        :return:
        '''
        train_df = self.clean_data()
        #891行，11列
        # print(train_df)


        Embarked_Q = pd.DataFrame(np.zeros(891), columns=['Embarked_Q'])
        Embarked_S = pd.DataFrame(np.zeros(891), columns=['Embarked_S'])
        Embarked_C = pd.DataFrame(np.zeros(891), columns=['Embarked_C'])
        res = pd.concat([train_df,Embarked_Q,Embarked_S,Embarked_C],axis=1,join_axes=[train_df.index])
        #
        # res.Embarked_Q[res.Embarked=='Q'] = 1
        res.loc[res['Embarked'=='Q','Embarked_Q']]=1
        # # res.Embarked_S[res.Embarked=='S'] = 1
        # # res.Embarked_C[res.Embarked=='C'] = 1
        # # print(res.shape)
        # print(train_df.info())




        # for i in range(res.shape[0]):
        #     print(i,res[i])

















train().ft_data()