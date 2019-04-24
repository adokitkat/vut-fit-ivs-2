#!/bin/sh
mkdir -p ../installer/usr/share/pasiemepytony 2>/dev/null
cp  main.py ../installer/usr/share/pasiemepytony/main.py && chmod +x ../installer/usr/share/pasiemepytony/main.py
cp  mathematica.py ../installer/usr/share/pasiemepytony/mathematica.py
cp  gui.py ../installer/usr/share/pasiemepytony/gui.py
mkdir -p ../installer/usr/local/bin 2>/dev/null
ln -sf /usr/share/pasiemepytony/main.py ../installer/usr/local/bin/kalc00lacka
mkdir ../installer/tmp 2>/dev/null
cp requirements.txt ../installer/tmp/requirements.txt
chmod +x ../installer/DEBIAN/postinst
dpkg-deb --build ../installer/ ../installer/kalc00lacka.deb
