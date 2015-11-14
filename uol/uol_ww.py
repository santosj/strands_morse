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
chair0 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair0.properties(Object = True, Type = 'Chair0')
chair0.translate(x=7.38, y=11.63, z=0.0)
chair0.rotate(x= 0.0, y=0.0, z=1.57)

chair1 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair1.properties(Object = True, Type = 'Chair1')
chair1.translate(x=7.38, y=10.09, z=0.0)
chair1.rotate(x= 0.0, y=0.0, z=1.57)

chair2 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair2.properties(Object = True, Type = 'Chair2')
chair2.translate(x=7.38, y=8.93, z=0.0)
chair2.rotate(x= 0.0, y=0.0, z=1.57)

chair3 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair3.properties(Object = True, Type = 'Chair3')
chair3.translate(x=8.10, y=4.64, z=0.0)
chair3.rotate(x= 0.0, y=0.0, z=1.57)

chair4 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair4.properties(Object = True, Type = 'Chair4')
chair4.translate(x=8.10, y=2.67, z=0.0)
chair4.rotate(x= 0.0, y=0.0, z=1.57)

chair5 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair5.properties(Object = True, Type = 'Chair5')
chair5.translate(x=5.87, y=11.62, z=0.0)
chair5.rotate(x= 0.0, y=0.0, z=-1.57)

chair6 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair6.properties(Object = True, Type = 'Chair6')
chair6.translate(x=5.87, y=10.02, z=0.0)
chair6.rotate(x= 0.0, y=0.0, z=-1.57)

chair7 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair7.properties(Object = True, Type = 'Chair7')
chair7.translate(x=5.87, y=8.42, z=0.0)
chair7.rotate(x= 0.0, y=0.0, z=-1.57)

chair8 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair8.properties(Object = True, Type = 'Chair8')
chair8.translate(x=6.56, y=4.21, z=0.0)
chair8.rotate(x= 0.0, y=0.0, z=-1.57)

chair9 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair9.properties(Object = True, Type = 'Chair9')
chair9.translate(x=6.56, y=2.6, z=0.0)
chair9.rotate(x= 0.0, y=0.0, z=-1.57)

chair10 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair10.properties(Object = True, Type = 'Chair10')
chair10.translate(x=3.52, y=11.62, z=0.0)
chair10.rotate(x= 0.0, y=0.0, z=1.57)

chair11 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair11.properties(Object = True, Type = 'Chair11')
chair11.translate(x=3.52, y=10.49, z=0.0)
chair11.rotate(x= 0.0, y=0.0, z=1.57)

chair12 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair12.properties(Object = True, Type = 'Chair12')
chair12.translate(x=3.52, y=8.46, z=0.0)
chair12.rotate(x= 0.0, y=0.0, z=1.57)

chair13 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair13.properties(Object = True, Type = 'Chair13')
chair13.translate(x=3.20, y=4.70, z=0.0)
chair13.rotate(x= 0.0, y=0.0, z=1.57)

chair14 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair14.properties(Object = True, Type = 'Chair14')
chair14.translate(x=3.20, y=2.69, z=0.0)
chair14.rotate(x= 0.0, y=0.0, z=1.57)

chair15 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair15.properties(Object = True, Type = 'Chair15')
chair15.translate(x=2.12, y=12.09, z=0.0)
chair15.rotate(x= 0.0, y=0.0, z=-1.57)

chair16 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair16.properties(Object = True, Type = 'Chair16')
chair16.translate(x=2.12, y=10.41, z=0.0)
chair16.rotate(x= 0.0, y=0.0, z=-1.57)

chair17 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair17.properties(Object = True, Type = 'Chair17')
chair17.translate(x=2.12, y=8.93, z=0.0)
chair17.rotate(x= 0.0, y=0.0, z=-1.57)

chair18 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair18.properties(Object = True, Type = 'Chair18')
chair18.translate(x=1.75, y=4.21, z=0.0)
chair18.rotate(x= 0.0, y=0.0, z=-1.57)

chair19 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair19.properties(Object = True, Type = 'Chair19')
chair19.translate(x=1.75, y=2.72, z=0.0)
chair19.rotate(x= 0.0, y=0.0, z=-1.57)

human0 = PassiveObject('uol/data/objects/woman_standing.blend','Woman Standing')
human0.properties(Object = True, Type = 'Human0')
human0.translate(x=1.75, y=2.72, z=0.0)
human0.rotate(x= 0.0, y=0.0, z=-1.57)

human1 = PassiveObject('uol/data/objects/woman_standing.blend','Woman Standing')
human1.properties(Object = True, Type = 'Human1')
human1.translate(x=1.75, y=2.72, z=0.0)
human1.rotate(x= 0.0, y=0.0, z=-1.57)

human2 = PassiveObject('uol/data/objects/woman_standing.blend','Woman Standing')
human2.properties(Object = True, Type = 'Human2')
human2.translate(x=1.75, y=2.72, z=0.0)
human2.rotate(x= 0.0, y=0.0, z=-1.57)

human3 = PassiveObject('uol/data/objects/woman_standing.blend','Woman Standing')
human3.properties(Object = True, Type = 'Human3')
human3.translate(x=1.75, y=2.72, z=0.0)
human3.rotate(x= 0.0, y=0.0, z=-1.57)

human4 = PassiveObject('uol/data/objects/woman_standing.blend','Woman Standing')
human4.properties(Object = True, Type = 'Human4')
human4.translate(x=1.75, y=2.72, z=0.0)
human4.rotate(x= 0.0, y=0.0, z=-1.57)

human5 = PassiveObject('uol/data/objects/woman_standing.blend','Woman Standing')
human5.properties(Object = True, Type = 'Human5')
human5.translate(x=1.75, y=2.72, z=0.0)
human5.rotate(x= 0.0, y=0.0, z=-1.57)

human6 = PassiveObject('uol/data/objects/woman_standing.blend','Woman Standing')
human6.properties(Object = True, Type = 'Human6')
human6.translate(x=1.75, y=2.72, z=0.0)
human6.rotate(x= 0.0, y=0.0, z=-1.57)

human7 = PassiveObject('uol/data/objects/woman_standing.blend','Woman Standing')
human7.properties(Object = True, Type = 'Human7')
human7.translate(x=1.75, y=2.72, z=0.0)
human7.rotate(x= 0.0, y=0.0, z=-1.57)

human8 = PassiveObject('uol/data/objects/woman_standing.blend','Woman Standing')
human8.properties(Object = True, Type = 'Human8')
human8.translate(x=1.75, y=2.72, z=0.0)
human8.rotate(x= 0.0, y=0.0, z=-1.57)

human9 = PassiveObject('uol/data/objects/woman_standing.blend','Woman Standing')
human9.properties(Object = True, Type = 'Human9')
human9.translate(x=1.75, y=2.72, z=0.0)
human9.rotate(x= 0.0, y=0.0, z=-1.57)

human10 = PassiveObject('uol/data/objects/woman_standing.blend','Woman Standing')
human10.properties(Object = True, Type = 'Human10')
human10.translate(x=1.75, y=2.72, z=0.0)
human10.rotate(x= 0.0, y=0.0, z=-1.57)

human11 = PassiveObject('uol/data/objects/woman_standing.blend','Woman Standing')
human11.properties(Object = True, Type = 'Human11')
human11.translate(x=1.75, y=2.72, z=0.0)
human11.rotate(x= 0.0, y=0.0, z=-1.57)

human12 = PassiveObject('uol/data/objects/woman_standing.blend','Woman Standing')
human12.properties(Object = True, Type = 'Human12')
human12.translate(x=1.75, y=2.72, z=0.0)
human12.rotate(x= 0.0, y=0.0, z=-1.57)

human13 = PassiveObject('uol/data/objects/woman_standing.blend','Woman Standing')
human13.properties(Object = True, Type = 'Human13')
human13.translate(x=1.75, y=2.72, z=0.0)
human13.rotate(x= 0.0, y=0.0, z=-1.57)

human14 = PassiveObject('uol/data/objects/woman_standing.blend','Woman Standing')
human14.properties(Object = True, Type = 'Human14')
human14.translate(x=1.75, y=2.72, z=0.0)
human14.rotate(x= 0.0, y=0.0, z=-1.57)

human15 = PassiveObject('uol/data/objects/woman_standing.blend','Woman Standing')
human15.properties(Object = True, Type = 'Human15')
human15.translate(x=1.75, y=2.72, z=0.0)
human15.rotate(x= 0.0, y=0.0, z=-1.57)

human16 = PassiveObject('uol/data/objects/woman_standing.blend','Woman Standing')
human16.properties(Object = True, Type = 'Human16')
human16.translate(x=1.75, y=2.72, z=0.0)
human16.rotate(x= 0.0, y=0.0, z=-1.57)

human17 = PassiveObject('uol/data/objects/woman_standing.blend','Woman Standing')
human17.properties(Object = True, Type = 'Human17')
human17.translate(x=1.75, y=2.72, z=0.0)
human17.rotate(x= 0.0, y=0.0, z=-1.57)

human18 = PassiveObject('uol/data/objects/woman_standing.blend','Woman Standing')
human18.properties(Object = True, Type = 'Human18')
human18.translate(x=1.75, y=2.72, z=0.0)
human18.rotate(x= 0.0, y=0.0, z=-1.57)

human19 = PassiveObject('uol/data/objects/woman_standing.blend','Woman Standing')
human19.properties(Object = True, Type = 'Human19')
human19.translate(x=1.75, y=2.72, z=0.0)
human19.rotate(x= 0.0, y=0.0, z=-1.57)

sitting0 = PassiveObject('uol/data/objects/woman_sitting.blend','Woman Sitting')
sitting0.properties(Object = True, Type = 'sitting0')
sitting0.translate(x=1.75, y=2.72, z=0.0)
sitting0.rotate(x= 0.0, y=0.0, z=-1.57)

sitting1 = PassiveObject('uol/data/objects/woman_sitting.blend','Woman Sitting')
sitting1.properties(Object = True, Type = 'sitting1')
sitting1.translate(x=1.75, y=2.72, z=0.0)
sitting1.rotate(x= 0.0, y=0.0, z=-1.57)

sitting2 = PassiveObject('uol/data/objects/woman_sitting.blend','Woman Sitting')
sitting2.properties(Object = True, Type = 'sitting2')
sitting2.translate(x=1.75, y=2.72, z=0.0)
sitting2.rotate(x= 0.0, y=0.0, z=-1.57)

sitting3 = PassiveObject('uol/data/objects/woman_sitting.blend','Woman Sitting')
sitting3.properties(Object = True, Type = 'sitting3')
sitting3.translate(x=1.75, y=2.72, z=0.0)
sitting3.rotate(x= 0.0, y=0.0, z=-1.57)

sitting4 = PassiveObject('uol/data/objects/woman_sitting.blend','Woman Sitting')
sitting4.properties(Object = True, Type = 'sitting4')
sitting4.translate(x=1.75, y=2.72, z=0.0)
sitting4.rotate(x= 0.0, y=0.0, z=-1.57)

sitting5 = PassiveObject('uol/data/objects/woman_sitting.blend','Woman Sitting')
sitting5.properties(Object = True, Type = 'sitting5')
sitting5.translate(x=1.75, y=2.72, z=0.0)
sitting5.rotate(x= 0.0, y=0.0, z=-1.57)

sitting6 = PassiveObject('uol/data/objects/woman_sitting.blend','Woman Sitting')
sitting6.properties(Object = True, Type = 'sitting6')
sitting6.translate(x=1.75, y=2.72, z=0.0)
sitting6.rotate(x= 0.0, y=0.0, z=-1.57)

sitting7 = PassiveObject('uol/data/objects/woman_sitting.blend','Woman Sitting')
sitting7.properties(Object = True, Type = 'sitting7')
sitting7.translate(x=1.75, y=2.72, z=0.0)
sitting7.rotate(x= 0.0, y=0.0, z=-1.57)

sitting8 = PassiveObject('uol/data/objects/woman_sitting.blend','Woman Sitting')
sitting8.properties(Object = True, Type = 'sitting8')
sitting8.translate(x=1.75, y=2.72, z=0.0)
sitting8.rotate(x= 0.0, y=0.0, z=-1.57)

sitting9 = PassiveObject('uol/data/objects/woman_sitting.blend','Woman Sitting')
sitting9.properties(Object = True, Type = 'sitting9')
sitting9.translate(x=1.75, y=2.72, z=0.0)
sitting9.rotate(x= 0.0, y=0.0, z=-1.57)

sitting10 = PassiveObject('uol/data/objects/woman_sitting.blend','Woman Sitting')
sitting10.properties(Object = True, Type = 'sitting10')
sitting10.translate(x=1.75, y=2.72, z=0.0)
sitting10.rotate(x= 0.0, y=0.0, z=-1.57)

sitting11 = PassiveObject('uol/data/objects/woman_sitting.blend','Woman Sitting')
sitting11.properties(Object = True, Type = 'sitting11')
sitting11.translate(x=1.75, y=2.72, z=0.0)
sitting11.rotate(x= 0.0, y=0.0, z=-1.57)

sitting12 = PassiveObject('uol/data/objects/woman_sitting.blend','Woman Sitting')
sitting12.properties(Object = True, Type = 'sitting12')
sitting12.translate(x=1.75, y=2.72, z=0.0)
sitting12.rotate(x= 0.0, y=0.0, z=-1.57)

sitting13 = PassiveObject('uol/data/objects/woman_sitting.blend','Woman Sitting')
sitting13.properties(Object = True, Type = 'sitting13')
sitting13.translate(x=1.75, y=2.72, z=0.0)
sitting13.rotate(x= 0.0, y=0.0, z=-1.57)

sitting14 = PassiveObject('uol/data/objects/woman_sitting.blend','Woman Sitting')
sitting14.properties(Object = True, Type = 'sitting14')
sitting14.translate(x=1.75, y=2.72, z=0.0)
sitting14.rotate(x= 0.0, y=0.0, z=-1.57)

sitting15 = PassiveObject('uol/data/objects/woman_sitting.blend','Woman Sitting')
sitting15.properties(Object = True, Type = 'sitting15')
sitting15.translate(x=1.75, y=2.72, z=0.0)
sitting15.rotate(x= 0.0, y=0.0, z=-1.57)

sitting16 = PassiveObject('uol/data/objects/woman_sitting.blend','Woman Sitting')
sitting16.properties(Object = True, Type = 'sitting16')
sitting16.translate(x=1.75, y=2.72, z=0.0)
sitting16.rotate(x= 0.0, y=0.0, z=-1.57)

sitting17 = PassiveObject('uol/data/objects/woman_sitting.blend','Woman Sitting')
sitting17.properties(Object = True, Type = 'sitting17')
sitting17.translate(x=1.75, y=2.72, z=0.0)
sitting17.rotate(x= 0.0, y=0.0, z=-1.57)

sitting18 = PassiveObject('uol/data/objects/woman_sitting.blend','Woman Sitting')
sitting18.properties(Object = True, Type = 'sitting18')
sitting18.translate(x=1.75, y=2.72, z=0.0)
sitting18.rotate(x= 0.0, y=0.0, z=-1.57)

sitting19 = PassiveObject('uol/data/objects/woman_sitting.blend','Woman Sitting')
sitting19.properties(Object = True, Type = 'sitting19')
sitting19.translate(x=1.75, y=2.72, z=0.0)
sitting19.rotate(x= 0.0, y=0.0, z=-1.57)

sitting20 = PassiveObject('uol/data/objects/woman_sitting.blend','Woman Sitting')
sitting20.properties(Object = True, Type = 'sitting20')
sitting20.translate(x=1.75, y=2.72, z=0.0)
sitting20.rotate(x= 0.0, y=0.0, z=-1.57)

sitting21 = PassiveObject('uol/data/objects/woman_sitting.blend','Woman Sitting')
sitting21.properties(Object = True, Type = 'sitting21')
sitting21.translate(x=1.75, y=2.72, z=0.0)
sitting21.rotate(x= 0.0, y=0.0, z=-1.57)

sitting22 = PassiveObject('uol/data/objects/woman_sitting.blend','Woman Sitting')
sitting22.properties(Object = True, Type = 'sitting22')
sitting22.translate(x=1.75, y=2.72, z=0.0)
sitting22.rotate(x= 0.0, y=0.0, z=-1.57)

sitting23 = PassiveObject('uol/data/objects/woman_sitting.blend','Woman Sitting')
sitting23.properties(Object = True, Type = 'sitting23')
sitting23.translate(x=1.75, y=2.72, z=0.0)
sitting23.rotate(x= 0.0, y=0.0, z=-1.57)

sitting24 = PassiveObject('uol/data/objects/woman_sitting.blend','Woman Sitting')
sitting24.properties(Object = True, Type = 'sitting24')
sitting24.translate(x=1.75, y=2.72, z=0.0)
sitting24.rotate(x= 0.0, y=0.0, z=-1.57)

sitting25 = PassiveObject('uol/data/objects/woman_sitting.blend','Woman Sitting')
sitting25.properties(Object = True, Type = 'sitting25')
sitting25.translate(x=1.75, y=2.72, z=0.0)
sitting25.rotate(x= 0.0, y=0.0, z=-1.57)

cpdoor0 = PassiveObject('uol/data/objects/TCupDoors.blend','SCupDoors')
cpdoor0.properties(Object = True, Type = 'cupdoor0')
cpdoor0.translate(x=9.7, y=10.9, z=1.0)
cpdoor0.rotate(x= 0.0, y=1.57, z=-1.57)

cpdoor1 = PassiveObject('uol/data/objects/TCupDoors.blend','SCupDoors')
cpdoor1.properties(Object = True, Type = 'cupdoor1')
cpdoor1.translate(x=10.1, y=8.2, z=1.0)
cpdoor1.rotate(x= 0.0, y=1.57, z=-1.57)

cpdoor2 = PassiveObject('uol/data/objects/TCupDoors.blend','SCupDoors')
cpdoor2.properties(Object = True, Type = 'cupdoor2')
cpdoor2.translate(x=10.1, y=5.9, z=1.0)
cpdoor2.rotate(x= 0.0, y=1.57, z=-1.57)

cpdoor3 = PassiveObject('uol/data/objects/TCupDoors.blend','SCupDoors')
cpdoor3.properties(Object = True, Type = 'cupdoor3')
cpdoor3.translate(x=10.1, y=4.9, z=1.0)
cpdoor3.rotate(x= 0.0, y=1.57, z=-1.57)

cpdoor4 = PassiveObject('uol/data/objects/TCupDoors.blend','SCupDoors')
cpdoor4.properties(Object = True, Type = 'cupdoor4')
cpdoor4.translate(x=10.1, y=3.2, z=1.0)
cpdoor4.rotate(x= 0.0, y=1.57, z=-1.57)

cpdoor5 = PassiveObject('uol/data/objects/TCupDoors.blend','SCupDoors')
cpdoor5.properties(Object = True, Type = 'cupdoor5')
cpdoor5.translate(x=10.1, y=2.2, z=1.0)
cpdoor5.rotate(x= 0.0, y=1.57, z=-1.57)

cpdoor6 = PassiveObject('uol/data/objects/SCupDoors.blend','SCupDoors')
cpdoor6.properties(Object = True, Type = 'cupdoor6')
cpdoor6.translate(x=7.1, y=7.5, z=0.5)
cpdoor6.rotate(x= -1.57, y=1.57, z=0.0)

cpdoor7 = PassiveObject('uol/data/objects/SCupDoors.blend','SCupDoors')
cpdoor7.properties(Object = True, Type = 'cupdoor7')
cpdoor7.translate(x=7.8, y=5.7, z=0.5)
cpdoor7.rotate(x= 1.57, y=-1.57, z=0.0)

cpdoor8 = PassiveObject('uol/data/objects/SCupDoors.blend','SCupDoors')
cpdoor8.properties(Object = True, Type = 'cupdoor8')
cpdoor8.translate(x=6.1, y=7.5, z=0.5)
cpdoor8.rotate(x= -1.57, y=1.57, z=0.0)

cpdoor9 = PassiveObject('uol/data/objects/SCupDoors.blend','SCupDoors')
cpdoor9.properties(Object = True, Type = 'cupdoor9')
cpdoor9.translate(x=6.8, y=5.7, z=0.5)
cpdoor9.rotate(x= 1.57, y=-1.57, z=0.0)

cpdoor10 = PassiveObject('uol/data/objects/SCupDoors.blend','SCupDoors')
cpdoor10.properties(Object = True, Type = 'cupdoor10')
cpdoor10.translate(x=3.3, y=7.5, z=0.5)
cpdoor10.rotate(x= -1.57, y=1.57, z=0.0)

cpdoor11 = PassiveObject('uol/data/objects/SCupDoors.blend','SCupDoors')
cpdoor11.properties(Object = True, Type = 'cupdoor11')
cpdoor11.translate(x=3.0, y=5.7, z=0.5)
cpdoor11.rotate(x= 1.57, y=-1.57, z=0.0))

cpdoor12 = PassiveObject('uol/data/objects/SCupDoors.blend','SCupDoors')
cpdoor12.properties(Object = True, Type = 'cupdoor12')
cpdoor12.translate(x=2.3, y=7.5, z=0.5)
cpdoor12.rotate(x= -1.57, y=1.57, z=0.0)

cpdoor13 = PassiveObject('uol/data/objects/SCupDoors.blend','SCupDoors')
cpdoor13.properties(Object = True, Type = 'cupdoor13')
cpdoor13.translate(x=2.0, y=5.7, z=0.5)
cpdoor13.rotate(x= 1.57, y=-1.57, z=0.0)



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
