import re
import matplotlib.pyplot as plt

import pysnooper
@pysnooper.snoop()
def desk():
    # 打开存放有清洗后的定位定向有效坐标的文件view1.txt
    with open('AAA085.xls', 'r', encoding="utf-8") as f:
        gpscont = f.read()
        pattern = re.compile('(\$GPHPD.*?4\*\w\w)')
        results = re.findall(pattern, gpscont)
        N_list, E_list, h_list, e_dis, n_dis, t_dis = [], [], [], [], [], []
        for result in results:
            rnc_line = result.strip().split(",")
            N_list.append(float(rnc_line[1]))
            E_list.append(float(rnc_line[2]))
        print('纬度：',N_list,'\n','经度',E_list,'\n',len(E_list))
        plt.figure(figsize=(8,6))
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.plot(E_list,N_list,'r.'), plt.title('小推车行驶轨迹图')
        plt.xlabel('经度E'), plt.ylabel('纬度N')
        plt.show()

if __name__ =='__main__':
    desk()
#



























# import re
# import numpy as np
# import matplotlib.pyplot as plt
# import scipy.integrate as si
#
# with open('dt.txt','r',encoding="utf-8") as f:
#     gpscont = f.read()
#     pattern = re.compile('(\$\w\wRMC.*?A\*\w\w)')
#     results = re.findall(pattern, gpscont)
#     with open('view.txt', 'w', encoding='utf-8') as g:
#         # RNC_list = []
#         N_list = []
#         t = np.arange(0,len(results))
#         for result in results:
#             g.write(result+'\n')
#             rnc_line = result.strip().split(",")
#             # RNC_list.append(rnc_line)
#             N_list.append(float(rnc_line[7]))
#
#         y_fit = np.polyfit(t, N_list, 3)#多项式拟合
#         print(y_fit)
#         y_fitnum = y_fit[0]*t**3+y_fit[1]*t**2+y_fit[2]*t+y_fit[3]
#         plt.plot(t,y_fitnum,'r-')
#
#         fc = 0
#         for i in range(len(N_list)):
#             fc+=(y_fit[0]*i**3+y_fit[1]*i**2+y_fit[2]*i+y_fit[3]-N_list[i])**2
#         fc = fc/len(N_list)
#         sdt=np.trapz(y_fitnum,t)#对拟合曲线积分得到路程
#
#         plt.plot(t,N_list,'g.')
#         plt.title('速度-时间关系\n拟合曲线方程：y=%.03fx^3+%.03fx^2+%.03ft+%.03f\n系数：%s;%s;%s\n拟合曲线方差：%.04f   行驶里程：%.03f米'%(y_fit[0],y_fit[1],y_fit[2],y_fit[3],y_fit[0],y_fit[1],y_fit[2], fc,sdt))
#         plt.xlabel('时间s')
#         plt.ylabel('速度m/s')
#         plt.rcParams['font.sans-serif'] = ['SimHei']
#         plt.show()

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# import re
# import matplotlib.pyplot as plt
#
# def desk():
#     with open('dt.txt', 'r', encoding="utf-8") as f:
#         gpscont = f.read()
#         pattern1 = re.compile('(\$\w\wRMC.*?A\*\w\w)')
#         pattern2 = re.compile('(\$\w\wGGA.*?\*\w\w)')
#         pattern3 = re.compile('(\$GPGSV.*?\*\w\w)')
#         results1 = re.findall(pattern1, gpscont)
#         results2 = re.findall(pattern2, gpscont)
#         results3 = re.findall(pattern3, gpscont)
#
#         time, N_list, E_list, v_list = [], [], [], []
#         for result in results1:
#             rnc_line = result.strip().split(",")
#             time.append(int(float((rnc_line[1]))))
#             N_list.append(float(rnc_line[3]))
#             E_list.append(float(rnc_line[5]))
#             v_list.append(float(rnc_line[7]))
#
#         height = []
#         for result in results2:
#             gga_line = result.strip().split(",")
#             height.append(float(gga_line[9]))
#
#         sign = []
#         for i in range(0,len(results3),3):
#             gsv_line = results3[i].strip().split(",")
#             sign.append(gsv_line[7])
#
#     plt.figure(figsize=(8,6))
#     plt.ion()
#     for i in range(len(time)):
#         plt.subplot(2,2,1)
#         plt.rcParams['font.sans-serif'] = ['SimHei']
#         plt.plot(E_list[i],N_list[i],'r.'), plt.title(str(time[0]//10000+8)+':'+str(time[0]%10000//100)+':'+str(time[0]%100)+'至'\
#                                                       +str(time[-1]//10000+8)+':'+str(time[-1]%10000//100)+':'+str(time[-1]%100)+'\n'+'经纬度')
#         plt.xlabel('E'), plt.ylabel('N')
#         plt.subplot(222)
#         plt.plot(time[i],v_list[i],'g.'),plt.title('瞬时速度m/s'),plt.xlabel('时间(s)'),plt.ylabel('速度(m/s)')
#         plt.subplot(223)
#         plt.plot(time[i],height[i],'b.'),plt.xlabel('时间(s)'),plt.ylabel('海拔高度(m)')
#
#         plt.subplot(224)
#         plt.plot(time[i],sign[i],'k*'),plt.xlabel('时间(s)'),plt.ylabel('%s号卫星信噪比'%int(float(results3[0].strip().split(',')[4])))
#         plt.pause(0.1)
#     plt.ioff()
#     plt.show()
#
# if __name__ =='__main__':
#     desk()
#
# # import re
# # import numpy as np
# # import matplotlib.pyplot as plt
# # import scipy.integrate as si
# #
# # with open('dt.txt','r',encoding="utf-8") as f:
# #     gpscont = f.read()
# #     pattern = re.compile('(\$\w\wRMC.*?A\*\w\w)')
# #     results = re.findall(pattern, gpscont)
# #     with open('view.txt', 'w', encoding='utf-8') as g:
# #         # RNC_list = []
# #         N_list = []
# #         t = np.arange(0,len(results))
# #         for result in results:
# #             g.write(result+'\n')
# #             rnc_line = result.strip().split(",")
# #             # RNC_list.append(rnc_line)
# #             N_list.append(float(rnc_line[7]))
# #
# #         y_fit = np.polyfit(t, N_list, 3)#多项式拟合
# #         print(y_fit)
# #         y_fitnum = y_fit[0]*t**3+y_fit[1]*t**2+y_fit[2]*t+y_fit[3]
# #         plt.plot(t,y_fitnum,'r-')
# #
# #         fc = 0
# #         for i in range(len(N_list)):
# #             fc+=(y_fit[0]*i**3+y_fit[1]*i**2+y_fit[2]*i+y_fit[3]-N_list[i])**2
# #         fc = fc/len(N_list)
# #         sdt=np.trapz(y_fitnum,t)#对拟合曲线积分得到路程
# #
# #         plt.plot(t,N_list,'g.')
# #         plt.title('速度-时间关系\n拟合曲线方程：y=%.03fx^3+%.03fx^2+%.03ft+%.03f\n系数：%s;%s;%s\n拟合曲线方差：%.04f   行驶里程：%.03f米'%(y_fit[0],y_fit[1],y_fit[2],y_fit[3],y_fit[0],y_fit[1],y_fit[2], fc,sdt))
# #         plt.xlabel('时间s')
# #         plt.ylabel('速度m/s')
# #         plt.rcParams['font.sans-serif'] = ['SimHei']
# #         plt.show()
