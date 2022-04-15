#! python3 
# renameDate_byMe.py - Changes the American date MM-DD-YYYY to European date DD-MM-YYYY in the filename. 

import os, re, shutil
from sre_parse import Verbose

# prepare american date MM-DD-YYYY
patternName = re.compile(r"""
    ^(.*?)          # contexts before date
    ((1|0)\d)       # month with one digit or two digits
    -
    ((0|1|2|3)\d)   # day 
    - 
    ((19|20)\d\d)   # year
    (.*?)$          # contexts after date
""", re.VERBOSE)

# find files with American date pattern
for amerFilename in os.listdir('.'):
    mo = patternName.search(amerFilename)
    print(type(patternName))

    # skip files without pattern
    if mo == None:
        continue

    beforeDate = mo.group(1)
    monthDate = mo.group(2)
    dayDate = mo.group(4)
    yearDate = mo.group(6)
    afterDate = mo.group(8)

    # transfer American date to European date DD-MM-YYYY
    euroFilename = beforeDate + dayDate + '-' + monthDate + '-' + yearDate + afterDate

    # todo: rename the files.
    absPath = os.path.abspath('.')
    amerFilename = os.path.join(absPath, amerFilename)
    euroFilename = os.path.join(absPath, euroFilename)

    print('The "%s" is changed to "%s" ' % (amerFilename, euroFilename))
    shutil.move(amerFilename, euroFilename)
