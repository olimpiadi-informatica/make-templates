from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from parser.IOLexer import IOLexer
from parser.IOParser import IOParser
from analyzer import Analyzer
import targets
import importlib
import argparse
import yaml
from os import path


# Error listener to make sure that parsing errors are not ignored.
class FailOnError(ErrorListener):
    def syntaxError(self, recognizer, offending, line, column, msg, e):
        assert False

languages = [x for x in dir(targets) if x[0] != '_']
cms_langs = 'c/cpp/java/pas/py/tex'.split('/')
terry_langs = [x for x in languages if x != 'tex']

def main(args):
    if args.lang not in ['en', 'it']:
        print("[ERROR] Language '%s' not supported" % args.lang)
        exit(1)
    if args.terry and args.cms:
        print("[ERROR] Cannot specify both --terry and --cms")
        exit(1)
    if not path.isfile('task.yaml'):
        print("[ERROR] File task.yaml not found")

    error_listener = FailOnError()
    input_stream = InputStream(''.join(open(args.description).readlines()))
    try:
        lexer = IOLexer(input_stream)
        lexer.addErrorListener(error_listener)
        token_stream = CommonTokenStream(lexer)
        parser = IOParser(token_stream)
        parser.addErrorListener(error_listener)
        analyzer = Analyzer()
        err, res = analyzer.visitFileSpec(parser.fileSpec())
    except e:
        print("Parsing failed, aborting")
        exit(1)

    for e in err:
        print("[ERROR]", e)
    if len(err) > 0:
        exit(1)

    task_yaml = yaml.safe_load(''.join(open('task.yaml', 'r').readlines()))

    if args.terry:
        format = "terry"
    elif args.cms:
        format = "cms"
    elif path.isdir('statement') and path.isdir('solutions') and 'description' in task_yaml:
        format = "terry"
    elif path.isdir('testo') and path.isdir('att') and path.isdir('sol') and 'title' in task_yaml:
        format = "cms"
    else:
        print("[ERROR] Cannot recognise task format")
        exit(1)
    if format == "terry":
        att_folder = "statement"
        sol_folder = "solutions"
        txt_file = "statement/statement"
    if format == "cms":
        att_folder = "att"
        sol_folder = "sol"
        txt_file = "testo/" + ("english" if args.lang == "en" else "italian")

    if args.limits is None:
        args.limits = "gen/limiti.py" if format == "cms" else "managers/limits.py"
    if not path.isfile(args.limits):
        print("[ERROR] File {args.limits} not found")

    spec = importlib.util.spec_from_file_location('limits', args.limits)
    limits = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(limits)

    if len(args.targets) == 0:
        args.targets = terry_langs if format == "terry" else cms_langs

    for t in args.targets:
        if t not in dir(targets):
            print("[ERROR] Target '%s' not supported" % t)
            exit(1)
        # TODO: write files rather than printing on stdout
        print(getattr(targets, t).generate(task_yaml['name'], res, args.lang, limits.__dict__))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(epilog="This script should be run in the root directory of a task.")
    parser.add_argument(
        "targets",
        nargs="*",
        help=f"Language targets that should be considered (the default is {'/'.join(cms_langs)} for CMS and {'/'.join(terry_langs)} for Terry)"
    )
    parser.add_argument(
        "-l", "--lang",
        default="en",
        help="Language to be used for generating the files (either 'it' or 'en', defaults to 'en')",
    )
    parser.add_argument(
        "-d", "--description",
        default="inout.slide",
        help="Path of the file containing the I/O description in SLIDe (defaults to 'inout.slide')",
    )
    parser.add_argument(
        "--limits",
        help="Path of the file containing task limits (defaults to 'gen/limiti.py' for CMS and 'managers/limits.py' for Terry)",
    )
    parser.add_argument(
        "-t", "--terry",
        action="store_true",
        help="Forces the tool to interpret the task as being in the Terry format",
    )
    parser.add_argument(
        "-c", "--cms",
        action="store_true",
        help="Forces the tool to interpret the task as being in the Italian-yaml format for CMS",
    )
    parser.add_argument(
        "-n", "--no-replace",
        action="store_true",
        help="Prevents the tool from replacing already-generated files (including task statements)",
    )
    main(parser.parse_args())
