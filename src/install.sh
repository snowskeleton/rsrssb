DEST="/usr/local/bin/rsrssb"
LIB="/usr/lib/rsrssb"

while getopts u; do
  update=1
done
while getopts r; do
  remove=1
done


#may need to create directory first. if so, probably also have to add it to PATH
#sudo mkdir ${LIB}

if [[ $update -eq 1 ]]; then
  git stash && git pull
  sudo rm -rf ${LIB}
  sudo rm -rf ${DEST}
fi

#comment out to not install (acts as a complete uninstall if paired with the above)
if [[ $remove -ne 1 ]]; then
  sudo cp -r ../../rsrssb ${LIB}
  sudo ln -s ${LIB}/src/main.py ${DEST}
  sudo chmod 755 ${DEST}
fi
