__author__ = 'mtacer'

import zipfile

f = 'd:\\temp\\d_DDDSK.TXT'
zf = 'd:\\temp\\d_DDDSK.zip'
zf = zipfile.ZipFile(zf, mode='w')
zf.write(f)
zf.close()
