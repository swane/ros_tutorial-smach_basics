#!/usr/bin/env python


import rospy
from smach import State, StateMachine
from time import sleep

# define state One
class One(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])
        
    def execute(self, userdata):
        print 'one'
	sleep(1)
        return 'success'


# define state Two
class Two(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])
        
    def execute(self, userdata):
        print 'two'
	sleep(1)
        return 'success'
       
# main
if __name__ == '__main__':
    
    # Create a SMACH state machine
    sm = StateMachine(outcomes=['success'])

    # Open the container
    with sm:
        # Add states to the container
        StateMachine.add('ONE', One(),transitions={'success':'TWO'})
        StateMachine.add('TWO', Two(),transitions={'success':'ONE'})

    # Execute SMACH plan
    sm.execute()

