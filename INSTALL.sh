#!/bin/bash

if [[ -x '$(command -v python3)' ]]
then
    python3 -m pip install --user - -upgrade pip
    python3 -m pip install colorama==0.4.5
    python3 -m pip install Columnar==1.4.1
    python3 -m pip install exif==1.3.5
    python3 -m pip install lifehacks.colour==1.0.1
    python3 -m pip install lifehacks.metaclasses==1.0.0
    python3 -m pip install Pillow==9.2.0
    python3 -m pip install plum-py==0.8.2
    python3 -m pip install simple-term-menu==1.5.0
    python3 -m pip install toolz==0.12.0
    python3 -m pip install wcwidth==0.2.5
    python3 -m venv -venv 
    source .venv/bin/activate
    python3 photo_file_handling.py
    echo "Done!"
else 
    echo "ERROR:
    need to install the latest version of python3"