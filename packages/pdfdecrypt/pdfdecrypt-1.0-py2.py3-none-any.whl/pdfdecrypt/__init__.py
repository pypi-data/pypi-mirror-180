#!/usr/bin/env python
"""
decrypt - Remove passwords from PDF documents
"""
#
# Copyright 2022 by Hartmut Goebel <h.goebel@crazy-compilers.com>
#
# This file is part of pdfdecrypt.
#
# pdfdecrypt is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# pdfdecrypt is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public
# License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with pdfdecrypt. If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: AGPL-3.0-or-later

__author__ = "Hartmut Goebel <h.goebel@crazy-compilers.com>"
__copyright__ = "Copyright 2022 by Hartmut Goebel <h.goebel@crazy-compilers.com>"
__licence__ = "GNU Affero General Public License v3 or later (AGPLv3+)"
__version__ = "1.0"

from PyPDF2 import PdfWriter, PdfReader
from logging import warn
from .i18n import _


class DecryptionError(ValueError):
    pass


def password_hook():
    import getpass
    return getpass.getpass()


def main(opts, infilename, outfilename, password_hook=password_hook):
    inpdf = PdfReader(open(infilename, 'rb'), strict=False)

    if not inpdf.is_encrypted:
        warn(_("File is not encrypted"))
    else:
        # try empty password first
        if not inpdf.decrypt(''):
            if not inpdf.decrypt(password_hook()):
                raise DecryptionError(_("Can't decrypt PDF. Wrong Password?"))

    outpdf = PdfWriter()
    outpdf.clone_document_from_reader(inpdf)
    with open(outfilename, 'wb') as outfh:
        outpdf.write(outfh)
