# LightMonitoring_Device
This is a Light Monitoring IoT Device which notifies you if anyone has Turned on/off the lights in the Room/House.

This device is Built on the concepts of Machine-Learning and IoT.

Done with using BoltIoT.  
# Harware used
  1)Bolt IoT Wifi Module
  2)LDR senor
  3)10k ohms carbon resistor
  4)Connecting Wires
  5)Bread Board.
![Untitled design](https://user-images.githubusercontent.com/76215048/160235428-bd99c416-1714-4174-a7b7-5a150e2004f1.jpg)
# Software used
  Python
# Editor used
  VS Code
# Code Preview


https://user-images.githubusercontent.com/76215048/160235865-d77c60ea-4f0c-488c-b7d3-360f7b427f1c.mp4

# Output
Initially it takes 10 data points after every 10 seconds to calculate the Z-score and decides the thershold bars , when suddenly the light is switched ON or OFF. The program will detech the Anomaly and It will send the Message to the Telegram accordingly.

Device collecting the data points.


https://user-images.githubusercontent.com/76215048/160236706-3868ced7-d91f-4d5a-a8a6-562093326928.mp4

When the light is Turned ON/OFF , The Intensity Increases/Decreases suddenly and it will detect the anomaly and sends the Telegram Message.


https://user-images.githubusercontent.com/76215048/160236855-86b978ab-7246-48cd-80f1-0c2c387abcc4.mp4

Telegram Notification Message.


https://user-images.githubusercontent.com/76215048/160236938-7f2d69f2-7b79-4585-939e-08def3865804.mp4

# Applications
It can be remodeled to send the Alert Messages.Like in a pharmaceutical factory [to detect the sudden change in temperature], Banks [if the credit card is misused], To keep a Note of your watchlist Stocks and Many more.

