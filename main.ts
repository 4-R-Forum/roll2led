bluetooth.onBluetoothConnected(function () {
    bluetooth.startAccelerometerService()
    bluetooth.startButtonService()
})
function doPitch () {
    if (p > 0 - t1 && p < t1) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            `)
    } else if (p < 0 - t2) {
        basic.showLeds(`
            . . # . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    } else if (p < 0 - t1) {
        basic.showLeds(`
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            . . . . .
            `)
    } else if (p > t2) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . # . .
            `)
    } else {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            `)
    }
}
function doRoll () {
    if (r > 0 - t1 && r < t1) {
        doPitch()
    } else if (r < 0 - t2) {
        basic.showLeds(`
            . . . . .
            . . . . .
            # . . . .
            . . . . .
            . . . . .
            `)
    } else if (r < 0 - t1) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . # . . .
            . . . . .
            . . . . .
            `)
    } else if (r > t2) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . #
            . . . . .
            . . . . .
            `)
    } else {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . # .
            . . . . .
            . . . . .
            `)
    }
}
let r = 0
let p = 0
let t2 = 0
let t1 = 0
basic.showString("roll2LED")
t1 = 20
t2 = 40
basic.forever(function () {
    r = input.rotation(Rotation.Roll)
    p = input.rotation(Rotation.Pitch)
    doRoll()
})
