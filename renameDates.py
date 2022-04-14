#! python3
# renameDates.py - Ranames filenames with American date MM-DD-YYYY to 
# European date DD-MM-YYYY
import shutil, os, re

# Regex search the American date
datePattern = re.compile(r"""
    ^(.*?) # all contexts before date
    ((0|1)?\d) # month, one digit or two digits.
    -
    ((0|1|2|3)?\d) # day, one digit or two digits
    -
    ((19|20)\d\d) # 1900-2099 years
    (.*?)$ # all contexts after date
    """, re.VERBOSE)

# Loop directory, finding all filenames with a date
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # skip files without a date:
    # matching none of pattern return None
    if mo == None:
        continue

    # Get the different parts of filename (unknown)
    # (1)
    # (2(3)) -
    # (4(5)) -
    # (6(7))
    # (8)
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Form the European-style date 
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Get the full, absolute paths. 
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir,amerFilename)
    euroFilename = os.path.join(absWorkingDir,euroFilename)

    # todo: Rename the files.
    print('Rename "%s" to "%s"...' % (amerFilename, euroFilename))
    shutil.move(amerFilename, euroFilename)

