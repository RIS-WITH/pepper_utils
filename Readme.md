# Pepper utils

## Install the required packages


#### On your computer

First, install the following packages in your catkin workspace:

```bash
git clone https://github.com/ros-naoqi/naoqi_bridge.git
git clone https://github.com/OctoMap/octomap_msgs.git
git clone https://github.com/ros-naoqi/naoqi_driver.git 
git clone https://github.com/ros-naoqi/naoqi_bridge_msgs.git 
git clone -b melodic-devel https://github.com/ros-naoqi/libqi.git 
git clone -b melodic-devel https://github.com/ros-naoqi/libqicore.git 
```

Then clone the following in your workspace:

```bash
git clone https://github.com/ros-naoqi/pepper_meshes
```

Before compiling everything, run:

```bash
catkin_make pepper_meshes_meshes
```

This will create a `mesh` folder in your workspace in `devel/tmp/meshes/1.0/`. Copy the `mesh` folder in the `pepper_meshes` ROS package using the `mv` command.

You can now compile the entire workspace.

#### On pepper

The current package should be installed on pepper nvidia computer in the same workspace than the realsense package.

## Setup your environment

We advise you to create a `setup.sh` file in your workspace. In there, paste the following:

```bash
export MYIP="$(ip route get 1.2.3.4 | awk '{print $7}')"
export MYINTERFACE="$(ip route get 1.2.3.4 | awk '{print $5}')"
export ROS_MASTER_URI=http://$MYIP:11311
export PYTHONPATH=${PYTHONPATH}:/usr/local/robots/pepper/pynaoqi-python2.7-2.5.7.1-linux64/lib/python2.7/site-packages/
```

Go in the `src/naoqi_driver/share/boot_config.json` file and set the audio to `false`.

## Launching the robot

On your computer you can simply launch:

```bash
roslaunch naoqi_driver naoqi_driver.launch nao_ip:=mummer6.laas.fr roscore_ip:=$MYIP network_interface:=$MYINTERFACE 
```

Then on the nvidia device in the realsence workspace launch:

```bash
roslaunch pepper_utils realsense.launch
```

> Do not forgot to export the ROS_MASTER_URI env variable !

The robot is ready! You can use the `strat.py` script to desactivate default pepper features like the artificial life if you need to.