import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import pandas as pd

# 设置使用的字体和字体大小
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['font.size'] = 12

# 读取数据
df = pd.read_excel('weizhi.xlsx')
lon = df['经度']
lat = df['纬度']
stations = df['名称']

fig = plt.figure(figsize=(10, 6))
ax = plt.axes(projection=ccrs.PlateCarree())


# 添加海岸线
ax.coastlines()

# 添加行政区划边界
province_border = cfeature.NaturalEarthFeature(category='cultural', name='admin_1_states_provinces_lines', scale='50m', facecolor='none', edgecolor='gray')
ax.add_feature(province_border, linewidth=0.8, alpha=0.8)

# 设置经纬度范围
ax.set_extent([118, 122, 24, 28], crs=ccrs.PlateCarree())

ax.scatter(lon, lat, color='red', marker='o', transform=ccrs.PlateCarree())

# 添加网格
ax.gridlines(draw_labels=True, linewidth=0.5, color='gray', alpha=0.5, linestyle='--')

# 添加站点标注
for (station, x, y) in zip(stations, lon, lat):
    ax.text(x + 0.11, y - 0.03, station, transform=ccrs.PlateCarree(),
            fontsize=12, va='top', ha='center')
    # ax.annotate('', xy=(x, y), xytext=(x + 0.15, y - 0.15),
    #             # arrowprops=dict(arrowstyle='-', color='black')
    #             )

# 添加省份标注
ax.text(118.3, 26.5, 'FuJian Province', fontsize=12, transform=ccrs.PlateCarree())

plt.title('Station Locations')
plt.savefig('station_map.png', dpi=300)
plt.show()

# marker
# '.' - 点
# ',' - 像素
# '+' - 加号
# 'x' - 叉号
# 's' - 正方形
# 'd' - 菱形
# '^' - 上三角形
# 'v' - 下三角形
# '|' - 垂直线
# '_' - 水平线