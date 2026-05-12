from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # 1. Gazebo World: Start the environment
        Node(package='gazebo_ros', executable='gzserver', name='gzserver'),
        
        # 2. Robot Description: Spawn the AURA model (URDF/Xacro)
        Node(package='robot_state_publisher', executable='robot_state_publisher', 
             parameters=[{'robot_description': '<xml_of_aura_model>'}]),
             
        # 3. Perception Agent: Start sign language & gaze tracking node
        Node(package='aura_perception', executable='sign_recognizer'),

        # 4. Orchestrator: The brain connecting logic to physics
        Node(package='aura_core', executable='orchestrator_node'),

        # 5. Haptic Sync: Audio to vibration bridge
        Node(package='aura_haptics', executable='haptic_sync_node'),
    ])
