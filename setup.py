"""
    This file is part of planetsentangled by terrabela
    Author: Marcelo Francis Máduar
"""

from setuptools import setup
from setuptools import find_packages


setup(
    # Project
    name = 'planetsentangled',
    version = '0.0.1-dev',
    
    # Sources
    packages = find_packages(),
    package_data = {
        'planetsentangled': [
            'resources/README.md',
            'resources/swefiles/*'
        ],
    },
    
    # Dependencies
    install_requires = ['pyswisseph==2.00.00-2'],
    
    # Metadata
    description = 'Python library for long-term graphing of planetary aspects in Traditional Astrology',
    url = 'https://github.com/terrabela/planetsentangled',
    keywords = ['Astrology', 'Traditional Astrology'],
    license = 'MIT',
    
    # Authoring
    author = 'João Ventura, Marcelo Francis Máduar',
    author_email = 'maduar(at)vivaldi.net',
    
    # Classifiers
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 1 - Alpha',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ], 
)
