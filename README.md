Really Simple RSS Builder

RSRSSB is a python program that builds an RSS (podcast) feed with arbitrary audio files.

RSRSSB was originally developed as a way to quickly create a personal RSS feed for audiobook files to be consumed through a podcast player.

See https://github.com/mkb79/audible-cli for details on downloading your Audible books.


# Install

## Linux

Clone this project

* ```git clone https://github.com/snowskeleton/rsrssb.git .```

Run the install script
* ```cd rssrsb```

* ```./install.sh```

To use rsrssb, navigate to a directory containing the audio files for which you want to make a podcast feed.
For example purposes, we'll assume we have ```file1.mp3```, ```file2.mp3```, and ```file3.mp3``` in a directory called ```podcast/```.

* ```cd podcast/```

Then execute as follows

* ```rsrssb --title someTitle --domain someDomain```

After a brief moment of processing, you'll be left with a file named ```feed.xml``` in your currect directory

[!NOTE]
this process overwrites the ```feed.xml``` file if it's already present, so be careful to backup any important information

All that's left now is to point a webserver at this directory, change the DNS records for a URL you don't mind using, and obtain an SSL certificat.
This is left as an exercise for the reader.

curl -l https://overcast.fm/ping\?urlprefix='https://\<domain\>'
