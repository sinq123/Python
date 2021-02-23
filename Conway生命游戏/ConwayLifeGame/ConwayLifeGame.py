import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys, argparse, os

#全局变量
ON = 255
OFF = 0
vals = [ON, OFF]


# 随机图案
def randommGrid(N):
    return np.random.choice(vals, N*N, p=[0.3, 0.7]).reshape(N, N)

# 用滑翔机图案
def addGlider(i, j, grid):
    glider = np.array([[0, 0, 255],
                       [255, 0, 255],
                       [0, 255, 255]])
    grid[i:i+3, j:j+3] = glider

# 更新
def update(frameNum, img, grid, N):
    # copy grid since we require 8 neighbors for calculation and we go line by line
    # 复制网格，因为我们需要8个邻居进行计算，我们逐行进行
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            # compute 8-neghbor sum using toroidal boundary conditions x and y wrap around to that the simulation takes place on a toroidal surface
            # 使用环形边界条件x和y绕包计算8负或和，以便模拟发生在环形表面上
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] + grid[(i-1)%N, j] + grid[(i+1)%N, j] + 
                         grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] + grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N]) / 255)
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON

    img.set_data(newGrid)
    grid[:]=newGrid[:]
    return img


def main():
    #传入参数
    # command line argumentss are in sys.argv[1], sys.argv[2]...
    # 命令行参数在系统argv[1] 你说，系统argv[2] 。。。
    # sys.argv[0] is the script name and can be ignored
    # 系统argv[0]是脚本名称，可以忽略
    # parss arguments
    # parss参数
    parser = argparse.ArgumentParser(description="Runs Conway's Games of Life simulation.(运行康威的生命模拟游戏。)")
    # 参数说明
    # 网格大小
    parser.add_argument('--grid-size', dest='N', required=False)
    # 保存文件名称 .mov
    parser.add_argument('--mov-file', dest='movfile', required=False)
    # 动画更新间隔 毫秒级
    parser.add_argument('--interval', dest='interval', required=False)
    # 用滑翔机图案模拟
    parser.add_argument('--glider', action='store_true', required=False)
    parser.add_argument('--gosper', action='store_true', required=False)
    args = parser.parse_args()

    # 网格大小
    N = 100
    if args.N and int(args.N) > 8:
        N = int(args.N)

    # 更新间隔
    updateInretval = 50
    if args.interval:
        updateInretval = int(args.interval)

    # 初始化图案
    grid = np.array([])
    if args.glider:
        grid = np.zeros(N*N).reshape(N,N)
        addGlider(1, 1, grid)
    else:
        grid = randommGrid(N)

    # 显示
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N), frames=10, interval=updateInretval, save_count=50)

    if args.movfile:
        ani.save(args.movfile)

    plt.title("ConwayLifeGame")
    plt.show()


if __name__ == '__main__':
    main()