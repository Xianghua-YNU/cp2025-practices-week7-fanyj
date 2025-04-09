import numpy as np
import scipy.ndimage as sim
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def load_stress_fibers():
    """
    加载应力纤维数据
    
    返回:
        numpy.ndarray: 包含应力纤维数据的二维数组
        
    注意:
        数据文件应位于data/stressFibers.txt
        使用np.loadtxt加载文本格式的数据
    """
    # 学生需要实现：使用np.loadtxt加载数据文件
    # Load the data from the specified file
    return np.loadtxt('data/stressFibers.txt')

def create_gauss_filter():
    """
    创建高斯滤波器
    
    返回:
        numpy.ndarray: 51x51的高斯滤波器矩阵
        
    说明:
        滤波器尺寸为51x51(-25到25)
        X方向标准差σ_x=√5, Y方向标准差σ_y=√45
        公式: exp(-0.5*(X²/5 + Y²/45))
    """
    # 学生需要实现：
    # 1. 使用np.arange和np.meshgrid创建坐标网格
    # 2. 根据公式计算高斯函数值
    # Create coordinate ranges
    x = np.arange(-25, 26)
    y = np.arange(-25, 26)
    
    # Create meshgrid
    X, Y = np.meshgrid(x, y)
    
    # Calculate Gaussian function
    sigma_x_sq = 5  # σ_x² = 5
    sigma_y_sq = 45  # σ_y² = 45
    gauss = np.exp(-0.5 * (X**2 / sigma_x_sq + Y**2 / sigma_y_sq))
    
    return gauss

def create_combined_filter(gauss_filter):
    """
    创建高斯-拉普拉斯组合滤波器
    
    参数:
        gauss_filter: 高斯滤波器矩阵
        
    返回:
        numpy.ndarray: 组合后的滤波器矩阵
        
    说明:
        使用3x3拉普拉斯滤波器与高斯滤波器卷积
        拉普拉斯核: [[0,-1,0],[-1,4,-1],[0,-1,0]]
    """
    # 学生需要实现：
    # 1. 定义3x3拉普拉斯滤波器
    # 2. 使用scipy.ndimage.convolve进行卷积
    # Define Laplacian kernel
    laplacian = np.array([[0, -1, 0],
                         [-1, 4, -1],
                         [0, -1, 0]])
    
    # Convolve Gaussian with Laplacian
    combined = sim.convolve(gauss_filter, laplacian, mode='constant', cval=0)
    
    return combined

def plot_filter_surface(filter, title):
    """
    绘制滤波器3D表面图
    
    参数:
        filter: 要绘制的滤波器矩阵
        title: 图形标题(使用英文) 
        
    说明:
        使用mpl_toolkits.mplot3d绘制3D表面
        图形尺寸设置为10x6英寸
    """
    # 学生需要实现：
    # 1. 创建fig和3D axes
    # 2. 使用plot_surface绘制表面
    # 3. 设置标题并显示图形
    # Create figure and 3D axes
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    # Create coordinate grid for plotting
    x = np.arange(filter.shape[1])
    y = np.arange(filter.shape[0])
    X, Y = np.meshgrid(x, y)
    
    # Plot surface
    surf = ax.plot_surface(X, Y, filter, cmap='viridis')
    
    # Add title and colorbar
    ax.set_title(title)
    fig.colorbar(surf)
    
    plt.show()

def process_and_display(stressFibers, filter, vmax_ratio=0.5):
    """
    处理图像并显示结果
    
    参数:
        stressFibers: 输入图像数据
        filter: 要应用的滤波器
        vmax_ratio: 显示时的最大强度比例(默认0.5)
        
    返回:
        numpy.ndarray: 处理后的图像数据
    """
    # 学生需要实现：
    # 1. 使用scipy.ndimage.convolve应用滤波器
    # 2. 使用plt.imshow显示结果，设置vmin=0, vmax=vmax_ratio*最大值
    # 3. 添加colorbar并显示图形
    # Apply the filter
    processed = sim.convolve(stressFibers, filter, mode='constant', cval=0)
    
    # Display the result
    plt.figure(figsize=(10, 6))
    plt.imshow(processed, cmap='gray', 
              vmin=0, vmax=vmax_ratio * np.max(processed))
    plt.colorbar()
    plt.title('Filtered Image')
    plt.show()
    
    return processed

def main():
    """
    主函数，执行完整的图像特征强调流程
    
    流程:
    1. 加载应力纤维数据
    2. 创建并可视化高斯滤波器
    3. 创建并可视化组合滤波器
    4. 应用不同方向的滤波器处理图像
    5. 显示处理结果
    """
    # 加载数据
    stressFibers = load_stress_fibers()
    
    # 任务(a): 创建并显示高斯滤波器
    gauss_filter = create_gauss_filter()
    # 学生需要添加:
    # 1. 使用plt.imshow显示滤波器
    # 2. 添加标题和colorbar
    # 3. 调用plot_filter_surface绘制3D图
    # Display Gaussian filter
    plt.figure(figsize=(10, 6))
    plt.imshow(gauss_filter, cmap='viridis')
    plt.colorbar()
    plt.title('Gaussian Filter')
    plt.show()
    
    # 3D surface plot
    plot_filter_surface(gauss_filter, 'Gaussian Filter Surface')
    # 任务(b): 创建组合滤波器并比较
    combined_filter = create_combined_filter(gauss_filter)
    # 学生需要添加显示代码
    # Display combined filter
    plt.figure(figsize=(10, 6))
    plt.imshow(combined_filter, cmap='viridis')
    plt.colorbar()
    plt.title('Combined Gaussian-Laplacian Filter')
    plt.show()
    
    # 3D surface plot
    plot_filter_surface(combined_filter, 'Combined Filter Surface')
    # 任务(c): 应用垂直滤波器
    # 学生需要添加处理代码
    # 任务(c): 应用垂直滤波器 (original Gaussian)
    print("Processing with vertical filter (Gaussian)")
    processed_vert = process_and_display(stressFibers, gauss_filter)
    # 任务(d): 应用水平滤波器
    # 学生需要添加处理代码
    # 任务(d): 应用水平滤波器 (rotated Gaussian)
    print("Processing with horizontal filter (rotated Gaussian)")
    # Rotate the Gaussian filter by 90 degrees for horizontal emphasis
    gauss_horizontal = np.rot90(gauss_filter)
    processed_horz = process_and_display(stressFibers, gauss_horizontal)
    # 选做: 45度方向滤波器
    # 学生需要添加处理代码
    # 选做: 45度方向滤波器 (combined filter)
    print("Processing with 45-degree filter (combined)")
    processed_combined = process_and_display(stressFibers, combined_filter)
if __name__ == "__main__":
    main()
