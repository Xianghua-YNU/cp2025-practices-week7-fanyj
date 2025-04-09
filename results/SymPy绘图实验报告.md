# SymPy 绘图实验报告

## 一、实验信息

- 小组名称：clannad
- 成员：范玉洁
- 实验日期：2025年4月9日

---

## 二、实验目的

- 熟悉SymPy的plot、plot_implicit、和plot3d_parametric_surface函数；
- 掌握曲线、隐函数和参数曲面的绘制方法。

---

## 三、实验内容与方法

分别说明三个问题的具体绘图方法和使用的函数接口。
1. 函数曲线绘制
使用`plot()`函数绘制函数$\cos(\tan(\pi x))$在区间[-1,1]上的图像。设置线型为红色虚线，添加标题和坐标轴标签。

```python
from sympy import symbols, cos, tan, pi, plot

x = symbols('x')
expr = cos(tan(pi*x))
plot(expr, (x, -1, 1), line_color='red', linestyle='--', 
     title=r'$\cos(\tan(\pi x))$曲线', xlabel='x', ylabel='y')
---
2. 隐函数曲线绘制
使用`plot_implicit()`函数绘制隐函数$e^y + \frac{\cos x}{x} + y = 0$的图像。设置绘图区域为x∈[-5,5]，y∈[-5,5]，使用蓝色实线。
```python
from sympy import exp, cos, symbols, Eq
from sympy.plotting import plot_implicit

x, y = symbols('x y')
eq = Eq(exp(y) + cos(x)/x + y, 0)
plot_implicit(eq, (x, -5, 5), (y, -5, 5), line_color='blue',
             title=r'隐函数$e^y + \frac{\cos x}{x} + y = 0$曲线')
```
3. 参数曲面绘制
使用`plot3d_parametric_surface()`函数绘制三维参数曲面。设置u∈[0,2π]，v∈[0,π]，添加标题和坐标轴标签。

```python
from sympy import symbols, cos, sin, pi
from sympy.plotting import plot3d_parametric_surface

u, v = symbols('u v')
plot3d_parametric_surface(
    cos(u)*sin(v), sin(u)*sin(v), cos(v),
    (u, 0, 2*pi), (v, 0, pi),
    title="三维参数曲面", xlabel='x', ylabel='y', zlabel='z')
```

---
## 四、实验结果与分析

### 问题1: 函数曲线 $\cos(\tan(\pi x))$ 绘制结果

*(插入图片或截图并简要分析曲线特点)*

### 问题2: 隐函数曲线 $e^y + \frac{\cos x}{x} + y = 0$ 绘制结果

*(插入图片或截图并简要分析隐函数曲线特点)*

### 问题3: 参数曲面绘制结果

*(插入图片或截图并简要分析三维曲面的特点)*

---

## 五、实验总结与讨论

- 通过本实验你掌握了哪些绘图技巧？
- 掌握的技巧
1. 学会了SymPy基本绘图函数的调用方法
2. 掌握了图形美化和参数设置技巧
3. 理解了参数曲面绘制的数学原理
- 实验中你遇到了哪些问题？如何解决？
- 遇到的问题及解决
1. 隐函数绘图速度慢：通过限制绘图范围和提高采样点数解决
2. 三维曲面显示不完整：调整视角参数解决
3. 数学公式渲染问题：使用LaTeX语法解决
- 你对SymPy的绘图功能有什么建议或意见？
改进建议
1. 增加交互式绘图功能
2. 优化隐函数绘图的算法效率
3. 添加更多自定义样式选项
---

## 六、参考文献

- SymPy官方文档：https://docs.sympy.org/latest/modules/plotting.html
