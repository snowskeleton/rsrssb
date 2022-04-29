DEST="/usr/local/bin/rsrssb"
LIB="/usr/lib/rsrssb"

#may need to create directory first. if so, probably also have to add it to PATH
#sudo mkdir ${LIB}

#uncomment to remove previous installation
# sudo rm -rf ${LIB}
# sudo rm -rf ${DEST}

#comment out to not install (acts as a complete uninstall if paired with the above)
sudo cp -r ../../rsrssb ${LIB}
sudo ln -s ${LIB}/src/main.py ${DEST}
sudo chmod 755 ${DEST}
