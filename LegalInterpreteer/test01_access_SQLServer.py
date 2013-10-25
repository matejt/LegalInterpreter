__author__ = 'mtacer'

import arcpy

# table = r'D:\ConnFiles\RDSQLDEV_Reporting.sde\Reporting.dbo.Location'
table = r'D:\ConnFiles\RDSQLDEV_Reporting.sde\Reporting.dbo.vw_LocationData'

fields = arcpy.ListFields(table)
print fields

# for field in fields:
#     print field.name
#
# with arcpy.da.SearchCursor(table, "*") as cursor:
#     for i,row in enumerate(cursor,1):
#         if i > 5: break
#         print("{0}, {1}, {2}".format(row[0], row[1], row[2]))