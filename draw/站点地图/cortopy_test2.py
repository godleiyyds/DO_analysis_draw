import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import pandas as pd

# 设置使用的字体和字体大小
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['font.size'] = 12
df = pd.read_excel('weizhi.xlsx')
lon = df['经度']
lat = df['纬度']
stations = df['名称']

fig = plt.figure(figsize=(10, 6))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines()

# 设置经纬度范围
ax.set_extent([110, 120, 20, 30], crs=ccrs.PlateCarree())

# 添加网格
ax.gridlines(draw_labels=True, linewidth=0.5, color='gray', alpha=0.5, linestyle='--')

ax.scatter(lon, lat, color='red', marker='o', transform=ccrs.PlateCarree())

# 添加站点标签
for (station, x, y) in zip(stations, lon, lat):
    ax.text(x, y, station, transform=ccrs.PlateCarree(),
            fontsize=8, va='center', ha='left')

plt.title('Station Locations')
plt.savefig('station_map.png', dpi=300)
plt.show()