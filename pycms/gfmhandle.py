import ghmarkdown.ghmarkdown as ghmd
import sys
import os.path
import hashlib


def html_from_markdown(markdown, login=None):
    ghmd.login = login
    return ghmd.html_from_markdown(markdown)

standalone = ghmd.standalone
run_server = ghmd.run_server
Login = ghmd.Login


class GfmHandle(object):
    def __init__(self):
        self.parser = ghmd.parser
        self.login = None
        self.silent = ghmd.silent
        self.__version__ = ghmd.__version__
        self.description = ghmd.description
        self.usage = ghmd.usage
        self.gh_url = ghmd.gh_url
        self.mdhash = ghmd.mdhash
        self.input = None
        self.title = ghmd.title
        self.html_title = ghmd.html_title
        self.input = None

    def main(self):
        global parser
        global login
        global silent
        global html
        global mdhash
        global inputfile

        parser = self.parser

        parser.add_argument('--version', action='store_true')
        parser.add_argument('--input', '-i', metavar='MD',
                            help='input markdown file (otherwise STDIN)')
        parser.add_argument('--output', '-o', metavar='HTML',
                            help='output html file (otherwise STDOUT)')
        parser.add_argument('--login', '-l', action='store_true',
                            help='allows for more requests')
        parser.add_argument('--bare', '-b', action='store_true',
                            help='disable standalone html (gives fragment)')
        parser.add_argument('--silent', '-q', action='store_true',
                            help='silences server output and rate information')
        parser.add_argument('--serve', '-s', action='store_true',
                            help='locally serve parsed markdown')
        parser.add_argument('--port', '-p', metavar='PORT')

        args = self

        login = self.login

        inputfile = args.input

        if os.path.isfile(args.input):
            with open(args.input, 'r', encoding='utf-8') as markdown:
                data = "".join(markdown.readlines())
        else:
            sys.stderr.write("Input file doesn't exist\n")
            sys.exit(1)

        if args.login:
            login = self.login
        else:
            login = Login()

        silent = self.silent

        html = html_from_markdown(data, login=login)
        m = hashlib.md5()
        m.update(data.encode('utf-8'))
        mdhash = m.hexdigest()

        return html
