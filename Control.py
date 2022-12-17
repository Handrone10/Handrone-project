import Voicy
import Handy
from djitellopy import tello

drone = tello.Tello()
drone.connect()
drone.get_battery()

c = Voicy.Voices()
command = c.Command()

if command == '이륙':
    drone.takeoff()
    while True:
        command = c.Command()
        if command == '착륙':
            drone.land()
        elif command:
            x = Handy.Hand()
            x.motion(command)
