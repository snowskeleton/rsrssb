mkdir .tmp
cd .tmp
touch \
test_chap01.mp3 \
test_chap02.mp3 \
test_chap03.mp3 \
test_chap04.mp3 \
test_chap05.mp3 \
test_chap06.mp3 \
test_chap07.mp3 \
test_chap08.mp3 \
test_chap09.mp3 \
test_chap10.mp3 \
test_chap11.mp3

touch \
test_chap01.m4b \
test_chap02.m4b \
test_chap03.m4b \
test_chap04.m4b \
test_chap05.m4b \
test_chap06.m4b \
test_chap07.m4b \
test_chap08.m4b \
test_chap09.m4b \
test_chap10.m4b \
test_chap11.m4b

python3 ../src/main.py --title "this is really long" --domain snowskeleton.net
mv feed.xml ../ && rm -rf ../.tmp
