# 数据容器
Python中的数据容器:
一种可以容纳多份数据的数据类型，容纳的每一份数据称之为1个元素
每一个元素，可以是任意类型的数据，如字符串、数字、布尔等。
数据容器根据特点的不同，如:
是否支持重复元素
是否可以修改
是否有序，等
分为5类，分别是:
列表(list) 、元组(tuple) 、字符串(str) 、集合(set)、字典(dict)

## 定义
一种可以存储多个元素的Python数据类型

1.列表的定义语法
[元素1,元素2,元素3, .... .
2.什么是元素?
数据容器内的每一份数据，都称之为元素
3.元素的类型有限制吗?
元素的数据类型没有任何限制，甚至元素    也可以是列表,这样就定义了
嵌套列表

## 方法
class Studend:
    def add(self, x, y):    
        return x + y


## 序列
内容连续、有序、支持下标索引的一类数据容器
2. 哪些数据容器可以视为序列？
列表、元组、字符串
3. 序列如何做切片
序列[begin:end:step]

## 集合
我们目前接触到了列表、元组、字符串三个数据容器了。基本满足大多数的使用场景。
为何又需要学习新的集合类型呢?
通过特性来分析:
列表可修改、支持重复元素且有序
元组、字符串不可修改、支持重复元素且有序

和列表、元组、字符串等定义基本相同:
列表使用:[]
元组使用: ()
字符串使用:""
集合使用:{} 

首先，因为集合是无序的，所以集合不支持冲下标索引访问
但是集合和列表一样，是允许修改的，所以我们来看看集合的修改方法。

取出2个集合的差集
语法:集合1 .difference(集合2),功能:取出集合1和集合2的差集(集合1有而集合2没有的)
结果:得到一个新集合，集合1和集合2不变
set1 = {1,2, 3}
set2={1，5，6}
set3 = set1 difference(set2)
print(set3)
得到的新集合
print(set1)
#结果:{1，2，3}不变
print(set2)
#结果:{1, 5，6}不变

消除2个集合的差集
语法:集合1.difference_ _update(集合2)
功能:对比集合1和集合2，在集合1内，删除和集合2相同的元素。
结果:集合1被修改，集合2不变

set1 = {1, 2，3}

set2 = {1， 5，6}

set1. difference_ _update (set2)
 print(set1)
#结果:{2, 3}
 print(set2)
#结果:{1，5，6}

集合的特点
经过.上述对集合的学习，可以总结出集合有如下特点:
●可以容纳多个数据
●
可以容纳不同类型的数据(混装)
●
数据是无序存储的(不支持下标索引)
●
不允许重复数据存在
●
可以修改(增加或删除元素等)
●
支持for循环

## 字典dict
字典的定义，同样使用{}，不过存储的元素是一一个个的:键值对，如下语法:
1#定义字典字面量
2 {key: valuekey
value， ..
key: value}]
3 #定义字典变量
‘4 my_ dict = {key: value, key: value， ....... key: value}
5#定义空字典
6| my_ _dict = {}
#空字典定义方式1
7 my_ _dict = dict()
#空字典定义方式2

# 总结
```
数据容器可以从以下视角进行简单的分类:
是否支持下标索引
支持:
列表、元组、字符串一序列类型
不支持:集合、字典-非序列类型
是否支持重复元素:
支持:列表、元组、字符串-序列类型,
不支持:集合、字典一非序列类型
是否可以修改
支持:列表、集合、字典
不支持:元组、字符串
```

1.基于各类数据容器的特点，它们的应用场景如下:
●
列表:一批数据，
可修改、可重复的存储场景
●
元组:一批数据，不可修改、可重复的存储场景
●
字符串:一串字符串的存储场景
●
集合:一批数据，去重存储场景
●
字典:一批数据，可用Key检索Value的存储场景

数据容器的通用操作-遍历
数据容器尽管各自有各自的特点，但是它们也有通用的一些操作。
首先，在遍历上:
5类数据容器都支持for循环遍历
列表、元组、字符串支持while循环，集合、字典不支持(无法下标索引)
尽管遍历的形式各有不同，但是，它们都支持遍历操作。

容器的通用转换功能
除了下标索引这个共性外，还可以通用类型转换
list(容器)
str(容器)
将给定容器转换为列表
将给定容器转换为字符串
tuple(容器)
set(容器)
将给定容器转换为元组
将给定容器转换为集合

ASCI码表
在程序中，字符串所用的所有字符如:
●
大小写英文单词
●
数字
●
特殊符号(!、\、|、@、#、空格等)
都有其对应的ASCII码表值
每一个字符都能对应上- -个:数字的码值
字符串进行比较就是基于数字的码值大小进行比较的。


