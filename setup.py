#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_packages, setup


with open('README.md') as readme_file:
    readme = readme_file.read()


with open('HISTORY.md') as history_file:
    history = history_file.read()


install_requires = [
    'graphviz>=0.9,<1',
]


examples_require = [
    'matplotlib>=2.2.2,<3.2.2',
    'mlprimitives>=0.2.5,<0.3',
    'boto3>=1.14,<1.14.45',
    'botocore<1.17.45,>=1.17.44',
    'jupyter==1.0.0',
    'docutils<0.16,>=0.10',
    'baytune>=0.3.0,<0.4',
]


tests_require = [
    'pytest>=3.4.2',
    'pytest-cov>=2.6.0',
    'mlprimitives>=0.2,<0.3',
    'setuptools>=41.0.0',
    'numpy<1.17',
    'rundoc>=0.4.3',
    'prompt-toolkit>=2.0,<3.0',
]


setup_requires = [
    'pytest-runner>=2.11.1',
]


development_requires = [
    # general
    'bumpversion>=0.5.3,<0.6',
    'pip>=9.0.1',
    'watchdog>=0.8.3,<0.11',

    # docs
    'm2r>=0.2.0,<0.3',
    'Sphinx>=1.7.1,<3',
    'sphinx_rtd_theme>=0.2.4,<0.5',
    'ipython>=6.5.0',
    'autodocsumm>=0.1.10',

    # style check
    'flake8>=3.7.7,<4',
    'isort>=4.3.4,<5',

    # fix style issues
    'autoflake>=1.1,<2',
    'autopep8>=1.4.3,<2',

    # distribute on PyPI
    'twine>=1.10.0,<4',
    'wheel>=0.30.0',

    # Advanced testing
    'coverage>=4.5.1,<6',
    'tox>=2.9.1,<4',

    # Documentation style
    'doc8>=0.8.0',
    'pydocstyle>=3.0.0'
]


setup(
    author='MIT Data To AI Lab',
    author_email='dailabmit@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Pipelines and primitives for machine learning and data science.",
    extras_require={
        'dev': development_requires + tests_require + examples_require,
        'test': tests_require + examples_require,
        'examples': examples_require,
    },
    include_package_data=True,
    install_requires=install_requires,
    keywords='auto machine learning classification regression data science pipeline',
    license="MIT license",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    name='mlblocks',
    packages=find_packages(include=['mlblocks', 'mlblocks.*']),
    setup_requires=setup_requires,
    test_suite='tests',
    tests_require=tests_require,
    url='https://github.com/HDI-Project/MLBlocks',
    version='0.3.5.dev0',
    zip_safe=False,
)
