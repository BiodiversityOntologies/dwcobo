#!/usr/bin/env python3
"""
Author : Ramona L. Walls <rlwalls2008@gmail.com>
Date   : 2020-09-23
Purpose: Reformat a CSV file with Darwin Core terms into the format needed to convert it to OWL.
"""

#Steps:
#Load imports/terms.csv
#Insert a term label row, as needed by ROBOT, as row 2 into the CSV file.
#Concatenate 'DWC:' to each ID in column 2
#Save output to a CSV file.
#So far only tested to work with terms.csv. Will use iri.csv later.


import argparse, os, pandas


# --------------------------------------------------
def get_args():
    """Get command-line arguments to input files"""

    parser = argparse.ArgumentParser(
        description='get command line arguments',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-i',
                        '--inputfile',
                        metavar='string',
                        help='input CSV file with terms',
                        type=str,
                        default='imports/terms.csv')

    parser.add_argument('-l',
                        '--labels',
                        help='file containing the labels row',
                        metavar='string',
                        type=str,
                        default='terms_label_row.csv')

    parser.add_argument('-o',
                        '--outputfile',
                        help='modified output file',
                        metavar='string',
                        type=str,
                        default='')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """reformat the DwC terms file"""

    args = get_args()
    outfile = args.outputfile
    
    infile = pandas.read_csv(args.inputfile)
    labels = pandas.read_csv(args.labels)
    robotlabels = list(labels)
    new = infile
    new.loc[-1] = robotlabels
    new.index = new.index + 1
    new =  new.sort_index()
    ID = new['term_localName']
    IDlist = []
    for id in ID:
        newid = 'DWC:'+id
        IDlist.append(newid)
    #The True statement below overwrites the existing DF "new")
    new.insert(1, 'ID', IDlist, True)
    if outfile:
        new.to_csv(outfile, index=False)
    else:
        new.to_csv('newtest.csv', index=False)

    print(f'new = {new}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
