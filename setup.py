from setuptools import setup

setup(
    name='andersoldahl.com',
    description='My personal website.',
    author='Anders Dahl',
    author_email='andersoldahl@gmail.com',
    packages=['andersoldahl'],
    install_requires=[
        'flask',
        'Frozen-Flask'
    ],
    include_package_data=True,
)
