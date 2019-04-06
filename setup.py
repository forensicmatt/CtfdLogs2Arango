from setuptools import setup

setup(
    name='ctfd2arango',
    version="0.0.1",
    description='Tools for ingesting ctfd logs into ArangoDB.',
    author='Matthew Seyer',
    url='https://github.com/forensicmatt/CtfdLogs2Arango',
    license='Apache License (2.0)',
    packages=[
        'python-arango'
    ],
    python_requires='>=3',
    install_requires=[],
    scripts=[
        'scripts/ctfd_2_arango.py'
    ]
)