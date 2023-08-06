def getGrammar():
    with open(f"src/fqllang/dsl/fqlgrammar.tx") as f:
        return f.read()

def getGrammarPath():
    return "src/fqllang/dsl/fqlgrammar.tx"

def getClassName(object):
    return object.__class__.__name__


