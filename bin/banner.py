#!/usr/bin/env python

import string, sys, argparse

p = argparse.ArgumentParser()

p.add_argument('-s','--style', choices=['big', 'small', 'tiny'], default='big')
p.add_argument('words', nargs='+')

args = p.parse_args()

print args

#
# Make sure there's a space on either side of the phrase
#
args.words.insert(0, '')
args.words.append('')

phrase = ' '.join(args.words).upper()

if args.style=='big':
    print "//" + 78*'*'
    print "//{: ^78s}".format(phrase)
    print "//" + 78*'*'
if args.style=='small':
    print "//{:-^78s}".format(phrase)
if args.style=='tiny':
    print "// -----" + phrase + "-----"