import base64

def decode_b64(b64_string):
    return base64.b64decode(b64_string).decode('utf-8')

decoded_string = open('b64.txt', 'r').read()

for _ in range(50):
    decoded_string = decode_b64(decoded_string)

print(decoded_string) 
