==========================
pdfdecrypt
==========================

-------------------------------------
Remove passwords from PDF documents
-------------------------------------

:Author:    Hartmut Goebel <h.goebel@crazy-compilers.com>
:Version:   Version 0.1
:Copyright: 2022 by Hartmut Goebel
:Licence:   GNU Affero General Public License v3 or later (AGPLv3+)
:Homepage:  https://pdfdecrypt.readthedocs.io/

``pdfdecrypt`` is a command line tool and a Python library to
remove passwords from PDF documents.  It will read the encrypted
document, ask for the password and write the decrypted document
without touching any internal structure.


Requirements when Installating from Source
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to install `pdfdecrypt` from source, make sure you have the
following software installed:

* `Python 3`__  (tested with 3.8),
* `pip`__ for installation, and
* `PyPDF2`__.

__ http://www.python.org/download/
__ https://pypi.org/project/pip
__ http://mstamy2.github.io/PyPDF2/


:Hints for installing on Windows: Following the links above you will
   find .msi and .exe-installers. Simply install them and continue
   with `installing pdfdecrypt`_.

:Hints for installing on GNU/Linux: Most current GNU/Linux distributions
   provide packages for the requirements. Look for packages names like
   `python-pypdf2`. Simply install them and
   continue with `installing pdfdecrypt`_.

:Hint for installing on other platforms: Many vendors provide Python.
   Please check your vendors software repository. Otherwise please
   download Python 3.8 (or any higher version from the 3.x series) from
   http://www.python.org/download/ and follow the installation
   instructions there.

   If the commands below fail due to module `pip` not found,
   please install it using::

     python -m ensurepip


Installing pdfdecrypt
---------------------------------

If your system has network access installing `pdfdecrypt`
is a breeze::

  pip install pdfdecrypt


If you  downloaded and unpacked `pdfdecrypt` just run::

  python -m pip install .


Without network access download `pdfdecrypt` from
http://pypi.python.org/pypi/pdfdecrypt and run::

   pip install pdfdecrypt-*.tar.gz


For more details like custom installation locations
please refer to
`the official end user guide for installing Python packages
<https://docs.python.org/3/installing/>`__.
