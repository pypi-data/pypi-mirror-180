import os

def getGrammar():
    with open(f"dsl/fqlgrammar.tx") as f:
        return f.read()

def getGrammarPath():
    return "dsl/fqlgrammar.tx"

def getClassName(object):
    return object.__class__.__name__


