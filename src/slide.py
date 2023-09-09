from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from parser.IOLexer import IOLexer
from parser.IOParser import IOParser
from analyzer import Analyzer
import targets
import importlib
import argparse
import yaml


# Error listener to make sure that parsing errors are not ignored.
class FailOnError(ErrorListener):
    def syntaxError(self, recognizer, offending, line, column, msg, e):
        assert False


def main(args):
    if args.target not in dir(targets):
        print("[ERROR] Target '%s' not supported" % args.target)
        exit(1)

    if args.lang not in ['en', 'it']:
        print("[ERROR] Language '%s' not supported" % args.lang)
        exit(1)

    error_listener = FailOnError()
    input_stream = InputStream(''.join(open(args.spec).readlines()))
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

    if len(err) == 0:
        spec = importlib.util.spec_from_file_location('limits', args.limits)
        limits = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(limits)
        name = yaml.safe_load(''.join(open(args.yaml, 'r').readlines()))['name']
        print(getattr(targets, args.target).generate(name, res, args.lang, limits.__dict__))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "spec",
        help="Path of the .spec file",
    )
    parser.add_argument(
        "yaml",
        help="Path of the task.yaml file",
    )
    parser.add_argument(
        "limits",
        help="Path of the limits.py file",
    )
    parser.add_argument(
        "target",
        help="The target language extension (supported: %s)" % ', '.join(x for x in dir(targets) if x[0] != '_'),
    )
    parser.add_argument(
        "lang",
        help="The language of the generated file (supported: en, it)",
    )
    main(parser.parse_args())
