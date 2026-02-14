#different languages have different character sets. To represent these characters in a computer, we need to encode them into bytes. UTF-8 is a common encoding that can represent a wide range of characters from various languages.
label_text = "Chai Spécial"
ecoded_label = label_text.encode("utf-8")
print(f"Non Encoded label: {label_text}")
print (f"Encoded label: {ecoded_label}")