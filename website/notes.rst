==========================
Class Notes
==========================

Numpy
~~~~~~~~

Links:
    * `Numpy documentation`_
    * `Numpy for Matlab users`_
    * `Numpy for Matlab users (2)`_
    * `Numpy for R users`_
    * `Numpy examples`_
    * The `Numpy Book`_ has probably too much detail, but it's a good reference.

.. _`Numpy documentation`: http://docs.scipy.org/doc/
.. _`Numpy for Matlab users`: http://mathesaurus.sourceforge.net/matlab-numpy.html
.. _`Numpy for Matlab users (2)`: http://www.scipy.org/NumPy_for_Matlab_Users
.. _`Numpy for Matlab users`: http://mathesaurus.sourceforge.net/matlab-numpy.html
.. _`Numpy for R users`: http://mathesaurus.sourceforge.net/r-numpy.html
.. _`Numpy examples`: http://www.scipy.org/Numpy_Example_List
.. _`Numpy Book`: http://www.tramy.us/

Numerical Representations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See the paper `A Remarkable Example of Catastrophic Cancellation Unravelled`_ for an illustration of catastrophic cancellation.

.. _`A Remarkable Example of Catastrophic Cancellation Unravelled`: http://www.springerlink.com/content/4hqxfemn24a0m3ep/

Software Carpentry: Debugging
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Links:
    * The software carpentry website on debugging_ has some useful tips on debugging (called Rules).

You might want to browse through the software carpentry website as it is the source of inspiration for this module.

.. _debugging: http://www.swc.scipy.org/lec/debugging.html

Software Carpentry: Testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nose testing framework
    * Nose_
    * `Show Me Do Video`_ about nose
    * MTEST_ - A unit test framework for MATLAB code
    
.. _Nose: http://somethingaboutorange.com/mrl/projects/nose/
.. _`Show Me Do Video`: http://showmedo.com/videos/video?name=2910010&fromSeriesID=291
.. _MTEST: http://blogs.mathworks.com/steve/2009/02/03/mtest-a-unit-test-harness-for-matlab-code/

If you install one of the bigger Python distributions like enthought, then nose should already be installed.

Software Carpentry: Version Control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Links
    * `SVN Book`_
    * `Visual Intro to Version Control`_
    * `Show Me Do`_ (screencast) on SVN. This is Linux based, but works on Mac OS and Windows.

.. _`SVN Book`: http://svnbook.red-bean.com
.. _`Visual Intro to Version Control`: http://betterexplained.com/articles/a-visual-guide-to-version-control/
.. _`Show Me Do`: http://showmedo.com/videos/series?name=bfNi2X3Xg

Software
    * `Subversion`_ (for any platform, command-line interface)
    * `kdesvn`_ (for Linux: this was what I demonstrated in class)
    * `TortoiseSVN`_ (for Windows)
    * `Versions`_ (for Mac OS, commercial software)
    * `SCPlugin`_ (for Mac OS, open source)

.. _`TortoiseSVN`: http://tortoisesvn.tigris.org/
.. _`Subversion`: http://subversion.tigris.org/
.. _`kdesvn`: http://kdesvn.alwins-world.de/
.. _`Versions`: http://versionsapp.com/
.. _`SCPlugin`: http://scplugin.tigris.org/

Lab Lecture 1
~~~~~~~~~~~~~

For this class, we are using *Python*. Most of my material will be based on Python 2.5. Version 2.6, which came out recently and hasn't yet made it into the mainstream, is also fine. However, version 3 of Python is **not recommended**. In particular, many of the libraries that will be introduced in the practical sessions do not support Python 3 yet.

Links for Python:
    * Python_ 
    * `Python Docs`_
    * `Enthought Python Distribution`_
    * `Python(x,y)`_

.. _Python: http://www.python.org
.. _Python Docs: http://docs.python.org
.. _Enthought Python Distribution: http://www.enthought.com/products/epd.php
.. _Python(x,y): http://www.pythonxy.com/

If you are using Linux, then I recommend you get the Python packages that are standard for your distribution. Be sure to look for the numpy and scipy packages as well (in ubuntu, they're called *python-numpy* and *python-scipy*). *Python-matplotlib* includes the very useful *matplotlib* library.

Enthought Python Distribution is a Python distribution specially targetted for scientific applications. It's a commercial product, but free for students (like you). All the sotware it includes is open-source, but it's nice to have a single distribution (especially if you are not using a Linux distribution that does that work for you).  Python(x,y) is similar, but for Windows only (*Linux version available soon*, but on Linux, follow the advice above and use your Linux distribution's installation).  

Mac OS X includes a version of Python with the numpy & scipy libraries (they're, I'm told, on a separate CD). If you are using 10.5, this should suffice for this course. If you are using an older version, you might consider upgrading using one of the distributions above (like Enthought's)

Consider installing *ipython*: it's a much improved Python shell (the default version is very limited). If you are using linux, then your distribution should have a package for it (Ubuntu calls it simply *ipython*). On Mac OS 10.5, check out this document_.

.. _document : http://www.brianberliner.com/2008/04/18/ipython-on-mac-os-x-105-leopard/

Python IDEs (integrated development environments):
    * Eclipse_ (see also PyDev_)
    * Stani_
    * DrPython_
    * KomodoIDE_
    * Ipython_
    * MacPython_ (for Mac OS X)
    * Also, you can use editors like Emacs and vi(m), of course

.. _Eclipse: http://www.eclipse.org/
.. _Stani: http://www.stani.be/
.. _PyDev: http://pydev.sourceforge.net/
.. _DrPython: http://drpython.sourceforge.net/
.. _KomodoIDE: http://www.activestate.com/Products/komodo_ide/index.mhtml
.. _Ipython: http://ipython.scipy.org/moin/
.. _MacPython: http://wiki.python.org/moin/MacPython


