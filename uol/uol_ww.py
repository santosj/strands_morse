#! /usr/bin/env morseexec

""" Basic MORSE simulation scene for <strands_sim> environment

Feel free to edit this template as you like!
"""

from morse.builder import *
from strands_sim.builder.robots import Scitosa5

#robot = Ranger()
robot = Scitosa5(with_cameras=Scitosa5.WITH_OPENNI)

# tum_kitchen
robot.translate(x=10.2, y=7.1, z=0.1)
#robot.translate(x=1, y=7.62, z=0.0)
#robot.rotate(0,0,1.57)

#chairs
chair1 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair1.properties(Object = True, Type = 'Chair1')
chair1.translate(x=7.38, y=11.63, z=0.0)
chair1.rotate(x= 0.0, y=0.0, z=1.57)

chair2 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair2.properties(Object = True, Type = 'Chair2')
chair2.translate(x=7.38, y=10.09, z=0.0)
chair2.rotate(x= 0.0, y=0.0, z=1.57)

chair3 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair3.properties(Object = True, Type = 'Chair3')
chair3.translate(x=7.38, y=8.93, z=0.0)
chair3.rotate(x= 0.0, y=0.0, z=1.57)

chair4 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair4.properties(Object = True, Type = 'Chair4')
chair4.translate(x=8.10, y=4.64, z=0.0)
chair4.rotate(x= 0.0, y=0.0, z=1.57)

chair5 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair5.properties(Object = True, Type = 'Chair5')
chair5.translate(x=8.10, y=2.67, z=0.0)
chair5.rotate(x= 0.0, y=0.0, z=1.57)

chair6 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair6.properties(Object = True, Type = 'Chair6')
chair6.translate(x=5.87, y=11.62, z=0.0)
chair6.rotate(x= 0.0, y=0.0, z=-1.57)

chair7 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair7.properties(Object = True, Type = 'Chair7')
chair7.translate(x=5.87, y=10.02, z=0.0)
chair7.rotate(x= 0.0, y=0.0, z=-1.57)

chair8 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair8.properties(Object = True, Type = 'Chair8')
chair8.translate(x=5.87, y=8.42, z=0.0)
chair8.rotate(x= 0.0, y=0.0, z=-1.57)

chair9 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair9.properties(Object = True, Type = 'Chair9')
chair9.translate(x=6.56, y=4.21, z=0.0)
chair9.rotate(x= 0.0, y=0.0, z=-1.57)

chair10 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair10.properties(Object = True, Type = 'Chair10')
chair10.translate(x=6.56, y=2.6, z=0.0)
chair10.rotate(x= 0.0, y=0.0, z=-1.57)

chair11 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair11.properties(Object = True, Type = 'Chair11')
chair11.translate(x=3.52, y=11.62, z=0.0)
chair11.rotate(x= 0.0, y=0.0, z=1.57)

chair12 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair12.properties(Object = True, Type = 'Chair12')
chair12.translate(x=3.52, y=10.49, z=0.0)
chair12.rotate(x= 0.0, y=0.0, z=1.57)

chair13 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair13.properties(Object = True, Type = 'Chair13')
chair13.translate(x=3.52, y=8.46, z=0.0)
chair13.rotate(x= 0.0, y=0.0, z=1.57)

chair14 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair14.properties(Object = True, Type = 'Chair14')
chair14.translate(x=3.20, y=4.70, z=0.0)
chair14.rotate(x= 0.0, y=0.0, z=1.57)

chair15 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair15.properties(Object = True, Type = 'Chair15')
chair15.translate(x=3.20, y=2.69, z=0.0)
chair15.rotate(x= 0.0, y=0.0, z=1.57)

chair16 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair16.properties(Object = True, Type = 'Chair16')
chair16.translate(x=2.12, y=12.09, z=0.0)
chair16.rotate(x= 0.0, y=0.0, z=-1.57)

chair17 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair17.properties(Object = True, Type = 'Chair17')
chair17.translate(x=2.12, y=10.41, z=0.0)
chair17.rotate(x= 0.0, y=0.0, z=-1.57)

chair18 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair18.properties(Object = True, Type = 'Chair18')
chair18.translate(x=2.12, y=8.93, z=0.0)
chair18.rotate(x= 0.0, y=0.0, z=-1.57)

chair19 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair19.properties(Object = True, Type = 'Chair19')
chair19.translate(x=1.75, y=4.21, z=0.0)
chair19.rotate(x= 0.0, y=0.0, z=-1.57)

chair20 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair20.properties(Object = True, Type = 'Chair20')
chair20.translate(x=1.75, y=2.72, z=0.0)
chair20.rotate(x= 0.0, y=0.0, z=-1.57)


# Battery discharging rate, in percent per seconds
# The bateery state is published to /battery
robot.battery.properties(DischargingRate=0.0)

docking_station = PassiveObject('strands_sim/robots/docking_station.blend','dockingStation')
docking_station.properties(Object = True)
docking_station.properties(ChargingZone = True)
docking_station.translate(10.55,7.1,0.235)
docking_station.rotate(0.0,0,0.0)

docking_station_label = PassiveObject('strands_sim/robots/docking_station_label.blend','dockingStationLabel')
docking_station_label.properties(Object = True)
docking_station_label.translate(10.60,7.1,1.75)
docking_station_label.rotate(1.57,0,-1.57)

# Set the environment
model_file=os.path.join(os.path.dirname(os.path.abspath( __file__ )),'data/ww.blend')
env = Environment(model_file,fastmode=False)
env.aim_camera([1.0470, 0, 0.7854])
