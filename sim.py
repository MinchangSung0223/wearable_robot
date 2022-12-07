import pybullet as p
import time
import pybullet_data
import numpy as np
np.set_printoptions(precision=6, suppress=True)

p.connect(p.GUI)
p.setGravity(0, 0, -9.8)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
wearable = p.loadURDF("wearable.urdf", [0, 0, 0.0],[0, 0, 0, 1])
while p.isConnected():


	p.stepSimulation()
	time.sleep(0.01);
