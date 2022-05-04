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
  # not implemented
  # p.add_argument(
  #     '--index', '-i',
  #     dest='index',
  #     action='store_true',
  #     help='Used without any other optionnsto create index.html file for all podcasts in cwd (recursively)',
  #     default=False,
  # )
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

  # @classmethod
  # def index(self):
  #   return self.args.index
