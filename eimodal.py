import scipy as sp
import math as m
import numpy as np
import matplotlib.pyplot as plt

#当前时刻环境参数条件下，汽车百公里能耗计算
di = 100000#100km
g = 9.807#m/s^2

def Vv_Ei(list):
    '''
        list = [M, f, ai, p, A, Vv, Vw, Cd, d, a, gt]
        汽车总质量、滚动摩擦系数、道路坡度(高长比)、空气密度、迎风面积、车速、风速、空气阻力系数、旋转质量换算系数、加速度、传动系统效率
    '''
    M, f, ai, p, A = list[0], list[1], m.atan(list[2]), list[3], list[4]
    Vv = np.arange(2, 120, 2)
    Vw, Cd, d, a, gt = list[6]/3.6, list[7], list[8], list[9], list[10]
    Ei = []
    for i in range(len(Vv)):
        Vv1 = Vv[i]/3.6
        Ei.append(di*(M*g*f*m.cos(ai)+Cd*A*p*(Vv1-Vw)**2/2+M*g*m.sin(ai)+d*M*a)/gt/3600000)#单位kWh
    return Vv, Ei

def V_E_plot(Vv, Ei):
    plt.plot(Vv, Ei, 'r-')
    plt.title("百公里能耗与车速关系\nM=%dkg:f=%.02f;p=%.03fkg/m^3;A=%.02fm^2;Vw=%.02fm/s;\nCd=%.02f;ai=%.02f;d=%.02f;a=%.02fm/s^2;gt=%.02f"\
              %(patt_list[0][0],patt_list[0][1],patt_list[0][3],patt_list[0][4],patt_list[0][6],patt_list[0][7],\
                patt_list[0][2],patt_list[0][8],patt_list[0][9],patt_list[0][10]))
    plt.xlabel("车速m/s")
    plt.ylabel("100km能耗kWh")
    plt.grid()
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.show()

if __name__ == "__main__":
    data = np.genfromtxt("data.csv", delimiter=",")
    patt_list = data[1:, :]
    for i in range(len(patt_list)):
        Vv, Ei = Vv_Ei(patt_list[i])
        # print('瞬时百公里能耗：%.3fKwh'%Ei)
        V_E_plot(Vv, Ei)