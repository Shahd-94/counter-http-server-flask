from flask import Flask

app = Flask(__name__)
COUNTER_FILE = 'counter.txt'

def read_counter():
    try:
        with open(COUNTER_FILE, 'r') as f:
            return int(f.read().strip())
    except FileNotFoundError:
        return 0

@app.route('/get')
def get_counter():
    counter = read_counter()
    return str(counter)


if __name__ == '__main__':
    app.run(debug=True, port=9090)