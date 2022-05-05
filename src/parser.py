import argparse

# parses cli arguments and returns values
class parse():
  p = argparse.ArgumentParser(description='Argument parser description')
  p.add_argument(
      '--domain', '-d',
      dest='domain',
      type=str,
      action='store',
      help='Base URL (e.g., example.net)',
      default='',
  )
  p.add_argument(
      '--root', '-r',
      dest='root',
      type=str,
      action='store',
      help='The directory structor of your website before the podcast (path/to/your/books): ',
      default='',
  )
  p.add_argument(
      '--title', '-t',
      dest='title',
      type=str,
      action='store',
      help='The name of your feed',
      default='',
  )
  p.add_argument(
      '--unattended', '-y',
      dest='unattended',
      action='store_true',
      help='Use this to bypass user input, leaving all values default',
      default='',
  )
  p.add_argument(
      '--extension', '-e',
      dest='extension',
      action='store',
      type=str,
      help='The name of your feed',
      default='mp3',
  )
  p.add_argument(
      '--output', '-o',
      dest='outputFile',
      action='store',
      type=str,
      help='Name of rss file to be created',
      default='feed.xml',
  )


  args = p.parse_args()

  @classmethod
  def domain(self):
    return self.args.domain

  @classmethod
  def root(self):
    return self.args.root

  @classmethod
  def title(self):
    return self.args.title

  @classmethod
  def extension(self):
    return self.args.extension

  @classmethod
  def output(self):
    return self.args.outputFile
