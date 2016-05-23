#!/usr/bin/env python


import rospy
from smach import State, StateMachine
from time import sleep

# define state One
class One(State):
    def __init__(self):
        State.__init__(self, outcomes=['success','flat'])
        self.one_counter=0
    def execute(self, userdata):
        print 'one'
	sleep(1)
	if self.one_counter < 3:
            self.one_counter += 1
            return 'success'
        else:
	    self.one_counter=0
            return 'flat'


# define state Two
class Two(State):
    def __init__(self):
        State.__init__(self, outcomes=['success','flat'])
        self.two_counter=0
    def execute(self, userdata):
        print 'two'
	sleep(1)
        
	if self.two_counter < 3:
            self.two_counter += 1
            return 'success'
        else:
	    self.two_counter=0
            return 'flat'
   
# define state Three
class Recharge(State):
    def __init__(self):
        State.__init__(self, outcomes=['charged'])
        
    def execute(self, userdata):
        print 'recharged'
	sleep(1)
        return 'charged'
    
# main
if __name__ == '__main__':
    
    # Create a SMACH state machine
    sm = StateMachine(outcomes=['success'])

    # Open the container
    with sm:
        # Add states to the container
        StateMachine.add('ONE', One(),transitions={'success':'TWO','flat':'RECHARGE'})
        StateMachine.add('TWO', Two(),transitions={'success':'ONE','flat':'RECHARGE'})
	StateMachine.add('RECHARGE', Recharge(),transitions={'charged':'ONE'})

    # Execute SMACH plan
    sm.execute()

