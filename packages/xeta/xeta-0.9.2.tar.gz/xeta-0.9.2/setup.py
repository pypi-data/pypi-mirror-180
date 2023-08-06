# -*- coding: utf-8 -*-
from setuptools import setup
from pathlib import Path

setup(**{
    'name': 'xeta',
    'version': '0.9.2',
    'description': 'Official test client',
    'long_description': (Path(__file__).parent/'README.md').read_text(),
    'long_description_content_type': 'text/markdown',
    'author': 'Xeta',
    'author_email': 'contact@xeta.com',
    'url': 'https://github.com/xetareality/xeta-py',
    'packages': ['xeta'],
    'install_requires': [],
})