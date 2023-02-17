"""
Nose tests for acp_times.py

Write your tests HERE AND ONLY HERE.
"""
from acp_times import open_time, close_time # added these
import arrow

import nose    # Testing framework
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)


# Use given website to get the correct values for testing!  https://rusa.org/octime_acp.html
# sudo docker exec container /app/run_tests.sh

def test_brevet_1():
    # distance: (expected open, expected close)
    # copy this five times with different values and you're done with testing
    
    brevet_start = arrow.get('2023-02-17 00:00', "YYYY-MM-DD HH:MM")
    brevet = 200
    checkpoints = {
        0: (brevet_start, brevet_start.shift(hours=1)),
        50: (brevet_start.shift(hours=1, minutes=28), brevet_start.shift(hours=3, minutes=30)),
        # and so on 150 200 blah blah
        100: (brevet_start.shift(hours=2, minutes=56), brevet_start.shift(hours=6, minutes=40)),
        #150 4:25 10:00
        #200 5:53 13:30
    }
    for km, time_tuple in checkpoints.items(): # loop through checkpoints
        check_open, check_close = time_tuple
        assert(open_time(km, brevet, brevet_start) == check_open)
        assert(close_time(km, brevet, brevet_start) == check_close)


    
