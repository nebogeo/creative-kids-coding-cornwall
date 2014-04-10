
#!/bin/bash

sudo apt-get -y install geany
cp geany.desktop ~/Desktop/geany.desktop
cp minecraft.desktop ~/Desktop/minecraft.desktop
cd ~
wget https://github.com/nebogeo/dbscode/archive/master.zip
unzip master.zip
cd ./dbscode-master
./install.sh
cd ~
wget https://s3.amazonaws.com/assets.minecraft.net/pi/minecraft-pi-0.1.1.tar.gz
tar -xvzf minecraft-pi-0.1.1.tar.gz
