# Copyright 2018 Open Source Robotics Foundation, Inc.
# Copyright 2019 Samsung Research America
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
import launch_ros.actions
import os
import yaml
from launch.substitutions import EnvironmentVariable, LaunchConfiguration
import pathlib
import launch.actions
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    ekf_file = LaunchConfiguration('ekf_file')

    declare_ekf_file_cmd = DeclareLaunchArgument(
        'ekf_file',
        default_value=os.path.join('/data', 'localization/ekf.yaml'),
        description='Full path to the imu driver file')
    return LaunchDescription([
        declare_ekf_file_cmd,
        launch_ros.actions.Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_filter_node',
            output='screen',
            parameters=[ekf_file],
            remappings=[("odometry/filtered", "odom")]
           ),
])
