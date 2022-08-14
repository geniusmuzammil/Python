alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser_cipher(direction, texts, shifts):
  ceaser_text = ""
  case = "encrypted"
  if(direction == "decode"):
    shifts *= -1
    case = "decoded"
  for letters in texts:
    if(letters.isalpha()):
      ceaser_text += alphabet[(alphabet.index(letters) + shifts)%26]
    else:
      ceaser_text += letters
  print(f"So, the {case} message is {ceaser_text}")
  
is_end = False
while not is_end:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  ceaser_cipher(direction,text,shift)
  again = input("Do, You want to restart the program?  y/n")
  if(again == "n"):
    is_end = True