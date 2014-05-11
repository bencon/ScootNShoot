Team Scoot-N-Shoot Senior Design Project University of Delaware
https://sites.google.com/a/udel.edu/scootnshoot/

Scoot-N-Shoot is an open-surfing WiFi project that focuses on finding and tracking the best available WiFi network and uploading as much data securely as quickly as possible.

In this repository you will find the code responsible for signal tracking. Materials needed include:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yagi antenna  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;two servos  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tripod  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;two servos  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Alpha usb dongle  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Arduino Uno   

The application runs as follows:  
&nbsp;&nbsp;&nbsp;1)performs scans on all available wifi network  
&nbsp;&nbsp;&nbsp;2)connects to strongest network  
&nbsp;&nbsp;&nbsp;3)performs a 360 degree scan on current network, sampling signal strength as it goes  
&nbsp;&nbsp;&nbsp;4)finds the direction of greatest signal strength after calculating a rolling average on sampled data  
&nbsp;&nbsp;&nbsp;5)orients antenna in most optimal direction  
