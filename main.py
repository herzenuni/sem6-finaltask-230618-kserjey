from flask import Flask, request
from types import SimpleNamespace
app = Flask(__name__)

def count(string):
  state = SimpleNamespace(current_word='', is_space=False)

  for char in string:
    if not char.isspace():
      state.is_space = False
      state.current_word += char
    elif not state.is_space:
      yield len(state.current_word)
      state.is_space = True
      state.current_word = ''

  yield len(state.current_word)
    

@app.route('/')
def handle():
  return 'Hello, World!'

@app.route('/count', methods=['POST'])
def handle_count():
  data = request.get_json()
  sequence = count(data)
  return ','.join(map(str, sequence))
