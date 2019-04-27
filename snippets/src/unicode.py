

def run_test():
    symbols = '$¢£¥€¤'
    codes = [ord(s) for s in symbols]
    print(codes)

    beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]

    print(chr(666))


if __name__ == "__main__":
    run_test()
