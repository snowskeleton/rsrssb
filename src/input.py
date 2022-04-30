import argparse


parser = argparse.ArgumentParser(description='Argument parser description')
parser.add_argument('--domain', dest='domain', type=str, action='store', help='Base URL (e.g., example.net)', default='')
parser.add_argument('--title', dest='title', type=str, action='store', help='The name of your feed', default='')
args = parser.parse_args()

class Input():
  @classmethod
  def title(self):
    if args.title != '':
      return args.title
    return input("Title: ")

  @classmethod
  def link(self):
    if args.domain != '':
      return args.domain
    return input("Base URL (e.g., example.com): ")
