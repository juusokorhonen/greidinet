# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function, unicode_literals)

from greidinet import create_app
app = create_app("config.py")
app.run(debug=True)

