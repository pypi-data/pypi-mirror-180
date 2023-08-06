from setuptools import find_packages, setup
setup(
    name='Pigeons Game Engine',
    packages=find_packages(include=['pgengine']),
    version='0.1.0',
    description='Game Engine for Python called Pigeons Game Engine',
    author='Damandes',
    license='MIT',
    install_requires=['keyboard'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)