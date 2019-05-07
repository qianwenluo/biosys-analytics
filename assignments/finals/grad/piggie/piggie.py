#!/usr/bin/env python3
"""
Author : qianwenluo
Date   : 2019-05-07
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import re
import string


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Convert to Pig Latin',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='FILE', help='Input file(s)',nargs='+')


    # parser.add_argument(
    #     '-o', '--outdir', help='Output directory', action='store_true',default='out-yay')

    parser.add_argument(
        '-o',
        '--outdir',
        help='Output directory',
        metavar='DIR',
        type=str,
        default='out-yay')

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    files = args.positional
    out_dir = args.outdir

    new_list = []
    count = 0
    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)

    for i ,file in enumerate(files, start = 1):
        if not os.path.isfile(file):
            warn('"{}" is not a file.'.format(os.path.basename(file)))
            #print('Done, wrote 0 files to "{}".'.format(out_dir))
            continue
        count += 1
        basename = os.path.basename(file)
        out_file = os.path.join(out_dir, basename)
        fh = open(file,'r')
        out_fh = open(out_file, 'wt')

        for line in fh:
            for word in line.split():
                clean = re.sub("[^a-zA-Z0-9']", '', word)
                consonants = re.sub('[aeiouAEIOU]', '', string.ascii_letters)
                match = re.match('^([' + consonants + ']+)(.+)', clean)
                if match:
                    out_fh.write('-'.join([match.group(2), match.group(1) + 'ay']) + ' ')
                else:
                    out_fh.write(word + '-yay' + ' ')
            out_fh.write('\n')
            #new_word = ''.join(standard)
                #new_list.append(new_word)
            #out_fh.write(new_word)
        print('{}: {}'.format(i,basename))
    if count ==1:
        print('Done, wrote 1 file to "{}".'.format(out_dir))
    else:
        print('Done, wrote {} files to "{}".'.format(count, out_dir))

# --------------------------------------------------
if __name__ == '__main__':
    main()
