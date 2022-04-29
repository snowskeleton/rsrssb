# the header is included at the top of the feed.xml
HEADER = """<?xml version="1.0" encoding="UTF-8"?>
<rss xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" version="2.0">
<channel>
<title>";TITLE"</title>
<link>;LINK</link>
<image>
	<url>;LINK/rss/;TITLE/cover.jpg<url>
	<link>;LINK</link>
</image>
<itunes:image href=";LINK/rss/;TITLE/cover.jpg"/>
<description>";DESCRIPTION"</description>
<lastBuildDate>";LASTBUILDDATE"</lastBuildDate>
<pubDate>";LASTPUBDATE"</pubDate>
<docs>http://blogs.law.harvard.edu/tech/rss</docs>
<webMaster>;WEBMASTER</webMaster>
"""

# a new item template will be used for each file in your feed
ITEM_TEMPLATE = """
	<item>
	  <title>";EP_TITLE"</title>
	  <link>";EP_LINK"</link>
	  <description>";EP_DESCRIPTION"</description>
	  <enclosure url=";EP_ENCLOSURE_URL" type="audio/mpeg" length=";EP_LENGTH_IN_BYTES" />
	  <pubDate>";EP_PUBDATE"</pubDate>
	</item>
"""

# closing tags for the header
FOOTER = """
</channel>
</rss>
"""
