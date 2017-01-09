# Test script for Boldport TheMatrix

Here's a quick Python test script to drive your board from a Raspberry Pi.

## Prerequisites

You need I2C set up on your Raspberry Pi. If you haven't done this before, you
need to enable the I2C hardware:

    sudo raspi-config

Choose `9 Advanced Options`, `A6 I2C`, `Yes`, `Ok`, `Finish`.

Next, you'll need to install the I2C support for Python:

    sudo apt-get install python-smbus

It's possible that you'll need to reboot at this point, but I've not found that
necessary on the Raspberry Pi boards I've tried so far.

## Connections

To connect to the I2C bus on the Raspberry Pi, connect directly to the
expansion header. Here's a top-down view - pin 1 is closest to the display
connector:

        VCC  1  2
        SDA  3  4
        SCL  5  6
             7  8
        GND  9 10
            11 12
            13 14
            15 16
            17 18
            19 20
            21 22
            23 24
            25 26
            27 28
            29 30
            31 32
            33 34
            35 36
            37 38
            39 40
        [USB ports this end]

## Usage

From your Raspberry Pi shell, run `i2cdetect` to check that your TheMatrix is
responding and has the address you're expecting:

    i2cdetect -y 1

By default, TheMatrix will have address 0x30 if you haven't added a resistor at
R4 to specify otherwise.

## [the_matrix.py](./the_matrix.py)

If your address matches the default, you can just run the Python script
directly:

    python the_matrix.py

and that should light up all the LEDs. There's some extra functionality in
there (it can set/clear individual pixels, handle PWM and blink frames, etc)
but it's not complete or tested yet.

If your board has a different address, you'll want to change the address
hard-coded at the top of the script.

## [matrix_leds.py](./matrix_leds.py)

There's a script called `matrix_leds.py` which can set specified LEDs on
individually - that may be useful for testing too. You can specify LEDs either
by coordinates or by their logical number in hex, or groups of LEDs by AS1130
pin:

    # turn on three LEDs
    python matrix_leds.py 7 9 b0

    # turn on top left corner and top right corner LEDs
    python matrix_leds.py 0,0 23,0

    # turn on all LEDs whose anode connects to CS2
    python matrix_leds.py cs2

    # turn on all LEDs whose cathode connects to CS10
    python matrix_leds.py /CS10

It can also show a map of the physical connections for each LED:

    python matrix_leds.py -p

    Physical layout:
    +-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
    |    /CS0   |    /CS1   |    /CS2   |    /CS3   |    /CS4   |    /CS5   |    /CS6   |    /CS7   |    /CS8   |    /CS9   |   /CS10   |   /CS11   |
    +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
    | CS1 | CS6 | CS0 | CS6 | CS0 | CS6 | CS0 | CS6 | CS0 | CS6 | CS0 | CS6 | CS0 | CS5 | CS0 | CS5 | CS0 | CS5 | CS0 | CS5 | CS0 | CS5 | CS0 | CS5 |
    +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
    | CS2 | CS7 | CS2 | CS7 | CS1 | CS7 | CS1 | CS7 | CS1 | CS7 | CS1 | CS7 | CS1 | CS7 | CS1 | CS6 | CS1 | CS6 | CS1 | CS6 | CS1 | CS6 | CS1 | CS6 |
    +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
    | CS3 | CS8 | CS3 | CS8 | CS3 | CS8 | CS2 | CS8 | CS2 | CS8 | CS2 | CS8 | CS2 | CS8 | CS2 | CS8 | CS2 | CS7 | CS2 | CS7 | CS2 | CS7 | CS2 | CS7 |
    +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
    | CS4 | CS9 | CS4 | CS9 | CS4 | CS9 | CS4 | CS9 | CS3 | CS9 | CS3 | CS9 | CS3 | CS9 | CS3 | CS9 | CS3 | CS9 | CS3 | CS8 | CS3 | CS8 | CS3 | CS8 |
    +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
    | CS5 | CS10| CS5 | CS10| CS5 | CS10| CS5 | CS10| CS5 | CS10| CS4 | CS10| CS4 | CS10| CS4 | CS10| CS4 | CS10| CS4 | CS10| CS4 | CS9 | CS4 | CS9 |
    +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+

and a logical map with the LED numbers in hex (the same numbers it expects on
the command line):

    python matrix_leds.py -l

    Logical layout:
    +-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
    | Segment 0 | Segment 1 | Segment 2 | Segment 3 | Segment 4 | Segment 5 | Segment 6 | Segment 7 | Segment 8 | Segment 9 | Segment A | Segment B |
    +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
    |  00 |  05 |  10 |  15 |  20 |  25 |  30 |  35 |  40 |  45 |  50 |  55 |  60 |  65 |  70 |  75 |  80 |  85 |  90 |  95 |  A0 |  A5 |  B0 |  B5 |
    +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
    |  01 |  06 |  11 |  16 |  21 |  26 |  31 |  36 |  41 |  46 |  51 |  56 |  61 |  66 |  71 |  76 |  81 |  86 |  91 |  96 |  A1 |  A6 |  B1 |  B6 |
    +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
    |  02 |  07 |  12 |  17 |  22 |  27 |  32 |  37 |  42 |  47 |  52 |  57 |  62 |  67 |  72 |  77 |  82 |  87 |  92 |  97 |  A2 |  A7 |  B2 |  B7 |
    +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
    |  03 |  08 |  13 |  18 |  23 |  28 |  33 |  38 |  43 |  48 |  53 |  58 |  63 |  68 |  73 |  78 |  83 |  88 |  93 |  98 |  A3 |  A8 |  B3 |  B8 |
    +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
    |  04 |  09 |  14 |  19 |  24 |  29 |  34 |  39 |  44 |  49 |  54 |  59 |  64 |  69 |  74 |  79 |  84 |  89 |  94 |  99 |  A4 |  A9 |  B4 |  B9 |
    +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+

## Web Interface - [web.py](./web.py)

This is a very basic web interface for controlling TheMatrix. It runs on the
Raspberry Pi and uses `the_matrix.py` described above. It needs Flask to run,
which you can install with:

    pip install flask

(you may need to do that as root, depending on your system setup). To start the
application, just run it:

    python web.py

and visit your Raspberry Pi's IP address or hostname on port 5000 in your
browser. The application lets you control individual LEDS, rows and columns of
them together and vary the LED current.
