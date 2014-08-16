# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function, unicode_literals)
from greidinet import create_app
from config import Config, ProductionConfig, DevelopmentConfig, TestingConfig

app = create_app(default_settings=DevelopmentConfig)
app.run(debug=True)

