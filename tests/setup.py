from setuptools import find_packages, setup
setup(
    name='coolrsa',
    packages=find_packages(include=['coolrsa']),
    version='0.1.0',
    description='YYY',
    author='E',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
