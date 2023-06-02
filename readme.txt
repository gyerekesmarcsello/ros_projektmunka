TurtleBot Mozgatás

A TurtleBotunkat a Gazeboo emulátorba helyezzük.

A feladat, hogy az elé kerülő akadályokat észlelje, és megpróbálja kikerülni LIDAR szenzor segítségével
Az első lépés hogy feliratkozunk a LIDAR Scan topicjára és velocity parancsokat publisholjuk cmd_vel a topicnak, hogy navigálni tudjunk az akadályok között.

Amikor a robot érzékel egy akadályt. megpróbál elfordulni, hogy folytassa az útját.

További részletekért itt a Turtlebot3 dokumentációja:
https://ros2-industrial-workshop.readthedocs.io/en/latest/_source/navigation/ROS2-Turtlebot.html
