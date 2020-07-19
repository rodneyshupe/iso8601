#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import iso8601

def tests():
    """ Run a number of tests on to_minutes and to_seconds """
    test_data = [
            {'iso8601': 'PT10M', 'minutes': 10, 'seconds': 600},
            {'iso8601': 'PT5H', 'minutes': (5*60), 'seconds': (5*60*60)},
            {'iso8601': 'P3D', 'minutes': (3*24*60), 'seconds': (3*24*60*60)},
            {'iso8601': 'PT45S', 'minutes': (0), 'seconds': (45)},
            {'iso8601': 'P8W', 'minutes': (8*7*24*60), 'seconds': (8*7*24*60*60)},
            {'iso8601': 'P7Y', 'minutes': (7*365*24*60), 'seconds': (7*365*24*60*60)},
            {'iso8601': 'PT5H10M', 'minutes': (5*60+10), 'seconds': ((5*60+10)*60)},
            {'iso8601': 'P2YT3H10M', 'minutes': ((((2*365*24)+3)*60)+10), 'seconds': (((((2*365*24)+3)*60)+10)*60)},
            {'iso8601': 'P3Y6M4DT12H30M5S', 'minutes': ((((((3*365)+(6*30)+4)*24)+12)*60)+30), 'seconds': (((((((3*365)+(6*30)+4)*24)+12)*60)+30)*60+5)},
            {'iso8601': 'P23M', 'minutes': (23*30*24*60), 'seconds': (23*30*24*60*60)},
            {'iso8601': 'P2Y', 'minutes': (2*365*24*60), 'seconds': (2*365*24*60*60)}
        ]
    for test in test_data:
        seconds = iso8601.to_seconds( test['iso8601'] )
        minutes = iso8601.to_minutes( test['iso8601'] )
        if seconds == test['seconds']:
            seconds_result='pass (' + str(seconds) + ')'
        else:
            seconds_result='fail (expected ' + str(test['seconds']) + ' returned ' + str(seconds) + ')'
        if minutes == test['minutes']:
            minutes_result='pass (' + str(minutes) + ')'
        else:
            minutes_result='fail (expected ' + str(test['minutes']) + ' returned ' + str(minutes) + ')'

        print ("iso8601 duration Test: %-16s \t to_seconds %-16s \t to_minutes %-16s" % (test['iso8601'], seconds_result, minutes_result))
