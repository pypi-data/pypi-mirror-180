from setuptools import find_packages, setup
setup(
    name='jackals',
    packages=find_packages(include=['jackals']),
    version='0.1.5',
    description='Typed Panda-like Dataframe',
    author='Pietro Bonazzi',
    license='MIT',
    install_requires=[],
    tests_require=['unittest'],
    test_suite='test',
)
