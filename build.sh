#! /bin/bash

#creating executable
"pyinstaller" --onefile -i "media/icon.ico" --name="Logical Clock" --noconsole LogicalClock.py

#copying Logical Clock executable to project root
cp "dist/Logical Clock" .

#removing Logical Clock.spec file created by pyinstaller
rm "Logical Clock.spec"

#removing build folder created by pyinstaller
rm -r build

#removing dist folder created by pyinstaller
rm -r dist
