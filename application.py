#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from app import scheduler_runner
from config import profiles

active_profile = os.getenv('profile') or 'default'

config = profiles[active_profile]


if __name__ == '__main__':
    scheduler_runner.run()
