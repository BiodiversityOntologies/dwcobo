#!/usr/bin/env python3
"""
Author : Ramona L. Walls <rlwalls2008@gmail.com>
Date   : 2020-09-23
Purpose: Reformat a CSV file with Darwin Core terms into the format needed to convert it to OWL.
"""

#Steps:
#Load imports/terms.csv
#Pull out column 2 (IDs) and concatenate 'dwc:' to each ID
#Replace column 2 in file with concatenated values
#Insert a term label row, as needed by ROBOT, as row 2 into the CSV file.
#So far only tested to work with terms.csv. Will use iri.csv later.


import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments to input files"""

    parser = argparse.ArgumentParser(
        description='get command line arguments',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('inputfile',
                        metavar='file',
                        help='A positional argument for the input CSV file with terms',
                        type=file)

    parser.add_argument('-f',
                        '--file',
                        help='The file containing the labels row',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='term_label_row.csv')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file_arg = args.file
    pos_arg = args.inputfile


    print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))
     print(f'inputfile = "{pos_arg}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
