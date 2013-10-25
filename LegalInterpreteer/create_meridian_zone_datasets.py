__author__ = 'mtacer'

import arcpy
import os
from settings import PLS_input_gdb

class Feature_class():
    def __init__(self, ds, full_path, template, _type):
        self.ds = ds
        self.full_path = full_path
        self.template = template
        self.type = _type


class Input_data(object):
    def __init__(self, input_datasets):
        self.input_datasets = input_datasets
        self.input_feature_classes = None

    def create_input_fc(self):
        __in_fc = []
        for gdb in self.input_datasets:
            arcpy.env.workspace = gdb
            ds_list = arcpy.ListDatasets()
            for ds in ds_list:
                print 'ds: %s' % ds
                arcpy.env.workspace = os.path.join(gdb, ds)
                fc_list = arcpy.ListFeatureClasses()
                for fc in fc_list:
                    if 'section' in fc.lower():
                        _type = 'sc'
                    elif 'township' in fc.lower():
                        _type = 'ts'
                    elif 'ladesc' in fc.lower():
                        _type = 'qq'
                    else:
                        _type = None
                        print 'Unrecognizable feature class: %s' % fc
                        continue

                    full_path = os.path.join(gdb,ds,fc)
                    __in_fc.append(Feature_class(ds,full_path, None, _type ))

        self.input_feature_classes = __in_fc


class Output_data(object):

    def __init__(self, fgdb):
        self.fgdb = fgdb
        self.output_feature_classes = None

    def create_output_fc(self, _range):

        __out_fc = []
        #recreate fgdb
        if arcpy.Exists(self.fgdb):
            arcpy.Delete_management(self.fgdb)
        arcpy.CreateFileGDB_management(*os.path.split(self.fgdb))

        quarter_quarter_poly = r'\\rdsrv05\Mapping\USLandGrid\Arizona\Arizona.gdb\LandGrid\Ladesc'
        section_poly = r'\\rdsrv05\Mapping\USLandGrid\Arizona\Arizona.gdb\LandGrid\Section_Poly'
        township_poly = r'\\rdsrv05\Mapping\USLandGrid\Arizona\Arizona.gdb\LandGrid\Township_Poly'
        for i in _range:
            ds = 'Meridian_zone_%02i' % i
            ts = 'township_poly_%02i' % i
            sc = 'section_poly_%02i' % i
            qq = 'quarter_quarter_poly_%02i' % i

            d = {ts:(township_poly, 'ts'), sc:(section_poly, 'sc'), qq:(quarter_quarter_poly, 'qq')}
            # Create dataset
            print 'Creating dataset: %s' % ds
            arcpy.CreateFeatureDataset_management(self.fgdb, ds, township_poly)

            # Create feture classes
            for fc in d:
                print '\tCreating feature class: %s' % fc
                full_path = os.path.join(self.fgdb, ds)
                arcpy.CreateFeatureclass_management(full_path, fc, "POLYGON", d[fc][0])
                __out_fc.append(Feature_class(ds, full_path, d[fc][0], d[fc][1]))

        self.output_feature_classes = __out_fc

    def populate_output_fc(self, input_fc_list, output_fc_list):
        for input_fc in input_fc_list:
            pass


def list_of_meridian_zones(in_feature_class):
    pass

def append_data_to_meridian_zone(in_fc, out_fc_list):
    pass

def main():
    fgdb = r'd:\temp\fgdb_mz_usa.gdb'
    mer_zone_range = range(1,3)

    out_data = Output_data( fgdb )
    out_data.create_output_fc( mer_zone_range )

    in_data = Input_data( PLS_input_gdb )
    in_data.create_input_fc()

    for in_fc in in_data.input_feature_classes:
        append_data_to_meridian_zone(in_fc, out_data.output_feature_classes)

if __name__ == '__main__':
    main()