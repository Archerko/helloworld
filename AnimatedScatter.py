#coding:gb18030
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.font_manager import FontProperties
import getdata
import init_data
import spread_progress
import math
from sympy.series.formal import fps
from init_data import g_spread_rate
#from bitarray._bitarray import length

font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)

class AnimatedScatter(object):
    """An animated scatter plot using matplotlib.animations.FuncAnimation."""
    def __init__(self, filename , seed_num , deta = 0.5,arf = 1):
        self.arf = arf        #test fixed arf
        self.seed_num = seed_num #seed number
        #self.seed_num = [seed_num] #seed number
        self.deta = deta        #deta参数1，对感染概率的一个参数
        self.iter_max = 50000 #max iter times
        self.Matrix_R = getdata.get_matrix_from_file(filename,",") #get standard Relative Matrix from file，从文件中读取矩阵
        self.nums = len(self.Matrix_R ) #nums items of matrix  矩阵的长度即节点数量
        self.col_num = int(math.sqrt(self.nums)) #set col , row 设置多少行多少列（为后期画图）
        self.xlim = self.col_num+2
        self.ylim = self.col_num+self.col_num/2-5

        #update flow  data
        self.L_statu = []    #所有节点的状态
        self.L_namida = []    #所有节点被感染的概率
        self.L_relative = []     #节点间关系的矩阵

        #update  index for animation
        self.index = 0     #设置活跃节点为第一个？就是种子节点是第一个？

        #scatter type data
        self.type1_x = []
        self.type1_y = []
        self.type2_x = []
        self.type2_y = []
        self.type3_x = []
        self.type3_y = []
        self.type4_x = []
        self.type4_y = []
        #dymatic data
        self.List_Show = []
        # Setup the figure and axes...
        self.fig = plt.figure(figsize=(8, 8), dpi=80)
        self.axes = plt.subplot(111)


    def setup_data(self):
        """Initial scatter plot."""
        self.L_relative = init_data.init_relative(self.Matrix_R)  #获取矩阵关系情况，
        self.L_statu = init_data.init_data_Status(self.nums, self.seed_num) #所有节点的状态，种子为1，其他为0
        self.L_namida = spread_progress.namida_update(self.L_relative,self.L_statu,self.deta)
        L_tmp = spread_progress.statu_update(self.L_statu,self.L_namida,self.L_relative,self.seed_num,self.iter_max,self.arf,self.deta)
        # L_tmp[0] is itertimes L_tmp[1] is Propagation rate , L_tmp[2] is speed
        # L tmp[3] ->
        #[t,x,y,s]
        # t : type from I to Spread = 0 , from Spread to stiff = 1 ,  no changed = 2
        # x,y is the pos of infecter and Infected
        # s is the iterlevel of itertime
        self.List_Show.append(L_tmp[3])
        #print ("迭代次数")
        #print L_tmp[0]
        #print ("最终感染率")
        #print L_tmp[1]
        #return  L_tmp[0]  #返回传播迭代次数
        return  L_tmp  #返回整个传播情况的数组


    def x_map(self,i):
        x = i % self.col_num
        return x+1

    def y_map(self,i):
        y = i / self.col_num
        return y+1

    #remove pos from type1,2
    def find_del_index(self,pos):
        x = self.x_map(pos)
        y = self.y_map(pos)
        for m in range (len(self.type1_x)):
            if x == self.type1_x[m] and y == self.type1_y[m]:
                del self.type1_x[m]
                del self.type1_y[m]
                return 0
        for m in range (len(self.type2_x)):
            if x == self.type2_x[m] and y == self.type2_y[m]:
                del self.type1_x[m]
                del self.type1_y[m]
                return 0

        return -1

    def init_pic(self):
        """Initial first pic."""
        # type 1 : green Igo type 2 : red speard , type 3 : blue stiff  type 4 :yellow statu_change

        print 'first pic .'
        for i in range(self.nums) :
            self.type1_x.append( self.x_map(i))
            self.type1_y.append( self.y_map(i))

        self.type2_x.append( self.x_map(self.seed_num[0]))
        self.type2_y.append( self.y_map(self.seed_num[0]))
        self.find_del_index(self.seed_num[0])

        type1 = self.axes.scatter(self.type1_x, self.type1_y, s=20, c='green',animated=True)
        type2 = self.axes.scatter(self.type2_x, self.type2_y, s=80, c='red',animated=True)
        type3 = self.axes.scatter(self.type3_x, self.type3_y, s=40, c='blue',animated=True)
        type4 = self.axes.scatter(self.type4_x, self.type4_y, s=60, c='yellow',animated=True)
        # plt.scatter(matrix[:, 0], matrix[:, 1], s=20 * numpy.array(labels),
        #             c=50 * numpy.array(labels), marker='o',
        #             label='test')
        plt.xlabel(u'col  ', fontproperties=font)
        plt.ylabel(u'row  ', fontproperties=font)
        self.axes.legend((type1, type2, type3, type4), (u'igo', u'spr', u'stiff', u'infecting'), loc=0, prop=font)
        plt.ylim(-1,self.ylim)
        plt.xlim(-1,self.xlim)
        return type1,type2,type3,type4;

    def update(self,i):
        """Update the List_Show to scatter plot."""
        #update picture
        # type 1 : green Igo type 2 : red speard , type 3 : blue stiff  type 4 :yellow statu_change
        #used for video change  (statu , x, y , iter level)
        #statu 0 . I -> S. statu 1 S->Sti  statu 2 : no change(S-I) statu 3 : no change(S-s) statu 4 : no change(S-sti) statu 5  : progress
        L_tmp = self.List_Show[0][self.index]
        infect = L_tmp[1]
        infected = L_tmp[2]
        x_infect = self.x_map(infect)
        y_infect = self.y_map(infect)
        x_infected = self.x_map(infected)
        y_infected = self.y_map(infected)


        if L_tmp[0] == 0:
            self.type2_x.append( x_infected)
            self.type2_y.append( y_infected)
            self.type4_x = []
            self.type4_y = []
            #remove igo
            self.find_del_index(infected)

        elif L_tmp[0] == 1:
            self.type3_x.append(x_infect)
            self.type3_y.append(y_infect)
            self.type4_x = []
            self.type4_y = []
            #rm speard
            self.find_del_index(infect)
        #clean type4
        elif L_tmp[0] == 2:
            self.type4_x = []
            self.type4_y = []
        elif L_tmp[0] == 3:
            self.type4_x = []
            self.type4_y = []
        elif L_tmp[0] == 4:
            self.type4_x = []
            self.type4_y = []
        else :   #L_tmp[0] == 5 : show progress
            self.type4_x.append( x_infect)
            self.type4_y.append( y_infect)
            self.type4_x.append( x_infected)
            self.type4_y.append( y_infected)

        type1 = self.axes.scatter(self.type1_x, self.type1_y, s=20, c='green',animated=True)
        type2 = self.axes.scatter(self.type2_x, self.type2_y, s=80, c='red',animated=True)
        type3 = self.axes.scatter(self.type3_x, self.type3_y, s=40, c='blue',animated=True)
        type4 = self.axes.scatter(self.type4_x, self.type4_y, s=60, c='yellow',animated=True)

        # plt.scatter(matrix[:, 0], matrix[:, 1], s=20 * numpy.array(labels),
        #             c=50 * numpy.array(labels), marker='o',
        #             label='test')
        #update flow
        self.index+= 1
        return type1,type2,type3,type4;
    def show(self):
        # Then setup FuncAnimation.
        self.ani  =  animation.FuncAnimation(self.fig, self.update, interval=10, init_func=self.init_pic , blit=True)

        Writer = animation.writers['ffmpeg']
        writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
        #FFwriter = animation.FFMpegWriter()
        #self.ani.save('result.mp4', writer = writer,  dpi=255 ,extra_args=['-vcodec', 'libx264'])
        self.ani.save('result.mp4', writer = writer,  dpi=255 )
        plt.show()

if __name__ == '__main__':
    #deal with the input file to standard input file

    #standard input test
    a = AnimatedScatter("list2_1_matrix.csv",[136])    #读矩阵文件，设置种子节点的位置
    #a = AnimatedScatter("list2_1_matrix.csv",[0,83,229,102,2,114,9,78,97,306,125,20,345,42,29,80,2133,264,1367,439,69,30,129])    #读矩阵文件，设置种子节点的位置
    #ready for tst
    x1=0
    diedai_num=0.0
    chuanbo_num=0.0
    ganran_rate=0.0
    spread_rate_i_time=[]
    while x1<100:
        temp_list=a.setup_data()
        diedai_num+=temp_list[0] #计算迭代总数
        ganran_rate+=temp_list[1]
        chuanbo_num+=init_data.len_L_Video   #计算传播总数
        x1+=1
        #x2=0
        #temp_rate=init_data.g_spread_rate
        #print((g_spread_rate))
        #print(len(g_spread_rate))
       # spread_rate_i_time.append(g_spread_rate) #每次传播的传播率,一起存放到一个数组中。
       # g_spread_rate=[]



    #x3=0
   # while x3<len():
     #   spread_rate_i_time[x3]=spread_rate_i_time[x3]/100
     #   x3+=1
        """
          if(x1/10==0):
              print("迭代次数:")             #计算迭代平均数
              print(diedai_num/x1)
              print("传播扩散数:")           #计算传播平均数
              print(chuanbo_num/x1)
              print("最终感染率:")           #计算传播平均数
              print(ganran_rate/x1)
         """

    print("迭代次数:")             #计算迭代平均数
    print(diedai_num/100)
    print("传播扩散数:")           #计算传播平均数
    print(chuanbo_num/100)
    print("最终感染率:")           #计算感染率
    print(ganran_rate/100)
    #print("最终感染率变化:")           #计算感染率变化情况
    #print(spread_rate_i_time)
    #show the animations

    #a.show()
