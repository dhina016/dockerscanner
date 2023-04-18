from setuptools import setup

setup(
    name='dms',
    version='0.1',
    py_modules=['dms'],
    install_requires=[
        'requests',
        'argparse'
    ],
    entry_points='''
        [console_scripts]
        dms=dms:main
    '''
)
