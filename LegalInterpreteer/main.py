__author__ = 'mtacer'

# import arcpy


class LegalDescription(object):
    def __init__(self, location_id, quarter_section, section_number, abstract_number, survey_name, township,
                 township_direction, range_, range_direction, footage1, footage1_direction,
                 footage2, footage2_direction, footage_corner, county_id, state_code, country):
        pass

    def type(self):
        pass

    def NAD83_latlon(self, grid):
        pass


class LocationTable(object):
    def __init__(self, connection):
        pass


class GridFeatureClass(object):
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
