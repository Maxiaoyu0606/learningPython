"""
    数字类型 Number
"""

""" (1) 整数 int """
i = 10
print(isinstance(i,int))
# true

""" (2) 布尔 bool """
a = 10
b = 20
print(a>b)
# false

""" (3) 浮点数 """
f = 1.11112
print(isinstance(f, float))
# true

""" (4) 复数 complex """
print(isinstance(f, complex))
# false

c = 1.1 + 2.21j
print(isinstance(c, complex))
# true

"""
    字符串 String (单引号双引号使用相同)
    （1）使用三个单引号或三个双引号是一个多行字符串；
    （2）换行 '\' ；使用r可以让反斜杠不发生转义。如 r 'this is a \n line';
    （3）按照字面意义级联字符串，如"this" "is" "string" 会被自动准换为 this is string；
    （4）字符串可以用 + 运算符连接在一起，用 * 运算符重复；
    （5）python 中字符串有两种索引方式，从左往右以 0 开始；从右往左从 -1 开始；
    （6）python 中的字符串不能改变；
    （7）python 没有单独的字符类型，一个字符就是长度为1的字符串；
    （8）字符串的截取的语法格式：变量[头下标：尾下标：步长]
        例如： 
            str = 'maxiaoyu'
            str[0:-1] ---> 第一个到倒数第二个的所有字符
            str[2:5] ---> 第一个到第五个字符
            str * 2 ---> 输出两次字符串
            str + '你好' ---> 连接字符串
"""

# 字符串 + 运算符 和 * 运算符
print("this" + "is" + "string")
print("this" * 8 )

# python 索引
g = [1, 2, 3, 4, 5, 6, ]
print(g[-2])
# python 字符串长度
print(len(g))

# 换行
print('hello \nxiaoyu' )

# 换行运算
print( 1 +  \
      2)

print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')


# 按回车键后就会等待用户输入
input("\n\n按下 enter 键后退出。")
# "\n\n"在结果输出前会输出两个新的空行。一旦用户按下 enter 键时，程序将退出。

"""
      同一条显示多条语句： 以 ; 分隔
"""

"""
      多个语句构成代码组：
            if、 while、 def 和 class 这样的复合语句，首行以关键字开始，以冒号结束，该行之后的一行或多行代码构成代码组
            我们将首行及构面的代码组成为一个子句（clause）
"""

"""
      print 输出，默认输出是换行的，如果要实现不换行需要在变量的末尾加上end="":
"""
# 默认换行
x = 10; y = 20
print(x)
print(y)

# 不换行
print(x, end=" ")
print(y, end=" ")


"""
      import 与 from...import
在 python 中用 import 或者 from...import 来导入相应的模块；

- 将整个模块（somemodule）导入，格式为： 
      import somemodule
- 从某个模块中导入某个函数，格式为： 
      from somemodule import somefunction
- 从某个模块中导入多个函数，格式为：
      from somemodule import firstfunction, secondfunction, thirdfunction
- 将某个模块中的全部函数导入，格式为： 
      from somemodule import *
"""

"""
      命令行参数
打开命令行工具
- 查看 python 各参数帮助信息
      python -h
"""
