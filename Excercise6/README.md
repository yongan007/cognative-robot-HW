
>* I run 10 replications of the experiment from 
the evorobotpy/xdiscrim folder by using seeds from 1 to 13. For 1 to 10 I launched the training process with the LSTM architecture,
and 11-13 with Feed-Forward.

>* I noticed that robot can achieves the target and stop with seed 1,3,4,5,7,8,9,10. Robot moves clockwise about the target with seed 2
and moves counterclockwise with seed 6. With Feed-Forward architecture at seed 11 go to the target and move around and at seed 12,13 robot go to the 
target but doesn't stop. 

>* After running these experiment I found that robot with LSTM (Long Short Term Memory architecture) robot and reach the goal. However with Feed-Forward (without memory)
robot can't stop at the goal becuase it doesn't have feedback that why it can't estimate state or evolution stategy. 

>* Robot reach the goal and stop 
![alt text](/img/s1.gif)

>* Robot reach the goal and moving around (seed 2) 
![alt text](/img/s2.gif)

>* Robot doesn't stop when reach the goal (seed 11) 
![alt text](/img/s11.gif)