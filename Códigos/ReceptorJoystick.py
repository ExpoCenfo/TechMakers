import espnow
import board
import analogio
import time
from ideaboard import IdeaBoard

ib = IdeaBoard()

# Cambiamos los pines a GPIO32 y GPIO33 que están en ADC1
x_axis_pin = ib.AnalogIn(board.IO32)
y_axis_pin = ib.AnalogIn(board.IO33)

direction_list = ["East", "Southeast", "South", "Southwest", "West", "Northwest", "North", "Northeast", "Centre"]

def get_zero(times=500, sleep=0.01):
    x_total = 0
    y_total = 0
    for i in range(times):
        x_axis = x_axis_pin.value
        y_axis = y_axis_pin.value
        x_total += x_axis
        y_total += y_axis
        time.sleep(sleep)
    x_zero = x_total // times
    y_zero = y_total // times
    return (x_zero, y_zero)

def get_direction(zero=(32767, 32767)):
    x_axis = x_axis_pin.value - zero[0]
    y_axis = y_axis_pin.value - zero[1]
    if x_axis >= 10000 and -10000 < y_axis < 10000:
        return direction_list[0]
    elif x_axis >= 10000 and y_axis <= -10000:
        return direction_list[1]
    elif -10000 < x_axis < 10000 and y_axis <= -10000:
        return direction_list[2]
    elif x_axis <= -10000 and y_axis <= -10000:
        return direction_list[3]
    elif x_axis <= -10000 and -10000 < y_axis < 10000:
        return direction_list[4]
    elif x_axis <= -10000 and y_axis >= 10000:
        return direction_list[5]
    elif -10000 < x_axis < 10000 and y_axis >= 10000:
        return direction_list[6]
    elif x_axis >= 10000 and y_axis >= 10000:
        return direction_list[7]
    else:
        return direction_list[8]

zero = get_zero(times=50, sleep=0.01)
print(zero)

e = espnow.ESPNow()
peer = espnow.Peer(mac=b'\xc8.\x18;8x')
e.peers.append(peer)

e.send("Starting...")

while True:
    x_axis = x_axis_pin.value - zero[0]
    y_axis = y_axis_pin.value - zero[1]
    direction = get_direction(zero=zero)
    print((x_axis, y_axis))
    print(direction)
    e.send(direction)
    time.sleep(0.1)