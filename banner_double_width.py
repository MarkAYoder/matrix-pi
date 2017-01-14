#!/usr/bin/env python

# This assumes you've got two boards configured like this:
#
# +---------------+---------------+
# | Address: 0x30 | Address: 0x37 |
# +---------------+---------------+

from __future__ import print_function

from the_matrix import TheMatrix

import getopt, re, sys

def usage():
    print("Usage: %s <banner frames filename>" % (sys.argv[0]), file=sys.stderr)

def frame_from_data(frame_data):
    f = TheMatrix.OnOffFrame()
    for y in range(5):
        for x in range(24):
            if frame_data[y][x] == '#':
                f.setPixel(x, y)
    return f

def display_banner(args):
    frames = []
    for filename in args:
        frame_data = []
        for line in open(filename, 'r'):
            line = line.strip()
            if len(line) == 0:
                frames.append(frame_from_data(frame_data))
                frame_data = []
            else:
                frame_data.append(line)
        if len(frame_data):
            frames.append(frame_from_data(frame_data))

    m1 = TheMatrix(0x30)
    m2 = TheMatrix(0x37)

    m1.reset()
    m2.reset()
    m1.selectMemoryConfig(1)
    m2.selectMemoryConfig(1)
    m1.setClockSync(sync_out=1)
    m2.setClockSync(sync_in=1)
    m1.setCurrentSource(1)
    m2.setCurrentSource(1)

    blinkPWMFrame = TheMatrix.BlinkPWMFrame()
    m1.writeBlinkPWMFrame(0, blinkPWMFrame)
    m2.writeBlinkPWMFrame(0, blinkPWMFrame)

    for frame_num in range(len(frames)):
        m1.writeOnOffFrame(frame_num, frames[frame_num])
        m2.writeOnOffFrame(frame_num, frames[frame_num])

    m1.setDisplayOptions(loops=7)
    m2.setDisplayOptions(loops=7)
    m1.display(1)
    m2.display(1)
    m1.setMovieMode(frames=len(frames))
    m2.setMovieMode(frames=len(frames))
    m1.setFrameTime(1, enable_scrolling=1)
    m2.setFrameTime(1, enable_scrolling=1)
    m1.displayMovie()
    m2.displayMovie(frame=1)

def main(args):
    global frames

    try:
        opts, args = getopt.getopt(args, "h")
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()

    display_banner(args)

if __name__ == "__main__":
    main(sys.argv[1:])