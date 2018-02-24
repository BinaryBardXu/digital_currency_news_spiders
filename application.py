#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from app import scheduler_runner
from config import profiles
from app.utils import pid

active_profile = os.getenv('profile') or 'default'

config = profiles[active_profile]

if __name__ == '__main__':
    pid.write()
    scheduler_runner.run()
