from Color_Syntax import *
import time
import keyboard

def override(drone):
    """
    Emergency Protocol -
    0) override, else:
    1) try landing,
    2) try emergency (stop all motors)
    """
    protocol = False
    terminate = False

    print(f"{Fore.YELLOW}[INFO] Overriding drone ...")
    try:
        drone.send_rc_control(0, 0, 0, 0)
        try:
            drone.land()
            print(f"{Fore.GREEN}[SUCCESS] Drone successfully has been override")
        except:
            print(f"{Fore.RED}[ERROR] Overriding FAILED")
            protocol = True
    except:
        print(f"{Fore.RED}[ERROR] Overriding FAILED")
        protocol = True

    if protocol:
        print(f"{Fore.YELLOW}[INFO] Initiating emergency procedures")
        try:
            drone.land()
        except:
            print(f"{Fore.RED}[ERROR] Drone land command was unsuccessful")
            terminate = True

    if terminate:
        print(f"{Fore.LIGHTYELLOW_EX}[BEWARE] Terminating drone ...")
        time.sleep(0.5)
        drone.emergency()


def flightMode(drone, speed=45):

    lrv, fbv, udv, yv = 0, 0, 0, 0
    yawFactor = 0.75

    if keyboard.is_pressed("a"):
        lrv -= speed

    elif keyboard.is_pressed("d"):
        lrv = speed

    if keyboard.is_pressed("w"):
        fbv = speed

    elif keyboard.is_pressed("s"):
        fbv -= speed

    if keyboard.is_pressed("up"):
        udv = speed

    elif keyboard.is_pressed("down"):
        udv -= speed

    if keyboard.is_pressed("left"):
        yv -= (speed * yawFactor)

    elif keyboard.is_pressed("right"):
        yv = (speed * yawFactor)

    if keyboard.is_pressed("1"):
        drone.takeoff()

    if keyboard.is_pressed("2"):
        drone.land()

    drone.send_rc_control(lrv, fbv, udv, yv)

