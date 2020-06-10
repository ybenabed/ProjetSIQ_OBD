import obd
import files
import time

def get_distance():
    connection = obd.OBD() #may be changed to specify the interface
    cmd = obd.commands.DISTANCE_W_MIL
    distance = connection.query(cmd)
    return distance.value.magnitude


def get_speed():
    connection = obd.OBD() #may be changed to specify the interface
    # get the speed
    cmd = obd.commands.SPEED
    speed = connection.query(cmd)
    # add this value to the list of speeds
    files.write_value(speed.value.magnitude)

def get_speeds(delay):
    while(True):
        get_speed()
        time.sleep(delay)  