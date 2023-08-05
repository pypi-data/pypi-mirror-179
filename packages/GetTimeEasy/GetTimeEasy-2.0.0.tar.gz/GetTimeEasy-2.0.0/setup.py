from setuptools import setup

setup(
    name='GetTimeEasy',
    packages=['GetTimeEasy'],
    version='2.0.0',
    license='MIT',
    description='time and date library',
    author='Luka',
    author_email='app6onpython@gmail.com',
    keywords=['GetTimeEasy', 'gettimeeasy', 'Gettimeeasy', 'Get Time Easy'
              'get time easy', 'Get time easy', 'Get', 'get', 'Time', 'time', 'Easy', 'easy'],
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ]
)

# python setup.py sdist
# twine upload --skip-existing dist/*