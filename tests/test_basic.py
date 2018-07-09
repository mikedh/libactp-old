import unittest

class ACTPTest(unittest.TestCase):
    """
    Test to make sure plumbing is hooked up
    """
    def test_rough(self):
        import pyactp
        # make sure it actually has methods
        assert hasattr(pyactp, 'makerough')

        # run the actual calculation
        pyactp.makerough('../models/cone.stl')

        path_count = pyactp.getnumpaths()
        assert path_count > 0

        # store XYZ points
        curve = []
        
        for path in range(path_count):
            npoints = pyactp.getnumpoints(path)
            nbreaks = pyactp.getnumbreaks(path)
            nlinkpaths = pyactp.getnumlinkpths(path)
            z = pyactp.getz(path)
            start_pos = 0
            
            for brk in range(0, nbreaks):
                brkpos = pyactp.getbreak(path, brk)
                for point in range(start_pos, brkpos):
                    x, y = pyactp.getpoint(path, point)
                    curve.append([x,y,z])
                start_pos = brkpos
                nlinkpoints = pyactp.getnumlinkpoints(path, brk)
                for linkpoint in range(0, nlinkpoints):
                    x, y, z = pyactp.getlinkpoint(path,
                                                  brk,
                                                  linkpoint)
        assert len(curve) > 0

if __name__ == '__main__':
    unittest.main()
