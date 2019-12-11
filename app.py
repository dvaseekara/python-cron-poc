#!/usr/bin/env python3

import sys
from datetime import datetime


def main():
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	print("Kron Test - Current Time =", current_time)

if __name__ == "__main__":
    sys.exit(main())