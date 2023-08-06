# based on https://github.com/pypa/sampleproject
# MIT License

from io import open
from os import path

# Always prefer setuptools over distutils
from setuptools import find_namespace_packages
from setuptools import setup

import versioneer

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='asreview-insights',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Insight tools for the ASReview project',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/asreview/asreview-insights',
    author='ASReview LAB developers',
    author_email='asreview@uu.nl',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='asreview plot insights',
    packages=find_namespace_packages(include=['asreviewcontrib.*']),
    install_requires=[
        "numpy",
        "matplotlib",
        "asreview>=1,<2",
    ],
    extras_require={},
    entry_points={
        "asreview.entry_points": [
            "plot = asreviewcontrib.insights.entrypoint:PlotEntryPoint",
            "metrics = asreviewcontrib.insights.entrypoint:MetricsEntryPoint",
        ]
    },
    project_urls={
        'Bug Reports': "https://github.com/asreview/asreview-insights/issues",
        'Source': "https://github.com/asreview/asreview-insights",
    },
)
