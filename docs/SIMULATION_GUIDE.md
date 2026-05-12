# AURA Simulation Guide (ROS 2 & Gazebo)

To visualize AURA’s multi-agent coordination and safety features, we use a high-fidelity physics simulation. This allows us to test the "Soft-Touch" eSkin and active balancing logic before physical prototyping.

### 1. Prerequisites
- **OS:** Ubuntu 22.04 LTS (Jammy Jellyfish)
- **Middleware:** [ROS 2 Humble Hawksbill](https://ros.org)
- **Simulator:** Gazebo Sim (Ignition)
- **Bridge:** [ros_gz_bridge](https://github.com/gazebosim/ros_gz) to connect ROS 2 topics with Gazebo.

### 2. Launching the Simulation
```bash
# Source the ROS 2 environment
source /opt/ros/humble/setup.bash

# Build the workspace
colcon build --symlink-install
source install/setup.bash

# Launch the AURA world (Rehab Room)
ros2 launch aura_description aura_sim.launch.py
```

### 3. Simulation Scenarios
- **Scenario A (Fall Prevention):** A virtual human model tilts at 20°. The **Kinematic Agent** triggers electromagnetic brakes.
- **Scenario B (AR Interaction):** Visualizes the floor projection turning into a virtual forest as the robot moves.
