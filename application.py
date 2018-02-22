#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from app import create_app
from app import scheduler

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == '__main__':
    scheduler.schedule()
    app.run()
