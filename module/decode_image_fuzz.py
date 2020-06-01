# Lint as: python3
"""
Attempts at fuzzing tf.io.decode_image via pythonfuzz
"""

from absl import app

from tensorflow.io import decode_image
from pythonfuzz.main import PythonFuzz
from tensorflow.python.framework.errors_impl import InvalidArgumentError
@PythonFuzz
def decode_image_fuzz(buff):
  try:
    string_buff = buff.decode('ascii')
    size = len(buff)
    decode_image(buff)
  except UnicodeDecodeError:
    pass
  except InvalidArgumentError as err:
    print(err)

def main(argv):
  if len(argv) > 1:
    raise app.UsageError('Too many command-line arguments.')

if __name__ == '__main__':
  # app.run(main)
  decode_image_fuzz()
  print('Done fuzzing')
