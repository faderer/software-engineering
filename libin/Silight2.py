import matplotlib.pyplot as plt
from pylab import mpl
import numpy as np
from scipy import interpolate
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

data_x0,data_y0,data_x1,data_y1=[],[],[],[]

x0="1574	932	525.8	325.7	137.8	97.4	78.8	46.2	23.1	7.3	0.8"
y0="0.4059	0.3974	0.3786	0.3734	0.3622	0.3429	0.3266	0.3016	0.2757	0.24	0.1596"
x1="102.3	453.3	820.6	1003	1173	1557"
y1="3.3	13.8	32.4	43.6	55.1	71.5"

x0=x0.split("\t")
y0=y0.split("\t")
x1=x1.split("\t")
y1=y1.split("\t")

for i in range(len(x0)):
    data_x0.append(float(x0[i]))
    data_y0.append(float(y0[i]))
for i in range(len(x1)):
    data_x1.append(float(x1[i]))
    data_y1.append(float(y1[i]))
print(data_x0,data_x1)


_, ax_f = plt.subplots()
# 这步是关键
ax_c = ax_f.twinx()
# ax_d = ax_f.twiny()

# automatically update ylim of ax2 when ylim of ax1 changes.
# ax_f.callbacks.connect("ylim_changed", convert_ax_c_to_celsius)
# ax_f.plot(np.linspace(-40, 120, 100))
ax_f.set_xlim(0, 1600)

# ax_f.set_title('第二坐标', size=14)
ax_f.set_ylabel('U(V)',color='r',fontsize=12)
ax_f.set_xlabel('光强E(Lux)',color='black',fontsize=12)
ax_f.plot(data_x0,data_y0,c = 'r',marker='*',markerfacecolor='w') # lw是曲线的粗细  ,c="red",marker=">" ,markersize = 0

ax_c.set_ylabel('I(μA)', color='b',fontsize=12)
# ax_c.set_yticklabels(["$0$", r"$\frac{1}{2}\pi$", r"$\pi$", r"$\frac{3}{2}\pi$", r"$2\pi$"])
ax_c.set_ylim(0,80)

# ax_d.set_xlabel('第二X轴', color='g')
# ax_d.set_xlim(-1,1)
ax_c.plot(data_x1,data_y1,c = 'b',marker='*',markerfacecolor='w')
ax_f.text(400,0.385,"电压",color='r',ha='left',  fontsize=20)
ax_f.text(800,0.293,"电流",color='b',ha='left',  fontsize=20)
ax_f.text(1000,0.2,"作者 夏里宾\n 581021910503\n日期 2019.10.31",ha='left',  fontsize=16)

plt.show()
