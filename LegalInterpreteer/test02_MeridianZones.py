__author__ = 'mtacer'

file_name = r'd:\Projects\_00_Data\_USstates\MeridianZones.txt'

file = open(file_name,'r')
for line in file:
    line = line[:-1]
    if not line: continue
    la = [a.strip() for a in line.split(' ')]
    # print la
    if len(la[2:]) > 1:
        name = ' '.join(la[2:])
    else:
        name = la[2]
    print 'Code: %s, Zone: %s, Name: %s' % (la[0], la[1], name)