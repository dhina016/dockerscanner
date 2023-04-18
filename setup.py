from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess

class PostInstallCommand(install):
    def run(self):
        install.run(self)
        subprocess.call(['dms', 'update'])

setup(
    name='dms',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'dms = dms.main:main',
        ],
    },
    install_requires=[
        'requests',
        'argparse',
    ],
    cmdclass={
        'install': PostInstallCommand,
    },
    author='dhina016',
    description='A Docker misconfiguration scanner',
    url='https://github.com/dhina016/docker-misconfig-scanner',
)
