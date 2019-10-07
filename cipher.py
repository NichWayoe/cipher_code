# An encoder/decoder for our spies to secretly send messages.

encryption_option = input("Would you like to Encode or Decode? ")

# should_encode will be true if the user
should_encode = "encode" in encryption_option.lower()
should_decode = "decode" in encryption_option.lower()

# Ask the user for their message and cipher number.
cipher_number = int(input("What is your cipher number? "))
code = input("What is your message? ")
c = ""
if should_encode:
    # Your code here!
    for i in code:
        if (ord(i) >= ord("A") and ord(i) <= ord("Z")) or (ord(i) >= ord("a") and ord(i) <= ord("z")):
            d = ord(i) + cipher_number
            if d > ord("z") and ord(i) >= 97 and ord(i) <= 122:
                b = d - ord("z") - 1
                c = c + chr(ord("a") + b)
            elif ord(i) >= 65 and ord(i) <= 90 and d > ord("Z"):
                b = d - ord("Z") - 1
                c = c + chr(ord("A") + b)
            else:
                c = c + chr(ord(i) + cipher_number)
        else:
            c += i

    pass
elif should_decode:
    for i in code:
        if (ord(i) >= ord("A") and ord(i) <= ord("Z")) or (ord(i) >= ord("a") and ord(i) <= ord("z")):
            d = ord(i) - cipher_number
            if d < ord("a") and ord(i) >= 97 and ord(i) <= 122:
                b = ord("a") - d - 1
                c = c + chr(ord("z") - b)
            elif ord(i) >= 65 and ord(i) <= 90 and d < ord("A"):
                b = ord("A") - d - 1
                c = c + chr(ord("Z") - b)
            else:
                c = c + chr(ord(i) - cipher_number)
        else:
            c += i

    pass
else:
    # Print a nice notice that we only support encrypt/decrypt
    print("we will only support encrypt/decrypt")
    pass
print(c)

