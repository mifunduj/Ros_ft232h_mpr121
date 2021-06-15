# Ros_ft232h_mpr121
This project provides the necessary package to use up to 4 Mpr121 touch sensors connected to the Ft232h board with Ros

To use that source code you must have ROS version which use python3 or configure yours ([if you use ROS Melodic or earlier](https://dhanoopbhaskar.com/blog/2020-05-07-working-with-python-3-in-ros-kinetic-or-melodic/)) it to allow to work with

##### What you need
* Ft232h board
* 4 mpr121 sensors (you can modifie script to allow the nunber of sensors that you need)
* Install ROS
##### How it works
Each touch sensor have 12 channels and provide:
* Id of sensor that's concerned (called sensor_id)
* Id number of channel that's concerned (called channel_id)
* For the corresponding sensor and channel Id : 
  * Raw touch value (called val_raw)
  * Bool touch value (called touchval)

##### Installation instructions for Ft232h and Mpr121
-----------------------------------------------
the necessary installations are provided by Adafruit
1.  [Install FT232h]( https://learn.adafruit.com/circuitpython-on-any-computer-with-ft232h/linux)
2. sudo pip3 install adafruit-circuitpython-mpr121

##### After installation
------------------
1. Create your workspace
2. You have to do " export BLINKA_FT232H=1 "


   So as not to execute this line every time you want to run your code add it to your devel/setup.bash or your ./bashrc file
