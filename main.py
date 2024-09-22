t1 = 20
t2 = 40

def on_forever():
    if input.rotation(Rotation.ROLL) > 0 - t1 and input.rotation(Rotation.ROLL) < t1:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
    elif input.rotation(Rotation.ROLL) > 0 - t2:
        basic.show_leds("""
            . . . . .
            . . . . .
            . # . . .
            . . . . .
            . . . . .
            """)
    elif input.rotation(Rotation.ROLL) < 0 - t2:
        basic.show_leds("""
            . . . . .
            . . . . .
            # . . . .
            . . . . .
            . . . . .
            """)
    elif input.rotation(Rotation.ROLL) > t2:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . #
            . . . . .
            . . . . .
            """)
    elif True:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . # .
            . . . . .
            . . . . .
            """)
    else:
        basic.show_leds("""
            . . # . .
            . . # . .
            . . # . .
            . . # . .
            . . # . .
            """)
basic.forever(on_forever)
