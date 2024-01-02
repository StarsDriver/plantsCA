import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.patches as patches
from matplotlib.colors import BoundaryNorm
from matplotlib.colorbar import ColorbarBase
from matplotlib.ticker import FuncFormatter
import argparse

#设置命令行参数
#初始物种数量、（竞争系数）、互利系数、距离惩罚、干旱概率、干旱强度、植物死亡难度、输出图片保存文件夹、
parser = argparse.ArgumentParser()

parser.add_argument("-in","--init_num",type=int,help="初始时，每个物种的随机播种数量(默认值=100)",default=100,dest = "init_num")
parser.add_argument("-bf","--benefit_coef",type=float,help="特征间互利系数（默认值=8）",default = 8,dest = "benefit_coef")
parser.add_argument("-dp","--drought_probability",type=float,help="每次迭代中干旱发生的概率（默认值=0.5）",default= 0.5, dest="drought_probability")
parser.add_argument("-ds","--drought_strength",type=float,help = "干旱时元胞养分减少的百分比（默认值=0.5）",default=0.5,dest ="drought_strength")
parser.add_argument("-df","--die_diff",type=int,help="植物死亡需要连续缺少养分的回合数（默认值=1）",default=1,dest="die_diff")


args = parser.parse_args()

count = 0  #全局变量

plants_species_all = [] #所有的植株种类
plants_species_all.append((0,0,0))
plants_species_all.append((0,0,0))  #1
plants_species_all.append((0,0,1))#################################################################################
plants_species_all.append((0,1,0))
plants_species_all.append((1,0,0))
plants_species_all.append((1,1,0))
plants_species_all.append((0,1,1))
plants_species_all.append((1,0,1))
plants_species_all.append((1,1,1))

x=[]
y1=[]
y2 =[]
y3 = []
y4 = []
y5 = []
y6 = []
y7 = []
y8 = []
count = 0
epoch_count = [[0 for i in range(9)] for i in range(6)]



class Soil:

    def __init__(self):
        self.benefit_count = 0
        self.soil_nutrient = 100 #初始养分
        self.IsPoor = 0
        self.poor_count = 0
        self.plants_num = 0

    def grow_plants(self, plants_num):  # 在该地块种植物
        self.plants_num = plants_num

all_soil = [[Soil() for i in range(100)] for i in range(100)]
for i in range(args.init_num):     #生成的越多 互利种群接触的概率越大
    for j in range(1,9):###################################################################################
        x_new = random.randint(0,99)
        y_new = random.randint(0,99)
        all_soil[x_new][y_new].grow_plants(j)
    #    x_new = random.randint(0, 99)
     #   y_new = random.randint(0, 99)
      #  all_soil[x_new][y_new].grow_plants(5)

for epoch in range(1):

    def ani_update(k): #迭代次数


        global count #需要在函数体内部声明全局变量
        global x
        global y1
        global y2
        global y3
        global y4
        global y5
        global y6
        global y7
        global y8
        global all_soil
        global plants_species_all
        # 记录绘制折线图所需的数据
        if k % 1 == 0:
            x.append(count * 1)
            y1.append(0)
            y2.append(0)
            y3.append(0)
            y4.append(0)
            y5.append(0)
            y6.append(0)
            y7.append(0)
            y8.append(0)

            for i in range(100):
                for j in range(100):
                    if all_soil[i][j].plants_num == 1:
                        y1[count] += 1
                    elif all_soil[i][j].plants_num == 2:
                        y2[count] += 1
                    elif all_soil[i][j].plants_num == 3:
                        y3[count] += 1
                    elif all_soil[i][j].plants_num == 4:
                        y4[count] += 1
                    elif all_soil[i][j].plants_num == 5:
                        y5[count] += 1
                    elif all_soil[i][j].plants_num == 6:
                        y6[count] += 1
                    elif all_soil[i][j].plants_num == 7:
                        y7[count] += 1
                    elif all_soil[i][j].plants_num == 8:
                        y8[count] += 1
            count += 1

        if k%1 ==0:

            final_distribution = [[0 for i in range(100)] for i in range(100)]
            for i in range(100):
                for j in range(100):
                    final_distribution[i][j] = all_soil[i][j].plants_num
            bounds = [0, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5]

            # 定义颜色列表
            colors = ['#63b2ee ', '#76da91', '#f8cb7f', 'f89588', '#7cd6cf ', '#9192ab', '#7898e1 ', '#efa666 ', '#eddd86 ']

            # 创建离散的颜色映射
            cmap = plt.cm.colors.ListedColormap(colors)
            norm = BoundaryNorm(bounds, cmap.N)
            final_np = np.array(final_distribution)
          #  fig = plt.figure()
            plt.clf()  # 清空画布
            im = plt.imshow(final_np)
            # cb1 = plt.colorbar(im, fraction=0.03, pad=0.05,ticks=np.linspace(0, 100, 11))
            cb1 = plt.colorbar(im, fraction=0.03, cmap=cmap, norm=norm, boundaries=bounds, ticks=bounds,
                               orientation='vertical')
            tick_locator = ticker.MaxNLocator(nbins=9)  # colorbar上的刻度值个数
            plt.clim(0, 8.5)
            cb1.locator = tick_locator
            cb1.set_ticks([0.25, 1, 2, 3, 4, 5, 6, 7, 8])


            def format_fn(value, tick_number):

                if int(tick_number) == 0:
                    return f'none'
                elif int(tick_number) == 1:
                    return f'000'
                elif int(tick_number) == 2:
                    return f'001'
                elif int(tick_number) == 3:
                    return f'010'
                elif int(tick_number) == 4:
                    return f'100'
                elif int(tick_number) == 5:
                    return f'110'
                elif int(tick_number) == 6:
                    return f'011'
                elif int(tick_number) == 7:
                    return f'101'
                elif int(tick_number) == 8:
                    return f'111'


            cb1.update_ticks()
            cb1.ax.yaxis.set_major_formatter(FuncFormatter(format_fn))
            plt.title(f"{k}")
            ####新图片平滑替代旧图片
            ####
            fig.savefig(fname=f"./outputs/{epoch}{k}.png")
        for i in range(100):
            for j in range(100):
                all_soil[i][j].soil_nutrient= 100

        if k>=100:#######################################################################################################
            p = random.random()
            if p >args.drought_probability :
                for i in range(100):
                    for j in range(100):
                        all_soil[i][j].soil_nutrient = 100
            else:
                for i in range(100):
                    for j in range(100):
                        all_soil[i][j].soil_nutrient =100*(1-args.drought_strength)

        for i in range(100):
            for j in range(100):
                x_1 = 0
                x_2 = 0
                x_3 = 0

                if plants_species_all[all_soil[i][j].plants_num][0] ==0:

                    try:
                        if plants_species_all[all_soil[i][j+1].plants_num][0] ==1:
                            x_1 +=1
                    except:
                        pass
                    try:
                        if plants_species_all[all_soil[i+1][j].plants_num][0] ==1:
                            x_1 +=1
                    except:
                        pass
                    try:
                        if plants_species_all[all_soil[i+1][j+1].plants_num][0] ==1:
                            x_1 +=1
                    except:
                        pass
                    try:
                        if plants_species_all[all_soil[i-1][j].plants_num][0] == 1:
                            x_1 +=1
                    except:
                        pass
                    try:
                        if plants_species_all[all_soil[i-1][j+1].plants_num][0] ==1:
                            x_1 +=1
                    except:
                        pass
                    try:
                        if plants_species_all[all_soil[i][j-1].plants_num][0] ==1:
                            x_1 +=1
                    except:
                        pass
                    try:
                        if plants_species_all[all_soil[i+1][j-1].plants_num][0] ==1:
                            x_1 +=1
                    except:
                        pass
                    if plants_species_all[all_soil[i-1][j-1].plants_num][0] ==1:
                        x_1 +=1
                    #第二圈
                    try:
                        for l in range(-2,3):
                            if plants_species_all[all_soil[i+2][j+l].plants_num][0] == 1:
                                x_1 += 0.5
                    except:
                        pass
                    try:
                        for l in range(-2,3):
                            if plants_species_all[all_soil[i+1][j+l].plants_num][0] ==1:
                                x_1 += 0.5
                    except:
                        pass
                    try:
                        for l in range(-2,1):
                            if plants_species_all[all_soil[i+l][j+1].plants_num][0] ==1:
                                x_1 +=0.5
                    except:
                        pass
                    try:
                        for l in range(-2,1):
                            if plants_species_all[all_soil[i+l][j+2].plants_num][0]==1:
                                x_1 += 0.5
                    except:
                        pass
                    for l in range(-2,1):
                        if plants_species_all[all_soil[i+l][j-1].plants_num][0]==1:
                            x_1+=0.5
                        if plants_species_all[all_soil[i+l][j-2].plants_num][0]==1:
                            x_1+=0.5
                    try:
                        for l in range(0,2):
                            if plants_species_all[all_soil[i+l][j].plants_num][0]==1:
                                x_1+=0.5
                            if plants_species_all[all_soil[i+l][j+1].plants_num][0]==1:
                                x_1+=0.5
                    except:
                        pass

                if plants_species_all[all_soil[i][j].plants_num][1] ==0:

                    try:
                        if plants_species_all[all_soil[i][j + 1].plants_num][1] == 1:
                            x_2 += 1
                    except:
                        pass
                    try:
                        if plants_species_all[all_soil[i + 1][j].plants_num][1] == 1:
                            x_2 += 1
                    except:
                        pass
                    try:
                        if plants_species_all[all_soil[i + 1][j + 1].plants_num][1] == 1:
                            x_2 += 1
                    except:
                        pass
                    try:
                        if plants_species_all[all_soil[i - 1][j].plants_num][1] == 1:
                            x_2 += 1
                    except:
                        pass
                    try:
                        if plants_species_all[all_soil[i - 1][j + 1].plants_num][1] == 1:
                            x_2 += 1
                    except:
                        pass
                    try:
                        if plants_species_all[all_soil[i][j - 1].plants_num][1] == 1:
                            x_2 += 1
                    except:
                        pass
                    try:
                        if plants_species_all[all_soil[i + 1][j - 1].plants_num][1] == 1:
                            x_2 += 1
                    except:
                        pass
                    if plants_species_all[all_soil[i - 1][j - 1].plants_num][1] == 1:
                        x_2 += 1

                    try:
                        for l in range(-2, 3):
                            if plants_species_all[all_soil[i + 2][j + l].plants_num][1] == 1:
                                x_2 += 0.5
                    except:
                        pass
                    try:
                        for l in range(-2, 3):
                            if plants_species_all[all_soil[i + 1][j + l].plants_num][1] == 1:
                                x_2 += 0.5
                    except:
                        pass
                    try:
                        for l in range(-2, 1):
                            if plants_species_all[all_soil[i + l][j + 1].plants_num][1] == 1:
                                x_2 += 0.5
                    except:
                        pass
                    try:
                        for l in range(-2, 1):
                            if plants_species_all[all_soil[i + l][j + 2].plants_num][1] == 1:
                                x_2 += 0.5
                    except:
                        pass
                    for l in range(-2, 1):
                        if plants_species_all[all_soil[i + l][j - 1].plants_num][1] == 1:
                            x_2 += 0.5
                        if plants_species_all[all_soil[i + l][j - 2].plants_num][1] == 1:
                            x_2 += 0.5
                    try:
                        for l in range(0, 2):
                            if plants_species_all[all_soil[i + l][j].plants_num][1] == 1:
                                x_2 += 0.5
                            if plants_species_all[all_soil[i + l][j + 1].plants_num][1] == 1:
                                x_2 += 0.5
                    except:
                        pass

                if plants_species_all[all_soil[i][j].plants_num][2] == 0:  # 三维是受利方

                    # 第一圈
                    try:
                        if plants_species_all[all_soil[i][j + 1].plants_num][2] == 1:
                            x_3 += 1
                    except:
                        pass
                    try:
                        if plants_species_all[all_soil[i + 1][j].plants_num][2] == 1:
                            x_3 += 1
                    except:
                        pass
                    try:
                        if plants_species_all[all_soil[i + 1][j + 1].plants_num][2] == 1:
                            x_3 += 1
                    except:
                        pass
                    try:
                        if plants_species_all[all_soil[i - 1][j].plants_num][2] == 1:
                            x_3 += 1
                    except:
                        pass
                    try:
                        if plants_species_all[all_soil[i - 1][j + 1].plants_num][2] == 1:
                            x_3 += 1
                    except:
                        pass
                    try:
                        if plants_species_all[all_soil[i][j - 1].plants_num][2] == 1:
                            x_3 += 1
                    except:
                        pass
                    try:
                        if plants_species_all[all_soil[i + 1][j - 1].plants_num][2] == 1:
                            x_3 += 1
                    except:
                        pass
                    if plants_species_all[all_soil[i - 1][j - 1].plants_num][2] == 1:
                        x_3 += 1
                    # 第二圈
                    try:
                        for l in range(-2, 3):
                            if plants_species_all[all_soil[i + 2][j + l].plants_num][2] == 1:
                                x_3 += 0.5
                    except:
                        pass
                    try:
                        for l in range(-2, 3):
                            if plants_species_all[all_soil[i + 1][j + l].plants_num][2] == 1:
                                x_3 += 0.5
                    except:
                        pass
                    try:
                        for l in range(-2, 1):
                            if plants_species_all[all_soil[i + l][j + 1].plants_num][2] == 1:
                                x_3 += 0.5
                    except:
                        pass
                    try:
                        for l in range(-2, 1):
                            if plants_species_all[all_soil[i + l][j + 2].plants_num][2] == 1:
                                x_3 += 0.5
                    except:
                        pass
                    for l in range(-2, 1):
                        if plants_species_all[all_soil[i + l][j - 1].plants_num][2] == 1:
                            x_3 += 0.5
                        if plants_species_all[all_soil[i + l][j - 2].plants_num][2] == 1:
                            x_3 += 0.5
                    try:
                        for l in range(0, 2):
                            if plants_species_all[all_soil[i + l][j].plants_num][2] == 1:
                                x_3 += 0.5
                            if plants_species_all[all_soil[i + l][j + 1].plants_num][2] == 1:
                                x_3 += 0.5
                    except:
                        pass
                x_count=0
                x_count +=x_1
                x_count +=x_2
                x_count +=x_3
                all_soil[i][j].benefit_count = x_count

        #判定每个地块的受利点数/受利养分
        for i in range(100):
            for j in range(100):
                #系数为6时会有一小片地稳定 不会稳定长久
                #系数为7稳定长久 但面积小
                all_soil[i][j].soil_nutrient +=all_soil[i][j].benefit_count*args.benefit_coef###################################################
                #print(all_soil[i][j].soil_nutrient)
                # 营养吸收
        for i in range(100):
            for j in range(100):
                if all_soil[i][j].plants_num != 0:

                    all_soil[i][j].soil_nutrient -= 20
                    #print(all_soil[i][j].soil_nutrient)

                    try:
                        all_soil[i][j + 1].soil_nutrient -= 10
                    except:
                        pass
                    try:
                        all_soil[i + 1][j + 1].soil_nutrient -= 10
                    except:
                        pass
                    try:
                        all_soil[i + 1][j].soil_nutrient -= 10
                    except:
                        pass

                    all_soil[i - 1][j].soil_nutrient -= 10
                    try:
                        all_soil[i - 1][j + 1].soil_nutrient -= 10
                    except:
                        pass

                    all_soil[i][j - 1].soil_nutrient -= 10
                    try:
                        all_soil[i + 1][j - 1].soil_nutrient -= 10
                    except:
                        pass

                    all_soil[i - 1][j - 1].soil_nutrient -= 10

        for i in range(100):
            for j in range(100):
                all_soil[i][j].IsPoor = 0; #贫瘠状态复位
        for i in range(100):
            for j in range(100):
                if all_soil[i][j].soil_nutrient <0:
                    #print(all_soil[i][j].soil_nutrient)
                    all_soil[i][j].IsPoor = 1
        #营养不良累计次数计算###########################################################################
        for i in range(100):
            for j in range(100):
                if all_soil[i][j].plants_num != 0:
                    if all_soil[i][j].IsPoor == 1:
                        all_soil[i][j].poor_count += 1
                    else:
                        all_soil[i][j].poor_count = 0
                    if all_soil[i][j].poor_count > args.die_diff-1:
                        all_soil[i][j].plants_num = 0  # 连续两次营养不良就死
                        all_soil[i][j].poor_count = 0  # 累计次数归零
        #统计每类植物数量
        n = []
        for i in range(9):
            n.append(0)
        #n[0]是总数量
        for i in range(100):
            for j in range(100):
                if all_soil[i][j].plants_num ==1:
                    n[1]+=1
                elif all_soil[i][j].plants_num ==2:
                    n[2]+=1
                elif all_soil[i][j].plants_num ==3:
                    n[3]+=1
                elif all_soil[i][j].plants_num ==4:
                    n[4]+=1
                elif all_soil[i][j].plants_num ==5:
                    n[5]+=1
                elif all_soil[i][j].plants_num ==6:
                    n[6]+=1
                elif all_soil[i][j].plants_num ==7:
                    n[7]+=1
                elif all_soil[i][j].plants_num ==8:
                    n[8]+=1
        n[0]=n[1]+n[2]+n[3]+n[4]+n[5]+n[6]+n[7]+n[8]
        # 进行繁殖判定
        for i in range(100):
            for j in range(100):
                if all_soil[i][j].plants_num != 0 and all_soil[i][j].IsPoor == 0:  # 健康植株可繁殖
                    new_x = i + random.randint(-1, 1)
                    new_y = j + random.randint(-1, 1)
                    #计算该植株的繁殖概率
                    p_norm = 0.5*(1-n[all_soil[i][j].plants_num]/10000 - (n[0]-n[all_soil[i][j].plants_num])/10000)
                    #辛普森指数？
                    p = random.random()
                    if p<p_norm:
                        if new_x > 99 or new_y > 99 or all_soil[new_x][new_y].plants_num != 0:
                            continue
                        else:
                            all_soil[new_x][new_y].grow_plants(all_soil[i][j].plants_num)


    import matplotlib.animation as animation
    fig = plt.figure()

    # 创建动画对象
    anim = animation.FuncAnimation(fig, ani_update, frames=1000, interval=1,repeat=False)

    # 显示动画
    plt.show()
    #画折线图
    fig = plt.figure()######################################################################################
    line1 , =plt.plot(x,y1,label = '000');plt.xlim(0, 1300);last_point = (x[-1], y1[-1]);plt.annotate(str(y1[-1]), xy=last_point, xytext=(10, 0),textcoords='offset points', ha='left', va='center')
    line2 , =plt.plot(x,y2,label = '001');last_point = (x[-1], y2[-1]);plt.annotate(str(y2[-1]), xy=last_point, xytext=(10, 0),textcoords='offset points', ha='left', va='center')
    line3, = plt.plot(x,y3,label = '010');last_point = (x[-1], y3[-1]);plt.annotate(str(y3[-1]), xy=last_point, xytext=(10, 0),textcoords='offset points', ha='left', va='center')
    line4, = plt.plot(x,y4,label = '100');last_point = (x[-1], y4[-1]);plt.annotate(str(y4[-1]), xy=last_point, xytext=(10, 0),textcoords='offset points', ha='left', va='center')
    line5, = plt.plot(x,y5,label = '110');last_point = (x[-1], y5[-1]);plt.annotate(str(y5[-1]), xy=last_point, xytext=(10, 0),textcoords='offset points', ha='left', va='center')
    line6, = plt.plot(x,y6,label = '011');last_point = (x[-1], y6[-1]);plt.annotate(str(y6[-1]), xy=last_point, xytext=(10, 0),textcoords='offset points', ha='left', va='center')
    line7, = plt.plot(x,y7,label = '101');last_point = (x[-1], y7[-1]);plt.annotate(str(y7[-1]), xy=last_point, xytext=(10, 0),textcoords='offset points', ha='left', va='center')
    line8, = plt.plot(x,y8,label = '111');last_point = (x[-1], y8[-1]);plt.annotate(str(y8[-1]), xy=last_point, xytext=(10, 0),textcoords='offset points', ha='left', va='center')
    plt.legend(handles=[line1,line2,line3,line4,line5,line6,line7,line8], loc='lower right')
    #plt.legend(handles=[line2,line5], loc='upper left')
    #plt.title('species abundance curve(2 recipient plant)')################################################################
    fig.savefig(fname=f'{epoch}line.png')
    #输出最后一刻植物数量
    with open(f'{epoch}count.txt','w') as f:
            f.write(f'plants1:{y1[-1]}\n')
            f.write(f'plants2:{y2[-1]}\n')
            f.write(f'plants3:{y3[-1]}\n')
            f.write(f'plants4:{y4[-1]}\n')
            f.write(f'plants5:{y5[-1]}\n')
            f.write(f'plants6:{y6[-1]}\n')
            f.write(f'plants7:{y7[-1]}\n')
            f.write(f'plants8:{y8[-1]}\n')

    epoch_count[0][epoch] = y2[-1]
    epoch_count[1][epoch] = y3[-1]
    epoch_count[2][epoch] = y4[-1]
    epoch_count[3][epoch] = y5[-1]
    epoch_count[4][epoch] = y6[-1]
    epoch_count[5][epoch] = y7[-1]

print(epoch_count)