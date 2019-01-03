"""
An example which makes a roughing pass on a mesh of
a truncated cone, and exports basic G- code.
"""
import pyactp
import trimesh

import numpy as np

if __name__ == '__main__':

    file_name = '../models/cone.stl'

    pyactp.makerough(file_name)

    curves = []
    for path in range(pyactp.getnumpaths()):
        npoints = pyactp.getnumpoints(path)
        nbreaks = pyactp.getnumbreaks(path)
        nlinkpaths = pyactp.getnumlinkpths(path)

        z = pyactp.getz(path)
        start_pos = 0
        first_z_done = False

        curves.append([])
        for brk in range(0, nbreaks):
            brkpos = pyactp.getbreak(path, brk)
            for point in range(start_pos, brkpos):
                x, y = pyactp.getpoint(path, point)

                curves[-1].append([x, y, z])
            start_pos = brkpos
            nlinkpoints = pyactp.getnumlinkpoints(path, brk)
            for linkpoint in range(0, nlinkpoints):
                x, y, z = pyactp.getlinkpoint(path, brk, linkpoint)
                curves[-1].append([x, y, z])

    # visualize the toolpaths and mesh in a pyglet window
    mesh = trimesh.load(file_name)
    viz = [trimesh.load_path(np.array(c)) for c in curves if len(c) > 0]
    viz.append(mesh)
    trimesh.Scene(viz).show()
