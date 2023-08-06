import os

def getGrammar():
    with open(f"fqllang/dsl/fqlgrammar.tx") as f:
        return f.read()

def getGrammarPath():
    return "fqllang/dsl/fqlgrammar.tx"

def getClassName(object):
    return object.__class__.__name__


