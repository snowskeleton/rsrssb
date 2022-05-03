from dotenv import dotenv_values
from parser import parse

# this file is responsible for combining environment variables either
# specified in the environment, in .env file, or from user input
# To add an environment variable, create a new classmethod in the
# env class.


vals = dotenv_values('~/.rsrssb')

# Use the getTrueValues method to query first the environment,
# secondly the .env file, and thirdly ask the user for input on the
# command line. It accepts
def getTrueValue(value, question):
  if value in parse.args:
    return getattr(parse.args, value)
  if value in vals:
    return getattr(vals, value)
  # save for next time
  domain = input(question)
  with open('~/.rsrssb', 'w') as settings:
    settings.write(f'domain={domain}')
  return domain


class env():
  @classmethod
  def domain(self):
    return getTrueValue('domain', "Base URL (e.g., example.com): ")

  @classmethod
  def title(self):
    if parse.title != '':
      return parse.title()
    return input("Title: ")
