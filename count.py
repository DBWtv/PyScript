
to_count = Element("to_count")

op = Element("result")

def Clear(*arg, **kwargs):
    to_count.clear()
  
def Counter(*arg, **kwargs):
    op.write(len(to_count.value))


