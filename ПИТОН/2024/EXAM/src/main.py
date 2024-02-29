import sys
from app import AbcApplication

# arguments = sys.argv[1:]
# if len(arguments) == 1:

if __name__ == "__main__":
    if len(sys.argv) == 1:
        app = AbcApplication()
        app.start()
    elif len(sys.argv) == 2:
        if sys.argv[1] == 'server':
            app = AbcApplication(mode='server')
            app.start()
        else:
            app = AbcApplication(hostname=sys.argv[1])
            app.start()
    elif len(sys.argv) == 3:
        if sys.argv[1] == 'server':
            app = AbcApplication(mode='server', hostname=sys.argv[2])
            app.start()