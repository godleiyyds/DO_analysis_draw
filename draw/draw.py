import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import cmaps
import os

def sandian(file,station='北礵',x="mod"):
    df = pd.read_excel(file, sheet_name=station, engine='openpyxl')

    time = df["时间"]  # 时间
    obs = df["观察值"]  # 溶解氧
    pred = df[x]  # 叶绿素
    # salinity = df["attention_group_swish/attention_lyr1_8"]  # 盐度

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    # 创建图形
    fig, ax = plt.subplots()

    # 绘制时序图
    ax.scatter(time, obs, label="obs")  # 溶解氧
    ax.scatter(time, pred, label=x)  # 叶绿素
    # ax.scatter(time, salinity, label="attention_lyr1_8")  # 盐度

    # 设置图例和标签
    ax.legend()
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")

    # my_title = {'北礵':'bei_shuang',
    #     '姥屿':"mu_yu",
    #     '筶杯岛':'gao_bei_dao',
    #     '港南':'gan_nan',
    #     '闽江口1号':'ming_jiang_kou_1',
    #     '湄洲岛':'mei_zhou_dao',
    #     '榕海Ⅳ号':'rong_hai_4',
    #      '鸟屿':'niao_yu',
    #     '同心湾2号':'tong_xin_wan_2'}
    # ax.set_title(my_title[station])
    ax.set_title(station)

    # save_dir=f"picture/{station}/"+x
    # save_dir = "picture/" + x + f'/{station}'
    save_dir = "picture/" + x

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # # 保存为矢量图 (SVG格式)
    plt.savefig(save_dir + f'/{station}.svg',format='svg')
    #
    # # 保存为矢量图 (PDF格式)
    # plt.savefig("timeseries.pdf", format='pdf')

    # 显示图形
    # plt.show()
    plt.close()
    print(save_dir + ".svg___saved!")

def tar(ax, r, std, model,station):
    # plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文
    # plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    ax.set_thetalim(thetamin=0, thetamax=90)
    r_small, r_big, r_interval = 0, 1.5 + 0.1, 0.5  # 横纵坐标范围，最小值 最大值 间隔
    ax.set_rlim(r_small, r_big)
    rad_list = [0, 0.2, 0.4, 0.6, 0.7, 0.8, 0.85, 0.9, 0.95, 0.99, 1]  # 需要显示数值的主要R的值
    minor_rad_list = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.86, 0.87, 0.88, 0.89,
                      0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1]  # 需要显示刻度的次要R的值
    angle_list = np.rad2deg(np.arccos(rad_list))
    angle_list_rad = np.arccos(rad_list)
    angle_minor_list = np.arccos(minor_rad_list)
    ax.set_thetagrids(angle_list, rad_list)
    for i in np.arange(r_small, r_big, r_interval):
        if i == 1:
            ax.text(0, i, s='\n' + 'REF', ha='center', va='top')
            # text的第一个坐标是角度（弧度制），第二个是距离
        else:
            ax.text(0, i, s='\n' + str(i), ha='center', va='top')
        ax.text(np.pi / 2, i, s=str(i) + '  ', ha='right', va='center')
    ax.set_rgrids([])
    labels = ax.get_xticklabels() + ax.get_yticklabels()
    ax.grid(False)
    angle_linewidth, angle_length, angle_minor_length = 0.8, 0.02, 0.01
    tick = [ax.get_rmax(), ax.get_rmax() * (1 - angle_length)]
    tick_minor = [ax.get_rmax(), ax.get_rmax() * (1 - angle_minor_length)]
    for t in angle_list_rad:
        ax.plot([t, t], tick, lw=angle_linewidth, color="k")  # 第一个坐标是角度（角度制），第二个是距离
    for t in angle_minor_list:
        ax.plot([t, t], tick_minor, lw=angle_linewidth, color="k")  # 第一个坐标是角度（角度制），第二个是距离

    # 然后开始绘制以REF为原点的圈，可以自己加圈
    circle = plt.Circle((1, 0), 0.25, transform=ax.transData._b, facecolor=(0, 0, 0, 0), edgecolor='gray',linestyle='--', linewidth=0.8)
    ax.add_artist(circle)

    # 绘制以原点为圆点的圆圈：
    circle4 = plt.Circle((0, 0), 0.5, transform=ax.transData._b, facecolor=(0, 0, 0, 0), edgecolor='grey',
                         linestyle='--', linewidth=1.0)
    circle5 = plt.Circle((0, 0), 1, transform=ax.transData._b, facecolor=(0, 0, 0, 0), edgecolor='grey', linestyle='-',
                         linewidth=1.5)
    circle6 = plt.Circle((0, 0), 1.5, transform=ax.transData._b, facecolor=(0, 0, 0, 0), edgecolor='grey',
                         linestyle='--', linewidth=1.0)
    ax.add_artist(circle4)
    ax.add_artist(circle5)
    ax.add_artist(circle6)

    # ax.set_xlabel('Normalized')
    ax.text(np.deg2rad(40), 1.75, s='Correlation', ha='center', va='bottom', rotation=-45)

    # 这里的网格包括：以原点为圆点的圆圈。首先绘制从原点发散的线段，长度等于半径
    ax.plot([0, np.arccos(0.4)], [0, 3], lw=1, color='gray', linestyle='--')
    ax.plot([0, np.arccos(0.8)], [0, 3], lw=1, color='gray', linestyle='--')

    # 画点，参数一相关系数，参数二标准差
    # ax.plot(np.arccos(r[0]), std[0], 'o', color='r', markersize=10, label='2')
    # ax.text(np.arccos(r[0] - 0.05), std[0], s='2', c='r', fontsize=13)  # 标数字，可不要
    #
    # ax.plot(np.arccos(r[1]), std[1], 'o', color='g', markersize=10, label='3')
    # ax.text(np.arccos(r[1] - 0.05), std[1], s='3', c='g', fontsize=13)

    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'orange']  # 定义8种不同的颜色
    markers = ['o', 's', '*', 'D', 'v', '^', '>', 'h']  # 定义8种不同的形状
    # labels = ['数值模型'] + ['智能模型{}'.format(i) for i in range(1, 8)]  # 标签名称
    labels = model

    for i in range(len(r)):
        # 画点，参数一相关系数，参数二标准差
        ax.plot(np.arccos(r[i]), std[i], marker=markers[i], color=colors[i],
                markersize=10,
                label=labels[i]
                )
        # ax.text(np.arccos(r[i] - 0.05), std[i], s=i + 1, c=colors[i], fontsize=13)  # 标数字，可不要

    ax.legend(loc='upper right')
    # ax.set_title(station, fontsize=30)



    ax.set_ylabel('Std (Normalized)', labelpad=32)

def tar2(ax, r, std, model,station):
    # plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文
    # plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    ax.set_thetalim(thetamin=0, thetamax=90)
    r_small, r_big, r_interval = 0, 1.0 + 0.1, 0.5  # 横纵坐标范围，最小值 最大值 间隔
    ax.set_rlim(r_small, r_big)
    rad_list = [0, 0.2, 0.4, 0.6, 0.7, 0.8, 0.85, 0.9, 0.95, 0.99, 1]  # 需要显示数值的主要R的值
    minor_rad_list = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.86, 0.87, 0.88, 0.89,
                      0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1]  # 需要显示刻度的次要R的值
    angle_list = np.rad2deg(np.arccos(rad_list))
    angle_list_rad = np.arccos(rad_list)
    angle_minor_list = np.arccos(minor_rad_list)
    ax.set_thetagrids(angle_list, rad_list)
    for i in np.arange(r_small, r_big, r_interval):
        if i == 1:
            ax.text(0, i, s='\n' + 'REF', ha='center', va='top')
            # text的第一个坐标是角度（弧度制），第二个是距离
        else:
            ax.text(0, i, s='\n' + str(i), ha='center', va='top')
        ax.text(np.pi / 2, i, s=str(i) + '  ', ha='right', va='center')
    ax.set_rgrids([])
    labels = ax.get_xticklabels() + ax.get_yticklabels()
    ax.grid(False)
    angle_linewidth, angle_length, angle_minor_length = 0.8, 0.02, 0.01
    tick = [ax.get_rmax(), ax.get_rmax() * (1 - angle_length)]
    tick_minor = [ax.get_rmax(), ax.get_rmax() * (1 - angle_minor_length)]
    for t in angle_list_rad:
        ax.plot([t, t], tick, lw=angle_linewidth, color="k")  # 第一个坐标是角度（角度制），第二个是距离
    for t in angle_minor_list:
        ax.plot([t, t], tick_minor, lw=angle_linewidth, color="k")  # 第一个坐标是角度（角度制），第二个是距离

    # 然后开始绘制以REF为原点的圈，可以自己加圈
    circle = plt.Circle((1, 0), 0.25, transform=ax.transData._b, facecolor=(0, 0, 0, 0), edgecolor='gray',linestyle='--', linewidth=0.8)
    ax.add_artist(circle)

    # 绘制以原点为圆点的圆圈：
    circle4 = plt.Circle((0, 0), 0.5, transform=ax.transData._b, facecolor=(0, 0, 0, 0), edgecolor='grey',
                         linestyle='--', linewidth=1.0)
    circle5 = plt.Circle((0, 0), 1, transform=ax.transData._b, facecolor=(0, 0, 0, 0), edgecolor='grey', linestyle='-',
                         linewidth=1.5)
    circle6 = plt.Circle((0, 0), 1.5, transform=ax.transData._b, facecolor=(0, 0, 0, 0), edgecolor='grey',
                         linestyle='--', linewidth=1.0)
    ax.add_artist(circle4)
    ax.add_artist(circle5)
    ax.add_artist(circle6)

    # ax.set_xlabel('Normalized')
    ax.text(np.deg2rad(40), 1.75, s='Correlation', ha='center', va='bottom', rotation=-45)

    # 这里的网格包括：以原点为圆点的圆圈。首先绘制从原点发散的线段，长度等于半径
    ax.plot([0, np.arccos(0.4)], [0, 3], lw=1, color='gray', linestyle='--')
    ax.plot([0, np.arccos(0.8)], [0, 3], lw=1, color='gray', linestyle='--')

    # 画点，参数一相关系数，参数二标准差
    # ax.plot(np.arccos(r[0]), std[0], 'o', color='r', markersize=10, label='2')
    # ax.text(np.arccos(r[0] - 0.05), std[0], s='2', c='r', fontsize=13)  # 标数字，可不要
    #
    # ax.plot(np.arccos(r[1]), std[1], 'o', color='g', markersize=10, label='3')
    # ax.text(np.arccos(r[1] - 0.05), std[1], s='3', c='g', fontsize=13)

    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'orange']  # 定义8种不同的颜色
    markers = ['o', 's', '*', 'D', 'v', '^', '>', 'h']  # 定义8种不同的形状
    # labels = ['数值模型'] + ['智能模型{}'.format(i) for i in range(1, 8)]  # 标签名称
    labels = model

    for i in range(len(r)):
        # 画点，参数一相关系数，参数二标准差
        ax.plot(np.arccos(r[i]), std[i], marker=markers[i], color=colors[i],
                markersize=10,
                label=labels[i]
                )
        # ax.text(np.arccos(r[i] - 0.05), std[i], s=i + 1, c=colors[i], fontsize=13)  # 标数字，可不要

    ax.legend(loc='upper right')
    ax.set_title(station, fontsize=40)



    ax.set_ylabel('Std (Normalized)', labelpad=32)
# def sandian_v2(file,stations=[ '北礵',  '同心湾2号','姥屿','榕海Ⅳ号','港南','湄洲岛', '筶杯岛', '闽江口1号', '鸟屿'],x="mod"):
#
#     # salinity = df["attention_group_swish/attention_lyr1_8"]  # 盐度
#
#     plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文
#     plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
#
#     # 创建图形
#     fig = plt.figure(figsize=(48, 32), dpi=300)
#
#     i=0
#
#     for station in stations:
#         df = pd.read_excel(file, sheet_name=station, engine='openpyxl')
#
#         time = df["时间"]  # 时间
#         obs = df["观察值"]  # 溶解氧
#         pred = df[x]  # 叶绿素
#
#         # 绘制时序图
#         ax = fig.add_subplot(3, 3, i + 1)  # 添加子图
#         ax.scatter(time, obs, label="obs")  # 溶解氧
#         ax.scatter(time, pred, label=x)  # 叶绿素
#         # ax.scatter(time, salinity, label="attention_lyr1_8")  # 盐度
#
#         # 设置图例和标签
#         ax.legend(fontsize=28)
#         ax.set_xlabel("Time")
#         ax.set_ylabel("Value")
#
#         ax.set_title(station, fontsize=38)
#
#         i=i+1
#
#     fig.suptitle(f"模型：{x}", fontsize=48)
#
#     # save_dir=f"picture/{station}/"+x
#     # save_dir = "picture/" + x + f'/{station}'
#     save_dir = "picture/" + x
#
#     if not os.path.exists(save_dir):
#         os.makedirs(save_dir)
#
#     # # 保存为矢量图 (SVG格式)
#     plt.savefig(save_dir + '.svg',format='svg', bbox_inches="tight", dpi=300)
#     #
#     # # 保存为矢量图 (PDF格式)
#     # plt.savefig("timeseries.pdf", format='pdf')
#
#     # 显示图形
#     # plt.show()
#     plt.close()
#     print(save_dir + ".svg___saved!")
#
# # def sandian_v3(file,stations=[ '北礵',  '同心湾2号','姥屿','榕海Ⅳ号','港南','湄洲岛', '筶杯岛', '闽江口1号', '鸟屿'],x="mod"):
# #
# #
# #     plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文
# #     plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# #
# #     # 创建图形
# #     fig = plt.figure(figsize=(48, 32), dpi=300)
# #
# #     mo_dict = {'attention_group_swish/attention_lyr1_8':'智能模型1',
# #                'attention_group_swish/attention_val_E32_lyr16':'智能模型2',
# #     'attention_group_swish/attention_val_E32_lyr16_8':'智能模型3',
# #     'attention_group_swish/attention_val_E64_lyr32':'智能模型4',
# #     'attention_group_swish/attention_val_E64_lyr32_16':'智能模型5',
# #     'attention_group_swish/attention_val_E64_lyr32_16_8':'智能模型6',
# #     'attention_group_swish/attention_val_lyr1_8':'智能模型7',
# #                'mod':'数值模型'
# #     }
# #
# #     i=0
# #
# #     for station in stations:
# #         df = pd.read_excel(file, sheet_name=station, engine='openpyxl')
# #
# #         # time = df["时间"]  # 时间
# #         obs = df["观察值"]  # 溶解氧
# #         pred = df[x]  # 叶绿素
# #
# #         # 绘制时序图
# #         ax = fig.add_subplot(3, 3, i + 1)  # 添加子图
# #         # ax.scatter(time, obs, label="obs")  # 溶解氧
# #         ax.scatter(obs, pred, label=mo_dict[x])  # 叶绿素
# #         # ax.scatter(time, salinity, label="attention_lyr1_8")  # 盐度
# #
# #         # z = np.polyfit(obs, pred, 1)
# #         # p = np.poly1d(z)
# #         ax.plot(obs, obs, "r--")
# #
# #         # 设置图例和标签
# #         ax.legend(fontsize=28)
# #         ax.set_xlabel("Time")
# #         ax.set_ylabel("Value")
# #
# #         ax.set_title(station, fontsize=38)
# #
# #         i=i+1
# #
# #     fig.suptitle(f"{mo_dict[x]}", fontsize=48)
# #
# #     # save_dir=f"picture/{station}/"+x
# #     # save_dir = "picture/" + x + f'/{station}'
# #     save_dir = "picture/sandian/" + x
# #
# #     if not os.path.exists(save_dir):
# #         os.makedirs(save_dir)
# #
# #     # # 保存为矢量图 (SVG格式)
# #     plt.savefig(save_dir + '.png',format='png', bbox_inches="tight", dpi=300)
# #     #
# #     # # 保存为矢量图 (PDF格式)
# #     # plt.savefig("timeseries.pdf", format='pdf')
# #
# #     # 显示图形
# #     # plt.show()
# #     plt.close()
# #     print(save_dir + ".svg___saved!")
#
# # def sandian_v4(file,stations=[ '北礵',  '同心湾2号','姥屿','榕海Ⅳ号','港南','湄洲岛', '筶杯岛', '闽江口1号', '鸟屿'],x="mod"):
# #
# #     # salinity = df["attention_group_swish/attention_lyr1_8"]  # 盐度
# #
# #     plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文
# #     plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# #
# #     # 创建图形
# #     fig = plt.figure(figsize=(48, 32), dpi=300)
# #
# #     mo_dict = {'attention_group_swish/attention_lyr1_8': '智能模型6',
# #                'attention_group_swish/attention_val_E32_lyr16': '智能模型1',
# #                'attention_group_swish/attention_val_E32_lyr16_8': '智能模型2',
# #                'attention_group_swish/attention_val_E64_lyr32': '智能模型3',
# #                'attention_group_swish/attention_val_E64_lyr32_16': '智能模型4',
# #                'attention_group_swish/attention_val_E64_lyr32_16_8': '智能模型5',
# #                'attention_group_swish/attention_val_lyr1_8': '智能模型7',
# #
# #                'mod': '数值模型'
# #                }
# #
# #     i=0
# #
# #     for station in stations:
# #         df = pd.read_excel(file, sheet_name=station, engine='openpyxl')
# #
# #         # time = df["时间"]  # 时间
# #         obs = df["观察值"]  # 溶解氧
# #         pred = df[x]
# #
# #
# #         # 绘制时序图
# #         ax = fig.add_subplot(3, 3, i + 1)  # 添加子图
# #         ax.scatter(obs, obs, label="obs")  # 溶解氧
# #         ax.scatter(obs, pred, label=mo_dict[x])  # 叶绿素
# #         # ax.scatter(time, salinity, label="attention_lyr1_8")  # 盐度
# #
# #         # z = np.polyfit(obs, pred, 1)
# #         # p = np.poly1d(z)
# #         ax.plot(obs, obs, "r--")
# #
# #         # 设置图例和标签
# #         ax.legend(fontsize=28)
# #         ax.set_xlabel("Time")
# #         ax.set_ylabel("Value")
# #
# #         ax.set_title(station, fontsize=38)
# #
# #         i=i+1
# #
# #     fig.suptitle(f"{mo_dict[x]}", fontsize=48)
# #
# #     # save_dir=f"picture/{station}/"+x
# #     # save_dir = "picture/" + x + f'/{station}'
# #     save_dir = "picture/sandian/" + x
# #
# #     if not os.path.exists(save_dir):
# #         os.makedirs(save_dir)
# #
# #     # # 保存为矢量图 (SVG格式)
# #     plt.savefig(save_dir + '.png',format='png', bbox_inches="tight", dpi=300)
# #     #
# #     # # 保存为矢量图 (PDF格式)
# #     # plt.savefig("timeseries.pdf", format='pdf')
# #
# #     # 显示图形
# #     # plt.show()
# #     plt.close()
# #     print(save_dir + ".svg___saved!")