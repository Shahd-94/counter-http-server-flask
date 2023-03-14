from flask import Flask

app = Flask(__name__)
COUNTER_FILE = 'counter.txt'

# This method is responsible for reading counter data from the counter file
def read_counter():
    try:
        with open(COUNTER_FILE, 'r') as f:
            return int(f.read().strip())
    # If file does not exist, return 0
    except FileNotFoundError:
        return 0

# This method is responsible for wrtiting counter values into the counter file
def write_counter(counter):
    with open(COUNTER_FILE, 'w') as f:
        f.write(str(counter))

# Initializing /get endpoint
@app.route('/get')
def get_counter():
    counter = read_counter()
    return str(counter)

# Initializing /increase endpoint
@app.route('/increase', methods=['POST'])
def increase_counter():
    counter = read_counter() + 1
    write_counter(counter)
    return str(counter)

# Initializing /decrease endpoint
@app.route('/decrease', methods=['POST'])
def decrease_counter():
    counter = read_counter() - 1
    write_counter(counter)
    return str(counter)

if __name__ == '__main__':
    app.run(debug=True)