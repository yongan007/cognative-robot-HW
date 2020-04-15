

## Exercise 4  

> * By comparing the original (for reinforcement learning) and 
the modified (for evolutionary algorithms) reward functions, the differences 
between them are :

* alive - To checks if robot fall or not by measuring the height of the robot. For evolutionary algorithms, it gives bonus when robot doesn't falling down.
* progress - The movement of the robot to the target. For evolutionary algorithms,it was normolize between[-1,1].
* electricity_cost -  The cost for using motors. For 
* joints_at_limit_cost - discourage stuck joints. For evolutionary algorithms, it uses angle_offset_cost for checking 
the angle difference between the robot and the target.
* feet_collision_cost -  to avoide collisions of robot links. For evolutionary algorithms, 
it uses feet_collision_cost and feet_cost to check if both of feet touch the ground or not.

> * By running both reward function in the case of the hopper and
halfcheetah. With the original I could see that the robot can't move or fall down, while 
with the modified, the agents behaves significantly better and robot can move toward the target.


> * The modified function is evolutionary algorithms that use the population of agents to learn and take best rewards to fit evolutionary strategies and keep improving
over generation. The original function which is reinforcement learning algorithms, it is suitable for only one agent.



