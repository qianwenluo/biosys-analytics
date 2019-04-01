#!/usr/bin/env python3
"""
Author : qianwenluo
Date   : 2019-03-26
Purpose: Rock the Casbah
"""

import os
import sys
import re

# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} DATE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    input = args[0]

    short = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05',
             'Jun':'06', 'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10',
             'Nov':'11', 'Dec':'12'}

    long = {'January':'01', 'February':'02', 'March':'03', 'April':'04', 'May':'05',
             'June':'06', 'July':'07', 'August':'08', 'September':'09', 'October':'10',
             'November':'11', 'December':'12'}

    date_re1 = re.compile('(?P<year>\d{4})'
                     '[-]'
                     '(?P<month>\d{1,})'
                     '[-]'
                     '(?P<day>\d{1,})')
    date_re1a = re.compile('(?P<year>\d{4})'
                     '(?P<month>\d{2})'
                     '(?P<day>\d{2})')

    date_re2 = re.compile('(?P<year>\d{4})'
                     '[-]'
                     '(?P<month>\d{1,})')


    date_re3 = re.compile('(?P<month>\d{1,})'
                          '/'
                          '(?P<year>\d{2})')


    date_re5 = re.compile('(?P<month>\D{3})'
                          '[,-]'
                          '[ ]?'
                          '(?P<year>\d{4})')

    date_re6 = re.compile('(?P<month>\D{4,})'
                          '[,-]'
                          '[ ]?'
                          '(?P<year>\d{4})')


    match1 = date_re1.match(input) or date_re1a.match(input)
    match2 = date_re2.match(input)
    match3 = date_re3.match(input)
    match4 = date_re5.match(input) or date_re6.match(input)


    if match1:
        standard = '{}-{}-{}'.format(match1.group('year'), match1.group('month').zfill(2), match1.group('day').zfill(2))

    elif match2:
        standard = '{}-{}-01'.format(match2.group('year'), match2.group('month').zfill(2))

    elif match3:
        standard = '20{}-{}-01'.format(match3.group('year'),match3.group('month').zfill(2))

    elif match4:
        if len(match4.group('month')) == 3:
            month = short[match4.group('month')]
        else:
            month = long[match4.group('month')]
        standard = '{}-{}-01'.format(match4.group('year'),month)
    else:
        standard = 'No match'

    print('{}'.format(standard))






# --------------------------------------------------
main()
