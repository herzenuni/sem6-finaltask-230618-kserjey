from main import count

def test_count():
  series = count('hello my friend')
  expected = [5, 2, 6]
  assert list(series) == expected