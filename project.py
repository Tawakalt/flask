import sys
from utility.create_app import create_app
from run_tests import test

app = create_app()

def run_app(x, f):
    if __name__ == '__main__':
        if 'test' in sys.argv:
            return test()
    app.run(debug=True)

# run_app()