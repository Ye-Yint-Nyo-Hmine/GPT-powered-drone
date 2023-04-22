from djitellopy import *
import logging
from drone_controls import *
import cv2

# run boolean
run = False

# initializing tello
drone = tello.Tello(retry_count=1)


# drone personals
sleep = False

# print txt
def say(text: str):
    print(text)


def main():
    """
    Connect to drone, and execute
    """
    global run

    # run set to True
    run = True

    drone = tello.Tello()


    # if connection failed, report, and run reset
    drone.connect()
    logging.info("Connected to drone")

    # open camera on drone
    drone.streamon()

    WIDTH, HEIGHT = 720, 480

    pTime = 0

    while run:

        flightMode(drone)

        raw_frame = drone.get_frame_read().frame()

        resized_frame = cv2.resize(raw_frame, (WIDTH, HEIGHT))
        frame = cv2.flip(resized_frame, 1)

        cTime = time.time()

        FPS = int(1/(cTime-pTime))
        pTime = cTime

        cv2.putText(frame, f"FPS: {FPS}", (15, 25), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 0, 0), 1)

        cv2.putText(frame, f"Battery: {drone.get_battery()}", (15, 50), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 1)

        cv2.imshow("Drone Cam", frame)
        cv2.waitKey(1)

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
