#!/usr/bin/env python

import sys
import rospy
import rospkg, genpy
import yaml
import copy

import moveit_commander
import geometry_msgs.msg
import moveit_msgs.msg
#from moveit_commander import RobotCommander, PlanningSceneInterface, MoveGroupCommander
#from moveit_commander import roscpp_initialize, roscpp_shutdown
#from moveit_msgs.msg import RobotState, Grasp
#from geometry_msgs.msg import PoseStamped

from std_msgs.msg import String


def move_group_python_interface():
	group.set_start_state_to_current_state() #WICHTIG	
	display_trajectory_publisher = rospy.Publisher(
		                      '/move_group/display_planned_path',
		                      moveit_msgs.msg.DisplayTrajectory, queue_size=1)

	## Wait for RVIZ to initialize. This sleep is ONLY to allow Rviz to come up.
	print "============ Waiting for RVIZ..."
	rospy.sleep(10)
	print "============ Starting tutorial "



	print "============ Generating plan 1"
	pose_target = geometry_msgs.msg.Pose()
	pose_target.orientation.w = 1.0
	pose_target.position.x = 0.26345
	pose_target.position.y = -0.038236
	pose_target.position.z = 0.95528
	group.set_pose_target(pose_target)
	plan1 = group.plan()
	rospy.sleep(10)	
	#group.clear_pose_targets()

	#group.go(wait=True) #uncomment with real robot #moves robot arm
	group.execute(plan1)
	rospy.sleep(10)
	group.set_start_state_to_current_state() #WICHTIG


	## Then, we will get the current set of joint values for the group
	group_variable_values = group.get_current_joint_values()
	print "============ Joint values: ", group_variable_values


	#---------------------------------------------------------------------------------------
	##ZWEITE BEWEGUNG!!
	group_variable_values[0] = 0
	group_variable_values[1] = -1.570796314870016
	group_variable_values[2] = 0
	group_variable_values[3] = -1.5707600752459925
	group_variable_values[4] = 0
	group.set_joint_value_target(group_variable_values)
	
	plan2 = group.plan()
	rospy.sleep(10)
	group.execute(plan2)	
	rospy.sleep(10)
	group.set_start_state_to_current_state() #WICHTIG




if __name__ == "__main__":
	#roscpp_initialize(sys.argv)
	moveit_commander.roscpp_initialize(sys.argv)
	rospy.init_node('moveit_grasp_app', anonymous=True)
	rospy.loginfo("Starting grasp app")
	# add some code here

	robot = moveit_commander.RobotCommander()
	scene = moveit_commander.PlanningSceneInterface()
	group = moveit_commander.MoveGroupCommander("manipulator")
	
	#display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',moveit_msgs.msg.DisplayTrajectory,queue_size = 10)
	rospy.sleep(1)

	move_group_python_interface()
	
	rospy.spin()
	moveit_commander.roscpp_shutdown() #vorher roscpp_shutdown()
	rospy.loginfo("Stopping grasp app")
