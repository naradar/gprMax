
#Spatial discretisation: 0.002 x 0.002 x 0.002m
#Domain size: 0.4 x 0.4 x 0.12m (200 x 200 x 60 = 2.4e+06 cells)
#Resolution of the model along (X,Y,Z) axis is (180, 180, 54)
#Mesh Bounding Box Size 359.000000 359.000000 106.175972

#    vx=discretization[0]*1000 
#    vy=discretization[1]*1000
#    vz=discretization[2]*1000
#
#    +1
# this gives the desired voxel grid size when mesh is in mm

from binvox import read_as_3d_array, read_as_coord_array
import h5py

from pathlib import Path

import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

with open('/home/johnathan/devel/naradar/web-gpr-frontend/data/5bd34986-c81d-4112-94a3-f749dc3f8cc7.obj_256.binvox', 'rb') as f:
    m1 = read_as_3d_array(f)

print("Resolution of the model along (X,Y,Z) axis is",m1.dims, m1.data.shape)

discretization=(0.002, 0.002, 0.002)

mat_index = 2
data = m1.data.astype(int)
with h5py.File('test.hdf5','w') as hdf:
    data[data==0] = -1
    data[data==1] = mat_index
    hdf.create_dataset('data',data=data)
    hdf.attrs['dx_dy_dz']=(discretization[0],discretization[1],discretization[2])

print(data)
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax.voxels(m1.data)
#plt.show()