from setuptools import setup, find_packages

setup(
name='dockerscanner',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'dockerscanner = dockerscanner.main:main'
        ]
    },
    install_requires=[
        'requests',
        'argparse',
    ],
    author='dhina016',
    description='A Docker misconfiguration scanner',
    url='https://github.com/dhina016/docker-misconfig-scanner',
)
