import sys
from utility.create_app import create_app
from run_tests import test
from werkzeug.debug import DebuggedApplication

def run_app():
    if __name__ == '__main__':
        if 'test' in sys.argv:
            return test()
    app = create_app()
    app.run(debug=True)

run_app()