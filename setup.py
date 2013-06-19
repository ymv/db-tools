from setuptools import setup
setup(
    name = "Database tools",
    version = "0.0.1",
    packages = ['dbtools'],
    entry_points={
        'console_scripts': ['myns = dbtools.myns:main']
    }
)
