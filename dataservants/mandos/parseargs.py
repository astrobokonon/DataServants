# -*- coding: utf-8 -*-
#
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
#  Created on Tue Feb 27 12:44:35 2018
#
#  @author: rhamilton

from __future__ import division, print_function, absolute_import


def extraArguments(parser):
    """ADDITIONAL command line arguments that Mandos will use.

    Implies that they already contain the default set so there's no
    setup of the parser details/format/whatever.

    If there are none, it just returns the parser unchanged.
    """

    return parser
