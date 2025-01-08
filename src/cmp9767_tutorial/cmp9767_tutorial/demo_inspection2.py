#! /usr/bin/env python3
# Copyright 2021 Samsung Research America
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

from copy import deepcopy

from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
import rclpy

"""
Basic stock inspection demo. In this demonstration, the expectation
is that there are cameras or RFID sensors mounted on the robots
collecting information about stock quantity and location.
"""


def main():
    rclpy.init()

    navigator = BasicNavigator()

    # Inspection route, probably read in from a file for a real application
    # from either a map or drive and repeat. (x, y, yaw)
    inspection_route = [
        [-0.49, 1.10, 0.0, 0.0, 0.0, -0.50, 0.86],  #update the points ,, ignore the z orentaion ,, only 6 values.
        [0.42, -1.91, 0.0, 0.0, 0.00, 1.00, 0.01],
        [0.09, -1.88, 0.0, 0.0, 0.99, 0.17, 1.00],
        [-2.89, -0.97, 0.0, 0.0, 0.47, 0.88, 1.00],  
        [-2.10, 0.36, 0.0, 0.0, 1.00, 0.04, 1.00],
        [-4.37, 1.07, 0.0, 0.0, -0.81, 0.58, 1.00],
        [-4.74, -0.42, 0.0, 0.0, -0.36, 0.93, 1.00],
        [-3.99, -1.51, 0.0, 0.0, -0.80, 0.60, 1.00],
        [-1.72, 1.04, 0.0, 0.0, -0.64, 0.77, 1.00],
        [-2.99, -0.76, 0.0, 0.0, -0.30, 0.95, 1.00],
        [0.40, -2.03, 0.0, 0.0, 0.73, 0.68, 1.00]
    ]
    
    # Set our demo's initial pose
    initial_pose = PoseStamped()
    initial_pose.header.frame_id = 'map'
    initial_pose.header.stamp = navigator.get_clock().now().to_msg()
    initial_pose.pose.position.x = 0.0
    initial_pose.pose.position.y = 0.0
    initial_pose.pose.orientation.z = 0.0
    initial_pose.pose.orientation.w = 1.0
    navigator.setInitialPose(initial_pose)

    # Wait for navigation to fully activate
    navigator.waitUntilNav2Active()

    # Send our route
    inspection_points = []
    inspection_pose = PoseStamped()
    inspection_pose.header.frame_id = 'map'
    inspection_pose.header.stamp = navigator.get_clock().now().to_msg()
    for pt in inspection_route:
        inspection_pose.pose.position.x = pt[0]
        inspection_pose.pose.position.y = pt[1]
        # Simplification of angle handling for demonstration purposes
        inspection_pose.pose.orientation.z = pt[4]
        inspection_pose.pose.orientation.w = pt[5]
        inspection_points.append(deepcopy(inspection_pose))

    navigator.followWaypoints(inspection_points)

    # Do something during our route (e.x. AI to analyze stock information or upload to the cloud)
    # Simply the current waypoint ID for the demonstation
    i = 0
    while not navigator.isTaskComplete():
        i += 1
        feedback = navigator.getFeedback()
        if feedback and i % 5 == 0:
            print(
                'Executing current waypoint: '
                + str(feedback.current_waypoint + 1)
                + '/'
                + str(len(inspection_points))
            )

    result = navigator.getResult()
    if result == TaskResult.SUCCEEDED:
        print('Inspection of shelves complete! Returning to start...')
    elif result == TaskResult.CANCELED:
        print('Inspection of shelving was canceled. Returning to start...')
    elif result == TaskResult.FAILED:
        print('Inspection of shelving failed! Returning to start...')

    # go back to start
    initial_pose.header.stamp = navigator.get_clock().now().to_msg()
    navigator.goToPose(initial_pose)
    while not navigator.isTaskComplete():
        pass

    exit(0)


if __name__ == '__main__':
    main()