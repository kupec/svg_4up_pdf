#!/bin/bash

python3 gen4.py "$@" | cairosvg /dev/stdin > out.pdf
