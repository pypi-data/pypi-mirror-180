#!/usr/bin/env python
"""
pdfdecrypt.cmd - Remove passwords from PDF documents
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

from . import main, __version__, DecryptionError
from .i18n import _

import PyPDF2.errors


def run():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version',
                        version='%(prog)s ' + __version__,
                        help=_("show program's version number and exit"))
    parser.add_argument('infile', metavar=_("InputFile"),
                        help=_("name of pdf file to decrypt"))
    parser.add_argument('outfile', metavar=_("OutputFile"),
                        help=_("name of file to write decrypted pdf document"))

    args = parser.parse_args()

    try:
        main(args, args.infile, args.outfile)
    except (IOError, DecryptionError) as e:
        raise SystemExit(str(e))
    except PyPDF2.errors.PdfReadError as e:
        parser.error(_("The input-file is either corrupt or no PDF at all: %s")
                     % e)


if __name__ == '__main__':
    run()
