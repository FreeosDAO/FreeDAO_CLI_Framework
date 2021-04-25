from setuptools import setup

setup(
    name = "freedao",
    package='freedao',
    install_requires = ['pytest','ecdsa'],
    version = '0.1.0',
    description = 'FreeOS Automation and Testing Framework, created by Shahid',
    author = "Mohammad Shahid Siddiqui",
    author_email = 'mssiddiqui.nz@gmail.com',
    url = 'https://github.com/shahidnz',
    keywords = ['freeos', 'freedao', 'eos', 'proton', 'blockchain'],
    classifiers = [
        'Development Status :: in progress',
        'Environment :: Console',
        'Programming Language :: Python'
    ],
)