# 实验报告 - Pandas 数据操作练习

## 一、实验目的
阐述本次实验的主要目的，可参考任务目的部分。
1. 掌握使用Pandas读取和操作数据的基本方法
2. 学习数据清洗和处理缺失值的技巧
3. 熟悉数据统计分析的基本操作
## 二、实验步骤
详细描述你完成每个任务的步骤和方法，可结合代码进行说明。

### 任务 1: 读取数据
说明你使用的读取数据的函数和过程。
使用`pd.read_csv()`函数读取CSV格式的数据文件，指定UTF-8编码确保中文正常显示。

```python
import pandas as pd
data = pd.read_csv('students.csv', encoding='utf-8')
```

### 任务 2: 查看数据基本信息
描述如何查看数据的基本信息。
使用`info()`查看数据结构，`describe()`查看统计信息，`head()`查看前几行数据。

```python
print(data.info())
print(data.describe())
print(data.head())
```
### 任务 3: 处理缺失值
说1. 使用`isnull().sum()`统计各列缺失值数量
2. 对数值列用中位数填充，分类列用众数填充

```python
# 统计缺失值
print(data.isnull().sum())

# 填充缺失值
data['年龄'].fillna(data['年龄'].median(), inplace=True)
data['成绩'].fillna(data['成绩'].median(), inplace=True)
data['城市'].fillna(data['城市'].mode()[0], inplace=True)
```

### 任务 4: 数据统计分析
说明你计算数值列均值、中位数和标准差的方法。
对数值列计算均值、中位数和标准差。

```python
stats = data[['年龄', '成绩']].agg(['mean', 'median', 'std'])
print(stats)
```
### 任务 5: 数据可视化
描述你选择的数值列和绘制直方图的过程。
选择"成绩"列绘制直方图，设置合适的bins数量。

```python
import matplotlib.pyplot as plt
data['成绩'].plot.hist(bins=10, edgecolor='black')
plt.title('成绩分布直方图')
plt.xlabel('成绩')
plt.ylabel('人数')
plt.show()
```
### 任务 6: 数据保存
说明你保存处理后数据的方法。
将处理后的数据保存为新的CSV文件。

```python
data.to_csv('processed_students.csv', index=False, encoding='utf-8')
```
## 三、实验结果
展示每个任务的结果，可使用表格或图表进行呈现。
数据集包含8行4列：
列名：姓名、年龄、成绩、城市
前3行示例：
   姓名    年龄    成绩  城市
0  张三  20.0  85.0  北京
1  李四  21.0  90.0  上海
2  王五  19.0  78.0  广州

### 任务 1: 读取数据
展示读取的数据的基本信息（如列名、行数等）。

### 任务 2: 查看数据基本信息
粘贴数据的基本信息输出。
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 8 entries, 0 to 7
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   姓名      8 non-null     object 
 1   年龄      7 non-null     float64
 2   成绩      7 non-null     float64
 3   城市      7 non-null     object
### 任务 3: 处理缺失值
说明处理后缺失值的情况。
处理前缺失值：
年龄    1
成绩    1
城市    1

处理后缺失值统计：
年龄    0
成绩    0
城市    0
### 任务 4: 数据统计分析
列出数值列的均值、中位数和标准差。
年龄        成绩
mean   20.285714  85.714286
median  20.000000  85.000000
std     0.951190   6.076722


### 任务 5: 数据可视化
![成绩分布直方图](histogram.png)

### 任务 6: 数据保存
处理后的数据已保存为：processed_students.csv
包含8条完整记录，无缺失值。

。

## 四、总结
总结本次实验的收获和体会，分析遇到的问题及解决方法，对 Pandas 数据操作的理解和认识。
   收获与体会
1. 掌握了Pandas数据处理的基本流程
2. 学会了处理缺失值的多种方法
   遇到的问题及解决
1. 中文显示问题：通过指定UTF-8编码解决
2. 缺失值处理选择困难：根据数据特点选择中位数/众数填充
   对Pandas的理解
Pandas提供了强大的数据操作功能，可以高效完成：
- 数据读取和清洗
- 缺失值处理
- 统计分析
