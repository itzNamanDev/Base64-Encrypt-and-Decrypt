import base64

# Input text
text = input("Enter Your Text Here: ")

# Encode the text in base64
encoded_text = base64.b64encode(text.encode('utf-8')).decode('utf-8')

print("Encoded Text: ", encoded_text)
