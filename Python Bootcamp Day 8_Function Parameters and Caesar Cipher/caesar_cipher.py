#Caesar Cipher Program

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
keep_going = True
while keep_going == True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  def caesar(text, shift, direction):
    new_text = ""
    if shift > 27:
      shift = shift % 27
    if direction == "decode":
        shift *= -1
    for char in text:
      new_char = alphabet[(alphabet.index(char) + shift)]
      new_text += new_char
    print(f"The {direction}ed text is: {new_text}")
   
  
  caesar(text = text, shift = shift, direction = direction)
  again = input("Do you want to run again? y or n: ")
  if again == "n":
    print("Goodbye")
    keep_going = False
  

   