# Subsystems

Our robots have various subsytems that need precise control. While the chassis is controlled through our localization and autonomous navigation systems, the subsystems require a separate solution. We have implemented an abstract subsystem object and base class. These provide our developers with significant flexibility and allow for the rapid development of our core software which changes annually. 

All subsystems are implemented as either position or velocity PID controllers for accurate and reliable movement. This is done under the hood and the calls to operate subsystems may simply look like:

``` c++
lift->moveToPosition(4_ft);
```

The use of PID controlled subsystems significantly increases the speed and accuracy of our robots. However, it comes at the cost of tuning time. Given the complexity of our robots, it is often very time consuming to tune the various control loops. To simplify this process, we have implemented a control loop tuning interface that interfaces with our existing subsystem classes. The joystick operated interface allows the user to rapidly tune the control loops and provides helpful feedback to novice users.