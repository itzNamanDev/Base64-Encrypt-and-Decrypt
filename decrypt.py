import base64

# Base64 encoded text
encoded_text = input("Enter your encoded text here: ")

try:
    # Decode the base64 text
    decoded_text = base64.b64decode(encoded_text).decode('utf-8')
    print("Decoded Text: ", decoded_text)
except (base64.binascii.Error, UnicodeDecodeError):
    print("Error: The input is not valid Base64 encoded text or it's improperly formatted.")
