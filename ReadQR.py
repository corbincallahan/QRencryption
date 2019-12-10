import zxing


def read(filename):
    reader = zxing.BarCodeReader()
    decoded = reader.decode(filename)
    if decoded:
        return decoded.parsed
    else:
        return ""
