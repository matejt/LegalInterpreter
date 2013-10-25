__author__ = 'mtacer'

import arcpy
import os

ws = r"\\rdsrv05\Mapping\USLandGrid\Arizona\Arizona.gdb"
arcpy.env.workspace = ws
ds_list = arcpy.ListDatasets()
for ds in ds_list:
    print 'ds: %s' % ds
    arcpy.env.workspace = os.path.join(ws, ds)
    fc_list = arcpy.ListFeatureClasses()
    for fc in fc_list:
        print fc