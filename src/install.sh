#!/usr/bin/env bash
DEST="/usr/local/bin/rsrssb"
LIB="/usr/lib/rsrssb"

while getopts u flag; do
  update=1
done
while getopts r flag; do
  remove=1
done


#may need to create directory first. if so, probably also have to add it to PATH
#sudo mkdir ${LIB}

if [[ $update -eq 1 ]]; then
  printf 'git: '
  git stash
  printf 'git: '
  git pull
  sudo rm -rf ${LIB}
  sudo rm -rf ${DEST}
fi

if [[ $remove -ne 1 ]]; then
  sudo cp -r $(pwd) ${LIB}
  sudo ln -s ${LIB}/src/main.py ${DEST}
  sudo chmod 755 ${DEST}
  echo Finished
fi
