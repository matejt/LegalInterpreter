__author__ = 'mtacer'

import os

rootdir = r'm:\USLandGrid\Alberta'
rootdir = r'd:\Downloads'

for root, subFolders, files in os.walk(rootdir):
    print 'Root: %s' % root
    print 'subFolders: %s' % subFolders
    print 'files: %s' % files

    # for folder in subFolders:
    #     outfileName = rootdir + "/" + folder + "/py-outfile.txt" # hardcoded path
    #     folderOut = open( outfileName, 'w' )
    #     print "outfileName is " + outfileName
    #
    #     for file in files:
