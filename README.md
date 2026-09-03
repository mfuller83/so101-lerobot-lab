# SO-101 LeRobot Lab
My SO-101 LeRobot project: hardware build, cameras, data collection, policy training, and robotics experiments.

## Summary
This project is primarily a learning exercise in deep learning and its application to robotics. The goal is to build a practical understanding of how modern robot learning systems work by progressing from the physical hardware setup through data collection, imitation learning, simulation, and eventually reinforcement learning.
The first stage of the project will focus on building and commissioning my SO-101 LeRobot setup. This will include assembling the robot, configuring the servos and control system, installing the camera system, and creating a repeatable physical training environment.
Once the hardware is working reliably, the next stage will be to use the Hugging Face LeRobot framework to collect datasets through teleoperation and train initial policies using imitation learning. This should provide a practical introduction to the complete robot-learning pipeline:
Teleoperation → Data Collection → Dataset → Policy Training → Inference → Physical Robot
The exact learning path will develop as the project progresses, but I would eventually like to explore reinforcement learning and simulation. One possible direction is to create a model of the SO-101 in a physics simulator such as MuJoCo, train or optimise policies in simulation, and then transfer those policies to the real robot for final training and refinement.

### This would introduce additional topics such as:
-  Robot kinematics and dynamics
-  Simulation environments
-  Reinforcement learning
-  Reward design
-  Domain randomisation
-  Sim-to-real transfer
-  Vision-based robot control
-  Multi-camera systems

The intention is not simply to build a working robot arm, but to use the project as a platform for understanding how deep learning, computer vision, control systems, simulation, and robotics fit together.

## Project Roadmap

The roadmap is expected to evolve as I learn more, but the current plan is:

1.  Build and commission the SO-101
    -  Assemble the robot
    -  Configure and calibrate the servos
    -  Set up leader/follower teleoperation
    -  Confirm reliable communication and motion
2.  Build the training environment
    -  Construct a repeatable training cell
    -  Install controlled lighting
    -  Install the first fixed camera
    -  Develop adjustable camera and lighting mounts
3.  Collect training data
    -  Record teleoperated demonstrations
    -  Understand the LeRobot dataset structure
    -  Experiment with different tasks and camera positions
4.  Imitation learning
    -  Train an initial policy from demonstrations
    -  Run the trained policy on the physical robot
    -  Evaluate reliability and repeatability
    -  Investigate the effect of dataset size and quality
5.  Expand the vision system
    -  Introduce additional cameras
    -  Compare fixed, wrist-mounted, and multi-camera configurations
    -  Explore how camera placement affects policy performance
6.  Simulation
    -  Create or configure an SO-101 model in MuJoCo
    -  Learn how the robot's joints, limits, actuators, and environment are represented
    -  Reproduce simple physical tasks in simulation
7.  Reinforcement learning
    -  Develop simple reinforcement-learning tasks
    -  Explore reward functions and policy training
    -  Investigate domain randomisation and sim-to-real transfer
    -  Use real-world training or fine-tuning to improve the final policy
