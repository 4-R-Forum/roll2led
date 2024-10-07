def on_bluetooth_connected():
    bluetooth.start_accelerometer_service()
    bluetooth.start_button_service()
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def doPitch():
    if p > 0 - t1 and p < t1:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
    elif p < 0 - t2:
        basic.show_leds("""
            . . # . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
    elif p < 0 - t1:
        basic.show_leds("""
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            . . . . .
            """)
    elif p > t2:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . # . .
            """)
    else:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            """)
def doRoll():
    if r > 0 - t1 and r < t1:
        doPitch()
    elif r < 0 - t2:
        basic.show_leds("""
            . . . . .
            . . . . .
            # . . . .
            . . . . .
            . . . . .
            """)
    elif r < 0 - t1:
        basic.show_leds("""
            . . . . .
            . . . . .
            . # . . .
            . . . . .
            . . . . .
            """)
    elif r > t2:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . #
            . . . . .
            . . . . .
            """)
    else:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . # .
            . . . . .
            . . . . .
            """)
r = 0
p = 0
t2 = 0
t1 = 0
t1 = 20
t2 = 40

def on_forever():
    global r, p
    r = input.rotation(Rotation.ROLL)
    p = input.rotation(Rotation.PITCH)
    doRoll()
basic.forever(on_forever)
