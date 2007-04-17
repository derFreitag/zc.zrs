##############################################################################
#
# Copyright (c) 2002 Zope Corporation.  All Rights Reserved.
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
"""Set's up the reactor used by zrs
"""

import atexit, os, threading

if 'GLADE_REACTOR' in os.environ:
    import twisted.manhole.gladereactor
    twisted.manhole.gladereactor.install()

from twisted.internet import reactor

thread = threading.Thread(target=lambda : reactor.run(False))
thread.setDaemon(True)
thread.start()

def _shutdown(event):
    reactor.stop()
    event.set()

def shutdown():
    event = threading.Event()
    reactor.callFromThread(_shutdown, event)
    event.wait()

atexit.register(shutdown)
