## Team Scoot-N-Shoot Senior Design Project University of Delaware
[ScootNShoot](https://sites.google.com/a/udel.edu/scootnshoot/)


Scoot-N-Shoot is an open-surfing WiFi project that focuses on finding and tracking the best available WiFi network and uploading as much data securely as quickly as possible.

In this repository you will find the code responsible for signal tracking. Materials needed include:

* Yagi antenna
* Two servos
* Tripod
* Two servos
* Alpha usb dongle
* Arduino Uno

The application runs as follows:
1. Performs scans on all available wifi network
2. Connects to strongest network
3. Performs a 360 degree scan on current network, sampling signal strength as it goes
4. Finds the direction of greatest signal strength after calculating a rolling average on sampled data
5. Orients antenna in most optimal direction

The aruino code included was a modified version of a sketch by Brian D. Wendt:
[https://bws428.github.io/arduino-python-4-axis-servo/](https://bws428.github.io/arduino-python-4-axis-servo/)

