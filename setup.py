import setuptools
import subprocess
import setuptools.command.build_py

class BuildMake(setuptools.command.build_py.build_py):
    """
    Custom build command which just calls Makefile.
    """
    def run(self):
        # just run Makefile
        subprocess.check_call(['make', '-C', 'pyactp', 'clean'])
        subprocess.check_call(['make', '-C', 'pyactp'])
        # call super
        setuptools.command.build_py.build_py.run(self)


setuptools.setup(
    cmdclass={'build_py': BuildMake},
    name='pyactp',
    version='0.1.6',
    description='Python bindings for ACTP',
    long_description='Python bindings for the Adaptive Clearing Tool Path Library',
    url='https://github.com/mikedh/pyactp',
    author='Michael Dawson-Haggerty',
    author_email='mik3dh@gmail.com',
    license="GPL",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='actp milling toolpath',
    packages=['pyactp'],
    package_data={'pyactp': ['actp.so']}
)
