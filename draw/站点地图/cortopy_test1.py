import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import pyferret
import pandas as pd


# df = pd.read_excel('weizhi.xlsx')
lon = [120.34, 119.453333, 119.268222,120.329167,119.7225,119.4855,119.716333,]  # 经度列表
lat = [26.6964, 25.155167, 25.336806,27.079783,25.976667,25.2525,26.140333,]  # 纬度列表

# lon = [120.34, 119.453333]  # 经度列表
# lat = [26.6964, 25.155167]  # 纬度列表
# pyferret.init(arglist=None, enterferret=True)

fig = plt.figure(figsize=(10, 6))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines()  # 绘制海岸线

ax.scatter(lon, lat, color='red', marker='o', transform=ccrs.PlateCarree())

plt.title('Station Locations')
plt.grid()
plt.savefig('station_map.png', dpi=300)
plt.show()
# pyferret.stop()