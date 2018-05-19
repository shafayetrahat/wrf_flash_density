from mpl_toolkits.basemap import Basemap 
import matplotlib.pyplot as plt
import numpy as np
import string
from netCDF4 import Dataset
import matplotlib.cm as cm
 


v_file = 'VHRFC.nc'
fh = Dataset(v_file, mode='r')
LIS_FRD = fh.variables['VHRFC_LIS_FRD'][:]

map = Basemap(llcrnrlon=86.5,llcrnrlat=20.,urcrnrlon=93.5,urcrnrlat=27.,
             resolution='f',projection='tmerc', lat_0 = 23.5, lon_0 = 90.)

#map.drawmapboundary(fill_color='#afceff')
map.drawcountries(linewidth=0.5)
map.drawrivers(linewidth=0.25, color='#96beff')

#map.fillcontinents(color='#c0edea',lake_color='#96beff')

lons=  np.arange(86.5, 93.5, 0.1)
lats=  np.arange(20., 27.0, 0.1)

bd=fh.variables['VHRFC_LIS_FRD'][580:650,2665:2735]

var=np.array(bd)
#var_f=var.ravel()
X,Y=map(lons,lats) 
x,y = np.meshgrid(X,Y)
plt.contourf(x,y,var,cmap='Wistia')
plt.ylabel('Flash desity rate')
map.colorbar()
plt.gcf().set_size_inches(15,15)


plt.show()
