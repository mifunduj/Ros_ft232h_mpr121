#!/usr/bin/env python3
import rospy
from touch_pkg.msg import mpr121Msg
from touch_pkg.msg import mpr121MsgArray
import board
import busio
import time
import adafruit_mpr121
import copy
import numpy as np

def touch():
	pub = rospy.Publisher('mpr121_topic', mpr121MsgArray, queue_size=12)
	rospy.init_node('talk', anonymous=True)
	rate = rospy.Rate(10) # 10hz
	touch_value=0
	ref_value=np.zeros((4,12))
	msg=mpr121MsgArray()
	tM=mpr121Msg()
	i2c=busio.I2C(board.SCL,board.SDA)
	cap1=adafruit_mpr121.MPR121(i2c,0x5A)
	cap2=adafruit_mpr121.MPR121(i2c,0x5B)
	cap3=adafruit_mpr121.MPR121(i2c,0x5C)
	cap4=adafruit_mpr121.MPR121(i2c,0x5D)
	cap=[cap1,cap2,cap3,cap4]
	for j in range(4):
		k=j+1
		print("setting reference values for capteur ", k)
		for i in range(12):
			ref_value[j,i]=cap[j][i].raw_value
	print("reference values set")
	while not rospy.is_shutdown():
		msg.touchSens.clear()
		for j in range(4):
			for i in range(12):
				tM.val_raw=cap[j][i].raw_value
				delta=ref_value[j,i]-tM.val_raw
				if (delta>10):				
					tM.touchval=True
				else :
					tM.touchval=False
				tM.channel_id=i
				tM.sensor_id=j+1
				msg.touchSens.append(copy.copy(tM))
		rospy.loginfo(msg.touchSens)
		pub.publish(msg)
		rate.sleep()
if __name__ == '__main__':
    try:
        touch()
    except rospy.ROSInterruptException:
        pass
