import os

# Fake the filename to make it appear local
exec(open(os.path.abspath(os.path.join(os.getcwd(), "../../setmeup.py"))).read(), {'__file__': 'setmeup.py', '__name__': '__main__'})
