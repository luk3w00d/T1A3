#!/bin/bash

cp -r poa/usr/local/bin
chmod +x /usr/local/bin/poa/RUN.sh
ln -s /usr/local/bin/poa/RUN.sh /usr/local/bin/pm
python3 -m pip install --user - -upgrade pip
pip install colorama==0.4.5
pip install Columnar==1.4.1
pip install exif==1.3.5
pip install lifehacks.colour==1.0.1
pip install lifehacks.metaclasses==1.0.0
pip install Pillow==9.2.0
pip install plum-py==0.8.2
pip install simple-term-menu==1.5.0
pip install toolz==0.12.0
pip install wcwidth==0.2.5
python3 -m venv -venv 
source .venv/bin/activate
echo "Done!"