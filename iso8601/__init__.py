#!/usr/bin/env python
# -*- coding: utf-8 -*-

def to_minutes( iso8601_duration ):
    """ Take iso8601 duration and returns minutes
        (rounded down to whole minute)
    """
    try:
        minutes = int(to_seconds(iso8601_duration)/60)
    except:
        minutes = 0
    return minutes

def to_seconds( iso8601_duration ):
    """ Take iso8601 duration and returns seconds """
    from re import findall

    def year(number):
        return number * 365 * 24 * 60 * 60

    def month(number):
        return number * 30 * 24 * 60 * 60 # Assumes 30 days

    def week(number):
        return number * 7 * 24 * 60 * 60

    def day(number):
        return number * 24 * 60 * 60

    def hour(number):
        return number * 60 * 60

    def minute(number):
        return number * 60

    def second(number):
        return number

    switcher = {
        'Y': year,
        'M': month,
        'W': week,
        'D': day,
        'H': hour,
        'm': minute,
        'S': second
    }

    if iso8601_duration[0] != 'P':
        raise ValueError('Not an ISO 8601 Duration string')
    seconds = 0
    # split by the 'T'
    for i, item in enumerate(iso8601_duration.split('T')):
        for number, unit in findall( '(?P<number>\d+)(?P<period>S|M|H|D|W|Y)', item ):
            # print '%s -> %s %s' % (d, number, unit )
            number = int(number)
            return_value = 0
            if unit == 'M' and i != 0:
                unit = 'm'
            func = switcher.get(unit, lambda: "Invalid ISO 8601 Duration string")
            seconds = seconds + func(number)
    return seconds
