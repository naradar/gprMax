from pathlib import Path

import gprMax

fn = Path(__file__)

title = gprMax.Title(name=fn.with_suffix('').name)
domain = gprMax.Domain(p1=(0.240,0.210,0.002))
dxdydz = gprMax.Discretisation(p1=(0.002, 0.002, 0.002))
time_window = gprMax.TimeWindow(time=3e-9)

half_space = gprMax.Material(er=6, se=0, mr=1, sm=0, id='half_space')

waveform = gprMax.Waveform(wave_type='ricker', amp=1, freq=1.5e9, id='my_ricker')

dipole = gprMax.HertzianDipole(polarisation='z', p1=(0.040, 0.170, 0), waveform_id='my_ricker')

rx = gprMax.Rx(p1=(0.080, 0.170, 0))

srcSteps = gprMax.SrcSteps(p1=(0.002, 0, 0))
rxSteps = gprMax.RxSteps(p1=(0.002, 0, 0))

#box = gprMax.Box(p1=(0, 0, 0), p2=(0.240, 0.170, 0.002), material_id='half_space')

box = gprMax.GeometryObjectsRead(p1=(0,0,0), 
    geofile='/home/johnathan/devel/naradar/pointCloud/gprMax/user_libs/test.hdf5' , 
    matfile='/home/johnathan/devel/naradar/pointCloud/gprMax/user_models/materials.txt')

gv = gprMax.GeometryView(p1=(0, 0, 0),
                         p2=(0.240, 0.210 , 0.002),
                         dl=(0.002, 0.002, 0.002),
                         filename=fn.with_suffix('').name,
                         output_type='n')

cylinder = gprMax.Cylinder(p1=(0.120, 0.080, 0), p2=(0.120, 0.080, 0.002), r=0.010, material_id='pec')

scenes = []
for i in range(60):
    scene = gprMax.Scene()
    # add the simulation objects to the scene
    scene.add(title)
    scene.add(domain)
    scene.add(dxdydz)
    scene.add(time_window)
    scene.add(waveform)
    scene.add(dipole)
    scene.add(rx)

    scene.add(srcSteps)
    scene.add(rxSteps)

    scene.add(half_space)

    scene.add(box)
    scene.add(cylinder)

   # scene.add(gv)

    scenes.append(scene)

# run the simulation (b-scan)
gprMax.run(scenes=scenes, geometry_only=False, n=60, outputfile=fn)

#gprMax.run(scenes=scenes, geometry_only=True, n=1, outputfile=fn)