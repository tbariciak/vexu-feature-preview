# Autonomous Navigation

The ability to autonomously navigate an environment is critical. Our autonomous navigation solution complements our localization system. To maximize the consistency of autonomous gameplay we use a global coordinate frame overlayed on the game field. 

Our robots are controlled using directional commmands relative to points. For instance, turning to a game element could be written as:

``` c++
turnToPoint({4_ft, 4_ft})
```
This system allows our robots to reliably navigate their environment and make dynamic scoring decisions.

