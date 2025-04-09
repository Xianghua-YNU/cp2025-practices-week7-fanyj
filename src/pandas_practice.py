import pandas as pd
import matplotlib.pyplot as plt

def creat_frame():
    """
    创建一个包含学生信息的DataFrame并保存为CSV文件。
    
    该函数创建一个包含学生姓名、年龄、成绩和所在城市的数据框架，
    并将其保存为UTF-8编码的CSV文件。
    
    Returns:
        None
    """
    # 学生需要在此处实现代码
    data = {
    '姓名': ['张三', '李四', '王五', '赵六', '陈七'],
    '年龄': [25, 30, None, 22, 28],
    '成绩': [85.5, 90.0, 78.5, 88.0, 92.0],
    '城市': ['北京', '上海', '广州', '深圳', '上海']
    }
    df = pd.DataFrame(data)
    df.to_csv('students.csv', index=False, encoding='utf-8')
    print("学生数据已保存为students.csv")

def load_data():
    """任务1: 读取数据文件"""
    # 学生需要在此处实现代码
    try:
        df = pd.read_csv('students.csv', encoding='utf-8')
        print("数据加载成功")
        return df
    except FileNotFoundError:
        print("文件未找到，请先运行creat_frame()创建数据文件")
        return None

def show_basic_info(data):
    """任务2: 显示数据基本信息"""
    # 学生需要在此处实现代码
    if data is not None:
        print("\n=== 数据基本信息 ===")
        print(f"数据形状: {data.shape}")
        print("\n前5行数据:")
        print(data.head())
        print("\n数据信息:")
        print(data.info())
        print("\n各列统计信息:")
        print(data.describe(include='all'))

def handle_missing_values(data):
    """任务3: 处理缺失值"""
    # 学生需要在此处实现代码
    if data is not None:
        print("\n=== 处理缺失值前 ===")
        print("缺失值统计:")
        print(data.isnull().sum())
        
        # 填充缺失值
        data['年龄'].fillna(data['年龄'].median(), inplace=True)
        data['成绩'].fillna(data['成绩'].mean(), inplace=True)
        data['城市'].fillna('未知', inplace=True)
        
        print("\n=== 处理缺失值后 ===")
        print("缺失值统计:")
        print(data.isnull().sum())
        return data
    return None

def analyze_statistics(data):
    """任务4: 统计分析数值列"""
    # 学生需要在此处实现代码
    if data is not None:
        print("\n=== 统计分析 ===")
        print("\n年龄统计:")
        print(data['年龄'].describe())
        print("\n成绩统计:")
        print(data['成绩'].describe())
        
        print("\n各城市平均成绩:")
        print(data.groupby('城市')['成绩'].mean())
        
        print("\n年龄与成绩的相关性:")
        print(data[['年龄', '成绩']].corr())

def visualize_data(data, column_name='成绩'):
    """任务6: 数据可视化"""
    # 学生需要在此处实现代码
    if data is not None:
        plt.figure(figsize=(15, 10))
        
        # 成绩分布直方图
        plt.subplot(2, 2, 1)
        data[column_name].plot(kind='hist', bins=10, edgecolor='black')
        plt.title('成绩分布直方图')
        plt.xlabel('成绩')
        plt.ylabel('人数')
        
        # 各城市平均成绩柱状图
        plt.subplot(2, 2, 2)
        data.groupby('城市')[column_name].mean().plot(kind='bar')
        plt.title('各城市平均成绩')
        plt.xlabel('城市')
        plt.ylabel('平均成绩')
        
        # 年龄与成绩散点图
        plt.subplot(2, 2, 3)
        plt.scatter(data['年龄'], data[column_name])
        plt.title('年龄与成绩关系')
        plt.xlabel('年龄')
        plt.ylabel('成绩')
        
        # 箱线图
        plt.subplot(2, 2, 4)
        data.boxplot(column=column_name, by='城市')
        plt.title('各城市成绩箱线图')
        plt.suptitle('')
        plt.xlabel('城市')
        plt.ylabel('成绩')
        
        plt.tight_layout()
        plt.show()

def save_processed_data(data):
    """任务7: 保存处理后的数据"""
    # 学生需要在此处实现代码
    if data is not None:
        data.to_csv('processed_students.csv', index=False, encoding='utf-8')
        print("\n处理后的数据已保存为processed_students.csv")

def main():
    """主函数，执行所有数据处理流程"""
    # 学生需要在此处组织代码流程
    # 创建数据文件(如果不存在)
    creat_frame()
    
    # 加载数据
    data = load_data()
    
    if data is not None:
        # 显示基本信息
        show_basic_info(data)
        
        # 处理缺失值
        data = handle_missing_values(data)
        
        # 统计分析
        analyze_statistics(data)
        
        # 数据可视化
        visualize_data(data)
        
        # 保存处理后的数据
        save_processed_data(data)

if __name__ == "__main__":
    main()
