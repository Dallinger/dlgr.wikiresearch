import os
import sys
from setuptools import setup, find_packages


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


setup_args = dict(
    name='dlgr.wikiresearch',
    version="1.0.0",
    description='Demonstration of an external website as a dallinger experiment',
    url='http://github.com/Dallinger/dlgr.wikiresearch',
    maintainer='Jordan Suchow',
    maintainer_email='suchow@berkeley.edu',
    license='MIT',
    keywords=['science', 'cultural evolution', 'experiments', 'psychology'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    packages=find_packages('.'),
    package_dir={'': '.'},
    namespace_packages=['dlgr'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
    ],
    entry_points={
        'dallinger.experiments': [
            'WikiResearch = dlgr.wikiresearch.experiment:WikiResearch',
        ],
    },
)

# Read in requirements.txt for dependencies.
setup_args['install_requires'] = install_requires = []
setup_args['dependency_links'] = dependency_links = []
with open('requirements.txt') as f:
    for line in []:#f.readlines():
        req = line.strip()
        if not req or req.startswith('#'):
            continue
        if req.startswith('-e '):
            dependency_links.append(req[3:])
        else:
            install_requires.append(req)

setup(**setup_args)
