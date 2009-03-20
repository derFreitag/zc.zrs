##############################################################################
#
# Copyright (c) Zope Corporation.  All Rights Reserved.
#
# This software is subject to the provisions of the Zope Visible Source
# License, Version 1.0 (ZVSL).  A copy of the ZVSL should accompany this
# distribution.
#
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE
#
##############################################################################

import os
from setuptools import setup

open('setup.cfg', 'w').write("""
[bdist_egg]
exclude-source-files = true
""")

open('LICENSE.txt', 'w').write(open('ZEL.txt').read())

entry_points = """
[console_scripts]
zrsmonitor-script = zc.zrs.monitor:main
"""

version = open('zrsversion.cfg').read().strip().split()[-1]+'.eval'

import shutil
if os.path.isdir('build'):
    shutil.rmtree('build')

try:
    setup(
        name = 'zc.zrs',
        version = version,
        author = "Jim Fulton",
        author_email = "jim#zope.com",
        description = "Zope Replication Server",
        license = "Zope Evaluation License 1.0",
        keywords = "ZODB",

        packages = ['zc', 'zc.zrs'],
        include_package_data = True,
        data_files = [('.', ['README.txt', 'LICENSE.txt'])],
        zip_safe = True,
        entry_points = entry_points,
        package_dir = {'':'src'},
        namespace_packages = ['zc'],
        install_requires = ['setuptools', 'ZODB3', 'Twisted'],
        )
finally:
    os.remove('setup.cfg')
    os.remove('LICENSE.txt')
