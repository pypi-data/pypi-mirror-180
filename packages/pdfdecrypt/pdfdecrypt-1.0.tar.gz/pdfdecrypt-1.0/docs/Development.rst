Development
===============================

The source of |pdfdecrypt| and its siblings is maintained at
`GitLab <https://gitlab.com/pdftools/>`_.
Patches and pull-requests are hearty welcome.

* Please submit bugs and enhancements to the `Issue Tracker
  <https://gitlab.com/pdftools/pdfdecrypt/issues>`_.

* You may browse the code at the
  `Repository Browser
  <https://gitlab.com/pdftools/pdfdecrypt>`_.
  Or you may check out the current version by running ::

    git clone https://gitlab.com/pdftools/pdfdecrypt.git


Seting up a `pdfdecrypt` Development Environment
--------------------------------------------------

Create a virtual environment somewhere. Lets call it `_venv`::

   python -m venv _venv

Activate our environment::

  source _venv/bin/activate

Install packages required for development::

  python -m pip install -r requirements.txt

Install `pdfdecrypt` in editable mode (i.e. setuptools "develop mode")::

  python -m pip install -e .

Going back to your non-virtual environment::

  deactivate

Run `pdfdecrypt` without activating the virtual environment::

  _venv/bin/pdfdecrypt …


See `Virtual Environments and Packages`__ tutorial
in the official Python documentation for more details.

__ https://docs.python.org/3/tutorial/venv.html


.. include:: _common_definitions.txt


