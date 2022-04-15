#! python3
# backupToZip.py - Copies an entire folder and its contents into 
# a ZIP file whose filename increments.

import zipfile, os, sys

# Find the absolute path of given argument (folder)
folder = sys.argv[1]
folder = os.path.abspath(folder) 

# Find the filename this code should use based on 
# what files already exist.
number = 1
while True:
    # For every new backed ZIP file, add an incremented number
    zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
    if not os.path.exists(zipFilename):
        break
    number = number + 1

# Create the ZIP file.
print('Creating %s...' % (zipFilename))
backupZip = zipfile.ZipFile(zipFilename, 'w')

# Walk the entire folder tree and compress the files in each folder.
for foldername, subfolders, filenames in os.walk(folder):
    print('Adding files in %s...' % (foldername))
    backupZip.write(foldername)

    # Add all the files in this folder to the ZIP file.
    for filename in filenames:
        # Don't backup the ZIP files.
        if filename.startswith(os.path.basename(folder) + '_') and filename.endswith('.zip'):
            continue 
        print('Adding %s for %s...' % (filename, foldername))
        # The zip module adds files according to their absolute path file 
        # The path of added files is fixed now
        backupZip.write(os.path.join(foldername, filename))
backupZip.close()
print('Done.')