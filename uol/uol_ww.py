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
chair0.properties(Object = True, Type = 'chair0')
chair0.translate(x=7.38, y=11.63, z=0.0)
chair0.rotate(x= 0.0, y=0.0, z=1.57)

chair1 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair1.properties(Object = True, Type = 'chair1')
chair1.translate(x=7.38, y=10.09, z=0.0)
chair1.rotate(x= 0.0, y=0.0, z=1.57)

chair2 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair2.properties(Object = True, Type = 'chair2')
chair2.translate(x=7.38, y=8.93, z=0.0)
chair2.rotate(x= 0.0, y=0.0, z=1.57)

chair3 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair3.properties(Object = True, Type = 'chair3')
chair3.translate(x=8.10, y=4.64, z=0.0)
chair3.rotate(x= 0.0, y=0.0, z=1.57)

chair4 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair4.properties(Object = True, Type = 'chair4')
chair4.translate(x=8.10, y=2.67, z=0.0)
chair4.rotate(x= 0.0, y=0.0, z=1.57)

chair5 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair5.properties(Object = True, Type = 'chair5')
chair5.translate(x=5.87, y=11.62, z=0.0)
chair5.rotate(x= 0.0, y=0.0, z=-1.57)

chair6 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair6.properties(Object = True, Type = 'chair6')
chair6.translate(x=5.87, y=10.02, z=0.0)
chair6.rotate(x= 0.0, y=0.0, z=-1.57)

chair7 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair7.properties(Object = True, Type = 'chair7')
chair7.translate(x=5.87, y=8.42, z=0.0)
chair7.rotate(x= 0.0, y=0.0, z=-1.57)

chair8 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair8.properties(Object = True, Type = 'chair8')
chair8.translate(x=6.56, y=4.21, z=0.0)
chair8.rotate(x= 0.0, y=0.0, z=-1.57)

chair9 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair9.properties(Object = True, Type = 'chair9')
chair9.translate(x=6.56, y=2.6, z=0.0)
chair9.rotate(x= 0.0, y=0.0, z=-1.57)

chair10 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair10.properties(Object = True, Type = 'chair10')
chair10.translate(x=3.52, y=11.62, z=0.0)
chair10.rotate(x= 0.0, y=0.0, z=1.57)

chair11 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair11.properties(Object = True, Type = 'chair11')
chair11.translate(x=3.52, y=10.49, z=0.0)
chair11.rotate(x= 0.0, y=0.0, z=1.57)

chair12 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair12.properties(Object = True, Type = 'chair12')
chair12.translate(x=3.52, y=8.46, z=0.0)
chair12.rotate(x= 0.0, y=0.0, z=1.57)

chair13 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair13.properties(Object = True, Type = 'chair13')
chair13.translate(x=3.20, y=4.70, z=0.0)
chair13.rotate(x= 0.0, y=0.0, z=1.57)

chair14 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair14.properties(Object = True, Type = 'chair14')
chair14.translate(x=3.20, y=2.69, z=0.0)
chair14.rotate(x= 0.0, y=0.0, z=1.57)

chair15 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair15.properties(Object = True, Type = 'chair15')
chair15.translate(x=2.12, y=12.09, z=0.0)
chair15.rotate(x= 0.0, y=0.0, z=-1.57)

chair16 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair16.properties(Object = True, Type = 'chair16')
chair16.translate(x=2.12, y=10.41, z=0.0)
chair16.rotate(x= 0.0, y=0.0, z=-1.57)

chair17 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair17.properties(Object = True, Type = 'chair17')
chair17.translate(x=2.12, y=8.93, z=0.0)
chair17.rotate(x= 0.0, y=0.0, z=-1.57)

chair18 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair18.properties(Object = True, Type = 'chair18')
chair18.translate(x=1.75, y=4.21, z=0.0)
chair18.rotate(x= 0.0, y=0.0, z=-1.57)

chair19 = PassiveObject('uol/data/objects/OfficeChair.blend','Chair')
chair19.properties(Object = True, Type = 'chair19')
chair19.translate(x=1.75, y=2.72, z=0.0)
chair19.rotate(x= 0.0, y=0.0, z=-1.57)

human0 = PassiveObject('uol/data/objects/woman_standing2.blend','wsyF')
human0.properties(Object = True, Type = 'human0')
human0.translate(x=1.75, y=2.72, z=0.0)
human0.rotate(x= 0.0, y=0.0, z=-1.57)

human1 = PassiveObject('uol/data/objects/woman_standing2.blend','wsyF')
human1.properties(Object = True, Type = 'human1')
human1.translate(x=1.75, y=2.72, z=0.0)
human1.rotate(x= 0.0, y=0.0, z=-1.57)

human2 = PassiveObject('uol/data/objects/woman_standing2.blend','wsyF')
human2.properties(Object = True, Type = 'human2')
human2.translate(x=1.75, y=2.72, z=0.0)
human2.rotate(x= 0.0, y=0.0, z=-1.57)

human3 = PassiveObject('uol/data/objects/woman_standing2.blend','wsyF')
human3.properties(Object = True, Type = 'human3')
human3.translate(x=1.75, y=2.72, z=0.0)
human3.rotate(x= 0.0, y=0.0, z=-1.57)

human4 = PassiveObject('uol/data/objects/woman_standing2.blend','wsyF')
human4.properties(Object = True, Type = 'human4')
human4.translate(x=1.75, y=2.72, z=0.0)
human4.rotate(x= 0.0, y=0.0, z=-1.57)

human5 = PassiveObject('uol/data/objects/woman_standing2.blend','wsyF')
human5.properties(Object = True, Type = 'human5')
human5.translate(x=1.75, y=2.72, z=0.0)
human5.rotate(x= 0.0, y=0.0, z=-1.57)

human6 = PassiveObject('uol/data/objects/woman_standing2.blend','wsyF')
human6.properties(Object = True, Type = 'human6')
human6.translate(x=1.75, y=2.72, z=0.0)
human6.rotate(x= 0.0, y=0.0, z=-1.57)

human7 = PassiveObject('uol/data/objects/woman_standing2.blend','wsyF')
human7.properties(Object = True, Type = 'human7')
human7.translate(x=1.75, y=2.72, z=0.0)
human7.rotate(x= 0.0, y=0.0, z=-1.57)

human8 = PassiveObject('uol/data/objects/woman_standing2.blend','wsyF')
human8.properties(Object = True, Type = 'human8')
human8.translate(x=1.75, y=2.72, z=0.0)
human8.rotate(x= 0.0, y=0.0, z=-1.57)

human9 = PassiveObject('uol/data/objects/woman_standing2.blend','wsyF')
human9.properties(Object = True, Type = 'human9')
human9.translate(x=1.75, y=2.72, z=0.0)
human9.rotate(x= 0.0, y=0.0, z=-1.57)

human10 = PassiveObject('uol/data/objects/woman_standing2.blend','wsyF')
human10.properties(Object = True, Type = 'human10')
human10.translate(x=1.75, y=2.72, z=0.0)
human10.rotate(x= 0.0, y=0.0, z=-1.57)

human11 = PassiveObject('uol/data/objects/woman_standing2.blend','wsyF')
human11.properties(Object = True, Type = 'human11')
human11.translate(x=1.75, y=2.72, z=0.0)
human11.rotate(x= 0.0, y=0.0, z=-1.57)

human12 = PassiveObject('uol/data/objects/woman_standing2.blend','wsyF')
human12.properties(Object = True, Type = 'human12')
human12.translate(x=1.75, y=2.72, z=0.0)
human12.rotate(x= 0.0, y=0.0, z=-1.57)

human13 = PassiveObject('uol/data/objects/woman_standing2.blend','wsyF')
human13.properties(Object = True, Type = 'human13')
human13.translate(x=1.75, y=2.72, z=0.0)
human13.rotate(x= 0.0, y=0.0, z=-1.57)

human14 = PassiveObject('uol/data/objects/woman_standing2.blend','wsyF')
human14.properties(Object = True, Type = 'human14')
human14.translate(x=1.75, y=2.72, z=0.0)
human14.rotate(x= 0.0, y=0.0, z=-1.57)

human15 = PassiveObject('uol/data/objects/woman_standing2.blend','wsyF')
human15.properties(Object = True, Type = 'human15')
human15.translate(x=1.75, y=2.72, z=0.0)
human15.rotate(x= 0.0, y=0.0, z=-1.57)

human16 = PassiveObject('uol/data/objects/woman_standing2.blend','wsyF')
human16.properties(Object = True, Type = 'human16')
human16.translate(x=1.75, y=2.72, z=0.0)
human16.rotate(x= 0.0, y=0.0, z=-1.57)

human17 = PassiveObject('uol/data/objects/woman_standing2.blend','wsyF')
human17.properties(Object = True, Type = 'human17')
human17.translate(x=1.75, y=2.72, z=0.0)
human17.rotate(x= 0.0, y=0.0, z=-1.57)

human18 = PassiveObject('uol/data/objects/woman_standing2.blend','wsyF')
human18.properties(Object = True, Type = 'human18')
human18.translate(x=1.75, y=2.72, z=0.0)
human18.rotate(x= 0.0, y=0.0, z=-1.57)

human19 = PassiveObject('uol/data/objects/woman_standing2.blend','wsyF')
human19.properties(Object = True, Type = 'human19')
human19.translate(x=1.75, y=2.72, z=0.0)
human19.rotate(x= 0.0, y=0.0, z=-1.57)

sitting0 = PassiveObject('uol/data/objects/woman_sitting2.blend','wyF')
sitting0.properties(Object = True, Type = 'sitting0')
sitting0.translate(x=1.75, y=2.72, z=0.0)
sitting0.rotate(x= 0.0, y=0.0, z=-1.57)

sitting1 = PassiveObject('uol/data/objects/woman_sitting2.blend','wyF')
sitting1.properties(Object = True, Type = 'sitting1')
sitting1.translate(x=1.75, y=2.72, z=0.0)
sitting1.rotate(x= 0.0, y=0.0, z=-1.57)

sitting2 = PassiveObject('uol/data/objects/woman_sitting2.blend','wyF')
sitting2.properties(Object = True, Type = 'sitting2')
sitting2.translate(x=1.75, y=2.72, z=0.0)
sitting2.rotate(x= 0.0, y=0.0, z=-1.57)

sitting3 = PassiveObject('uol/data/objects/woman_sitting2.blend','wyF')
sitting3.properties(Object = True, Type = 'sitting3')
sitting3.translate(x=1.75, y=2.72, z=0.0)
sitting3.rotate(x= 0.0, y=0.0, z=-1.57)

sitting4 = PassiveObject('uol/data/objects/woman_sitting2.blend','wyF')
sitting4.properties(Object = True, Type = 'sitting4')
sitting4.translate(x=1.75, y=2.72, z=0.0)
sitting4.rotate(x= 0.0, y=0.0, z=-1.57)

sitting5 = PassiveObject('uol/data/objects/woman_sitting2.blend','wyF')
sitting5.properties(Object = True, Type = 'sitting5')
sitting5.translate(x=1.75, y=2.72, z=0.0)
sitting5.rotate(x= 0.0, y=0.0, z=-1.57)

sitting6 = PassiveObject('uol/data/objects/woman_sitting2.blend','wyF')
sitting6.properties(Object = True, Type = 'sitting6')
sitting6.translate(x=1.75, y=2.72, z=0.0)
sitting6.rotate(x= 0.0, y=0.0, z=-1.57)

sitting7 = PassiveObject('uol/data/objects/woman_sitting2.blend','wyF')
sitting7.properties(Object = True, Type = 'sitting7')
sitting7.translate(x=1.75, y=2.72, z=0.0)
sitting7.rotate(x= 0.0, y=0.0, z=-1.57)

sitting8 = PassiveObject('uol/data/objects/woman_sitting2.blend','wyF')
sitting8.properties(Object = True, Type = 'sitting8')
sitting8.translate(x=1.75, y=2.72, z=0.0)
sitting8.rotate(x= 0.0, y=0.0, z=-1.57)

sitting9 = PassiveObject('uol/data/objects/woman_sitting2.blend','wyF')
sitting9.properties(Object = True, Type = 'sitting9')
sitting9.translate(x=1.75, y=2.72, z=0.0)
sitting9.rotate(x= 0.0, y=0.0, z=-1.57)

sitting10 = PassiveObject('uol/data/objects/woman_sitting2.blend','wyF')
sitting10.properties(Object = True, Type = 'sitting10')
sitting10.translate(x=1.75, y=2.72, z=0.0)
sitting10.rotate(x= 0.0, y=0.0, z=-1.57)

sitting11 = PassiveObject('uol/data/objects/woman_sitting2.blend','wyF')
sitting11.properties(Object = True, Type = 'sitting11')
sitting11.translate(x=1.75, y=2.72, z=0.0)
sitting11.rotate(x= 0.0, y=0.0, z=-1.57)

sitting12 = PassiveObject('uol/data/objects/woman_sitting2.blend','wyF')
sitting12.properties(Object = True, Type = 'sitting12')
sitting12.translate(x=1.75, y=2.72, z=0.0)
sitting12.rotate(x= 0.0, y=0.0, z=-1.57)

sitting13 = PassiveObject('uol/data/objects/woman_sitting2.blend','wyF')
sitting13.properties(Object = True, Type = 'sitting13')
sitting13.translate(x=1.75, y=2.72, z=0.0)
sitting13.rotate(x= 0.0, y=0.0, z=-1.57)

sitting14 = PassiveObject('uol/data/objects/woman_sitting2.blend','wyF')
sitting14.properties(Object = True, Type = 'sitting14')
sitting14.translate(x=1.75, y=2.72, z=0.0)
sitting14.rotate(x= 0.0, y=0.0, z=-1.57)

sitting15 = PassiveObject('uol/data/objects/woman_sitting2.blend','wyF')
sitting15.properties(Object = True, Type = 'sitting15')
sitting15.translate(x=1.75, y=2.72, z=0.0)
sitting15.rotate(x= 0.0, y=0.0, z=-1.57)

sitting16 = PassiveObject('uol/data/objects/woman_sitting2.blend','wyF')
sitting16.properties(Object = True, Type = 'sitting16')
sitting16.translate(x=1.75, y=2.72, z=0.0)
sitting16.rotate(x= 0.0, y=0.0, z=-1.57)

sitting17 = PassiveObject('uol/data/objects/woman_sitting2.blend','wyF')
sitting17.properties(Object = True, Type = 'sitting17')
sitting17.translate(x=1.75, y=2.72, z=0.0)
sitting17.rotate(x= 0.0, y=0.0, z=-1.57)

sitting18 = PassiveObject('uol/data/objects/woman_sitting2.blend','wyF')
sitting18.properties(Object = True, Type = 'sitting18')
sitting18.translate(x=1.75, y=2.72, z=0.0)
sitting18.rotate(x= 0.0, y=0.0, z=-1.57)

sitting19 = PassiveObject('uol/data/objects/woman_sitting2.blend','wyF')
sitting19.properties(Object = True, Type = 'sitting19')
sitting19.translate(x=1.75, y=2.72, z=0.0)
sitting19.rotate(x= 0.0, y=0.0, z=-1.57)

hsofa0 = PassiveObject('uol/data/objects/woman_sitting2.blend','wyF')
hsofa0.properties(Object = True, Type = 'hsofa0')
hsofa0.translate(x=1.75, y=2.72, z=0.0)
hsofa0.rotate(x= 0.0, y=0.0, z=-1.57)

hsofa1 = PassiveObject('uol/data/objects/woman_sitting2.blend','wyF')
hsofa1.properties(Object = True, Type = 'hsofa1')
hsofa1.translate(x=1.75, y=2.72, z=0.0)
hsofa1.rotate(x= 0.0, y=0.0, z=-1.57)

hsofa2 = PassiveObject('uol/data/objects/woman_sitting2.blend','wyF')
hsofa2.properties(Object = True, Type = 'hsofa2')
hsofa2.translate(x=1.75, y=2.72, z=0.0)
hsofa2.rotate(x= 0.0, y=0.0, z=-1.57)

hsofa3 = PassiveObject('uol/data/objects/woman_sitting2.blend','wyF')
hsofa3.properties(Object = True, Type = 'hsofa3')
hsofa3.translate(x=1.75, y=2.72, z=0.0)
hsofa3.rotate(x= 0.0, y=0.0, z=-1.57)

hsofa4 = PassiveObject('uol/data/objects/woman_sitting2.blend','wyF')
hsofa4.properties(Object = True, Type = 'hsofa4')
hsofa4.translate(x=1.75, y=2.72, z=0.0)
hsofa4.rotate(x= 0.0, y=0.0, z=-1.57)

hsofa5 = PassiveObject('uol/data/objects/woman_sitting2.blend','wyF')
hsofa5.properties(Object = True, Type = 'hsofa5')
hsofa5.translate(x=1.75, y=2.72, z=0.0)
hsofa5.rotate(x= 0.0, y=0.0, z=-1.57)

cpdoor0 = PassiveObject('uol/data/objects/TCupDoors2.blend','TCupDoors')
cpdoor0.properties(Object = True, Type = 'cupdoor0')
cpdoor0.translate(x=9.7, y=10.92, z=1.0)
cpdoor0.rotate(x= 0.0, y=0.0, z=0.0)

cpdoor1 = PassiveObject('uol/data/objects/TCupDoors2.blend','TCupDoors')
cpdoor1.properties(Object = True, Type = 'cupdoor1')
cpdoor1.translate(x=10.15, y=8.25, z=1.0)
cpdoor1.rotate(x= 0.0, y=0.0, z=0.0)

cpdoor2 = PassiveObject('uol/data/objects/TCupDoors2.blend','TCupDoors')
cpdoor2.properties(Object = True, Type = 'cupdoor2')
cpdoor2.translate(x=10.15, y=5.91, z=1.0)
cpdoor2.rotate(x= 0.0, y=0.0, z=0.0)

cpdoor3 = PassiveObject('uol/data/objects/TCupDoors2.blend','TCupDoors')
cpdoor3.properties(Object = True, Type = 'cupdoor3')
cpdoor3.translate(x=10.15, y=4.9, z=1.0)
cpdoor3.rotate(x= 0.0, y=0.0, z=0.0)

cpdoor4 = PassiveObject('uol/data/objects/TCupDoors2.blend','TCupDoors')
cpdoor4.properties(Object = True, Type = 'cupdoor4')
cpdoor4.translate(x=10.15, y=3.21, z=1.0)
cpdoor4.rotate(x= 0.0, y=0.0, z=0.0)

cpdoor5 = PassiveObject('uol/data/objects/TCupDoors2.blend','TCupDoors')
cpdoor5.properties(Object = True, Type = 'cupdoor5')
cpdoor5.translate(x=10.15, y=2.22, z=1.0)
cpdoor5.rotate(x= 0.0, y=0.0, z=0.0)

cpdoor6 = PassiveObject('uol/data/objects/SCupDoors2.blend','SCupDoors')
cpdoor6.properties(Object = True, Type = 'cupdoor6')
cpdoor6.translate(x=7.15, y=7.5, z=0.5)
cpdoor6.rotate(x=0.0, y=0.0, z=1.57)

cpdoor7 = PassiveObject('uol/data/objects/SCupDoors2.blend','SCupDoors')
cpdoor7.properties(Object = True, Type = 'cupdoor7')
cpdoor7.translate(x=7.85, y=5.65, z=0.5)
cpdoor7.rotate(x=0.0, y=0.0, z=1.57)

cpdoor8 = PassiveObject('uol/data/objects/SCupDoors2.blend','SCupDoors')
cpdoor8.properties(Object = True, Type = 'cupdoor8')
cpdoor8.translate(x=6.15, y=7.5, z=0.5)
cpdoor8.rotate(x=0.0, y=0.0, z=1.57)

cpdoor9 = PassiveObject('uol/data/objects/SCupDoors2.blend','SCupDoors')
cpdoor9.properties(Object = True, Type = 'cupdoor9')
cpdoor9.translate(x=6.85, y=5.65, z=0.5)
cpdoor9.rotate(x=0.0, y=0.0, z=1.57)

cpdoor10 = PassiveObject('uol/data/objects/SCupDoors2.blend','SCupDoors')
cpdoor10.properties(Object = True, Type = 'cupdoor10')
cpdoor10.translate(x=3.3, y=7.5, z=0.5)
cpdoor10.rotate(x=0.0, y=0.0, z=1.57)

cpdoor11 = PassiveObject('uol/data/objects/SCupDoors2.blend','SCupDoors')
cpdoor11.properties(Object = True, Type = 'cupdoor11')
cpdoor11.translate(x=2.95, y=5.75, z=0.5)
cpdoor11.rotate(x=0.0, y=0.0, z=1.57)

cpdoor12 = PassiveObject('uol/data/objects/SCupDoors2.blend','SCupDoors')
cpdoor12.properties(Object = True, Type = 'cupdoor12')
cpdoor12.translate(x=2.3, y=7.5, z=0.5)
cpdoor12.rotate(x=0.0, y=0.0, z=1.57)

cpdoor13 = PassiveObject('uol/data/objects/SCupDoors2.blend','SCupDoors')
cpdoor13.properties(Object = True, Type = 'cupdoor13')
cpdoor13.translate(x=1.95, y=5.75, z=0.5)
cpdoor13.rotate(x=0.0, y=0.0, z=1.57)



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
