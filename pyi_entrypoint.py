#!/usr/bin/env python3
import sys
from src.rsrssb import main

try:
    sys.exit(main.cli_main())
except KeyboardInterrupt:
    sys.exit(print('\nAbort mission.'))
