#!/usr/bin/python3
# coding: utf-8

import traceback
import time
from systemd.journal import send

for i in range(10):
    for j in range(10):
        emsg = "quick brown dog jumps over the lazy fox {} - {}".format(i, j)
        send(emsg, PRIORITY=7)
    time.sleep(.5)




