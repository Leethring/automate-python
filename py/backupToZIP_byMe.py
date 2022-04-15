#! python3
# backupToZIP.py - Copoies files to ZIP file and increments the ZIP filename number

import zipfile, sys, os

folder = sys.argv[1]

# Find the absolute path of given folder
folder = os.path.abspath(folder)

# Create a new ZIP files for backup
number = 1
while True:
    # Test the existence of other backup ZIP files
    # str(number) align the data type 
    zipName = os.path.basename(folder) + '_' + str(number) + '.zip'
    if not os.path.exists(zipName):
        break
    number = number + 1

print('Creating %s...' % (zipName))
backupZip = zipfile.ZipFile(zipName, 'w')

# todo: Walk folder and add files of folder to the ZIP files
# except ZIP files.
for foldername, subfolders, filenames in os.walk(folder):
    print('Adding %s to %s...' % (foldername, zipName))
    backupZip.write(foldername)

    for filename in filenames:
        # Test file being ZIP file
        if filename.startswith(os.path.basename(folder) + '_') and filename.endswith('.zip'):
            continue

        print('Adding %s in %s...' % (filename, foldername))
        backupZip.write(os.path.join(foldername, filename))

backupZip.close()
print('Done')
