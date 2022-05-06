trap "rm -rf ../.tmp" EXIT

mkdir .tmp
cd .tmp
touch \
'test_chap 01.mp3' \
'test_chap 02.mp3' \
'test_chap 03.mp3' \
'test_chap 04.mp3' \
'test_chap 05.mp3' \
'test_chap 06.mp3' \
'test_chap 07.mp3' \
'test_chap 08.mp3' \
'test_chap 09.mp3' \
'test_chap 10.mp3' \
'test_chap 11.mp3'

touch \
'test_chap 01.m4b' \
'test_chap 02.m4b' \
'test_chap 03.m4b' \
'test_chap 04.m4b' \
'test_chap 05.m4b' \
'test_chap 06.m4b' \
'test_chap 07.m4b' \
'test_chap 08.m4b' \
'test_chap 09.m4b' \
'test_chap 10.m4b' \
'test_chap 11.m4b'

python3 ../src/main.py \
--title "Ceci nes pas une title" \
--domain snowskeleton.net \
-y \
--audible-cli-data ../library.tsv \
--input ../list.txt \
-s

mv feed.xml ../ && rm -rf .tmp
