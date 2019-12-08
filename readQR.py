import python-zxing

def read(filename):
  reader = zxing.BarCodeReader()
  decoded = reader.decode(filename)
  return decoded[1]
