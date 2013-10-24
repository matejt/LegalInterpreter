__author__ = 'mtacer'

import arcpy
import datetime

class Field():
    def __init__(self, name, value):
        self.name = name
        self.value = value

class LocationRecord(object):

    # represents one row in a table
    def __init__(self, field_list, value_list):
        self.fields = []
        for i, field_def in enumerate(field_list):
            field = Field(field_def.name, value_list[i])
            self.fields.append(field)
            # setattr(self,field.name, value_list[i])

    def type(self):
        pass

    def NAD83_latlon(self, grid):
        pass


class LocationTable(object):
    def __init__(self, sde_conn, where_clause=''):
        self.sde_conn = sde_conn
        self.where_clause = where_clause
        self.field_list = arcpy.ListFields(self.sde_conn)

    def records(self):
        records = []
        with arcpy.da.SearchCursor(self.sde_conn, "*", self.where_clause) as cursor:
            print 'returns only first 10.000 records [testing]'
            for i,row in enumerate(cursor):
                if i > 10000: break
                records.append(LocationRecord(self.field_list, row))
        return records


class GridFeatureClass(object):
    __gis_workspace__ = 'SANDBOX'
    __table__ = 'GGADMIN.TC_LINEAR_DATA'

    def __init__(self):
        pass

    def get_feature(self, legal_description):
        pass


class PLS_Grid(GridFeatureClass):
    def __init__(self):
        super(PLS_Grid, self).__init__()


class Texas_Grid(GridFeatureClass):
    def __init__(self):
        super(Texas_Grid, self).__init__()


class Canada_Dominian_LS_Grid(GridFeatureClass):
    def __init__(self):
        super(Canada_Dominian_LS_Grid, self).__init__()


class Canada_British_Columbia_Grid(GridFeatureClass):
    def __init__(self):
        super(Canada_British_Columbia_Grid, self).__init__()


class Carter_Kentucky_Grid(GridFeatureClass):
    def __init__(self):
        super(Carter_Kentucky_Grid, self).__init__()


class Carter_Tennessee_Grid(GridFeatureClass):
    def __init__(self):
        super(Carter_Tennessee_Grid, self).__init__()


if __name__ == '__main__':
    pass


if __name__ == '__main__':
    print datetime.datetime.now(), 'reading data...'
    table = r'D:\ConnFiles\RDSQLDEV_Reporting.sde\Reporting.dbo.vw_LocationData'
    loc_table = LocationTable(table)
    records = loc_table.records()
    print datetime.datetime.now()
    for i, record in enumerate(records,1):
        if i > 5: break
        print i
        for j, field in enumerate(record.fields,1):
            print '\t%3i. %s | %s' % (j, field.name.ljust(30), str(field.value).strip().rjust(30))
