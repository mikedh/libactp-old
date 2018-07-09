import pyactp
import trimesh

if __name__ == '__main__':
    file_name = '../models/isogrid.stl'

    # load the mesh
    mesh = trimesh.load(file_name)

    # set a bunch of parameters, badly
    # probably the tool radius?
    pyactp.settoolflatrad(2)

    # presumably the minimum Z level to step down to
    pyactp.setminz(mesh.bounds[0][2] - 2)

    # possibly the top of parts, the "clearance plane" height
    pyactp.setclearcuspheight(mesh.bounds[1][2])

    # possibly the distance in Z to traverse every step
    pyactp.setstepdown(2)
    
    # make a tool path
    pyactp.makerough(file_name)

    curves = []
    npaths = pyactp.getnumpaths()
    for path in range(0, npaths):
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
                curves[-1].append([x,y,z])
            start_pos = brkpos
            nlinkpoints = pyactp.getnumlinkpoints(path, brk)
            for linkpoint in range(0, nlinkpoints):
                x, y, z = pyactp.getlinkpoint(path, brk, linkpoint)
                curve.append([x, y, z])

    # visualize the toolpaths and mesh in a pyglet window
    viz = [trimesh.load_path(c) for c in curves]
    viz.append(mesh)
    trimesh.Scene(viz).show()
