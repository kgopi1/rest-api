import base64


def get_base64_pat(pat):
    #sample_string = "GeeksForGeeks is the best"
    pat_string=f":{pat}"
    pat_string_bytes = pat_string.encode("ascii")
    base64_pat_bytes = base64.b64encode(pat_string_bytes)
    base64_pat = base64_pat_bytes.decode("ascii")
    return base64_pat

pat="test1234"
if __name__ == '__main__':
    print(get_base64_pat(pat))
