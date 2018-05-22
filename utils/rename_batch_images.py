import os

# Create a list of files from the current directory who's last 4 characters
# as lowercase are either '.jpg'

dirname = './pedestrains'
files = [f for f in os.listdir(dirname) if f[-4:].lower() == '.jpg']

DRYRUN = False

for (index, filename) in enumerate(files):
    extension = os.path.splitext(filename)[1]

    # Define new file name pattern
    newname = "0000%0d%s" % (index, extension)

    if os.path.exists(newname):
        print "Cannot rename %s to %s, already exists" % (filename, newname)
        continue

    if DRYRUN:
        print "Would rename %s to %s" % (filename, newname)
    else:
        print "Renaming %s to %s" % (filename, newname)
        os.rename(dirname + "/" + filename, dirname + "/" + newname)