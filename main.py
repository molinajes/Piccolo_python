import argparse
import config
import webapp

parser = argparse.ArgumentParser()
parser.add_argument(
    '--dev',
    action='store_true',
    dest='is_dev',
    help='Running piccololabs.com locally on http://127.0.0.1:8000/')
input_args = parser.parse_args()

app = webapp.create_app(config, is_dev=input_args.is_dev)


# This is only used when running locally. When running live, gunicorn runs
# the application.
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=False)
