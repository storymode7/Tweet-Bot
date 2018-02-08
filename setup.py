from setuptools import setup

setup(
        name='pyTwurl',
        version='0.1',
        py_modules=['post'],
        install_requires=[
            'Click',
            'python-twitter'
        ],
        entry_points='''
            [console_scripts]
            pyTwurl=post:setUpdate
        ''',
)
# use pip install --editable . to install in venv
