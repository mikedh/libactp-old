"""
An example which makes a roughing pass on a mesh of
a truncated cone, and exports basic G- code.
"""
import pyactp

with open("test.tap", 'w') as f_out:
    f_out.write("G90 G21 G17\n")
    pyactp.makerough('../models/cone.stl')


    for path in range(pyactp.getnumpaths()):
        npoints = pyactp.getnumpoints(path)
        nbreaks = pyactp.getnumbreaks(path)
        nlinkpaths = pyactp.getnumlinkpths(path)

        z = pyactp.getz(path)
        start_pos = 0
        first_z_done = False
      
        for brk in range(0, nbreaks):
            brkpos = pyactp.getbreak(path, brk)
            for point in range(start_pos, brkpos):
                x, y = pyactp.getpoint(path, point)
                #feed(x, y, z)
                curve.append([x,y,z])
                if first_z_done == False:
                    f_out.write("G0 X" +
                                str(' %.4f' % x) + " Y " +
                                str(' %.4f' % y) + " Z " +
                                str(' %.4f' % z) + "\n")
                    first_z_done = True
                else:
                    f_out.write("G1 X" + str(' %.4f' % x) +
                                " Y " + str(' %.4f' % y) + "\n")
            start_pos = brkpos
            nlinkpoints = pyactp.getnumlinkpoints(path, brk)
            for linkpoint in range(0, nlinkpoints):
                x, y, z = pyactp.getlinkpoint(path, brk, linkpoint)
                #rapid(x, y, z)
                f_out.write("G0 X" +
                            str(' %.4f' % x) + " Y " +
                            str(' %.4f' % y) + " Z " +
                            str(' %.4f' % z) + "\n")
    f_out.write("M2\n")
