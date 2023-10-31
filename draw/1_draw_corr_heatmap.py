import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import config as gcc
gc = gcc.get_config()

stations = gc.experiment_stations
# 设置使用的字体和字体大小
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['font.size'] = 12

# sheets  = pd.read_excel('processed_threshold_obs_mod_time_datas.xlsx',sheet_name=None)
for station in stations:
    station = station['station']
    df = pd.read_excel('processed_threshold_obs_mod_time_datas.xlsx',sheet_name=station)

    features1 = ['气温', '气压', '叶绿素', '溶解氧']
    # 绘制热力图
    heatmap = sns.heatmap(df[features1].corr(), annot=True,
                cmap=sns.color_palette("Blues", as_cmap=True))
    plt.savefig(f'corr_heatmap/{station}.png',format='png', dpi=300)
    plt.clf()
    print(station+"站点相关系数热力图已生成")