#!/usr/bin/env python3
"""
Author : Ramona L. Walls <rlwalls2008@gmail.com>
Date   : 2020-12-31
Purpose: Reformat a CSV file with Darwin Core terms into the format needed to convert it to OWL.
"""

#Steps:
#Load ../imports/terms.csv or ../imports/iri.csv
#Insert a term label row, as needed by ROBOT, as row 2 into the CSV file.
#Concatenate 'DWC:' to each ID in column 2
#Save output to a CSV file.
#By default, converts terms.csv to dwcterms.csv. To convert iri.csv to dwciri.csv, just specify the input and output.


import argparse, os, pandas, re


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
                        default='../imports/terms.csv')

    parser.add_argument('-l',
                        '--labels',
                        help='file containing the label row for robot',
                        metavar='string',
                        type=str,
                        default='label_row.csv')

    parser.add_argument('-o',
                        '--outputfile',
                        help='modified output file',
                        metavar='string',
                        type=str,
                        default='dwcterms.csv')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """reformat the DwC terms or iri file"""

    args = get_args()
    outfile = args.outputfile
    
    infile = pandas.read_csv(args.inputfile)
    labels = pandas.read_csv(args.labels)
    rlabels = list(labels)
    robotlabels = list()
    for x in rlabels:
        y = re.sub('Unnamed: [0-9]+', '', x)
        robotlabels.append(y)
    new = infile
    ID = new['term_localName']
    IDlist = []
    for id in ID:
        newid = 'DWC:'+id
        IDlist.append(newid)
    #The True statement below overwrites the existing DF "new")
    new.insert(1, 'ID', IDlist, True)
    new.drop(columns = ['term_localName'], inplace=True)
    new.rename(columns = {'ID': 'term_localName'}, inplace=True)
    new.loc[-1] = robotlabels
    new.index = new.index + 1
    new =  new.sort_index()
    new.to_csv(outfile, index=False)

    print(f'new = {new}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
