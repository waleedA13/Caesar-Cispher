alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

cap_alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]


restart = False
end = False
while not end:
    restart = False
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction != "encode" and direction != "decode":
            print("Error! Try Again")
    else:
      text = input("Type your message:\n")
      shift = int(input("Type the shift number:\n"))
      def caesar(direction, text, shift):
            crypted_answer = ""
            if direction == "decode":
                shift *= -1
            for dif in text:
                if dif in alphabet:
                    position = alphabet.index(dif)
                    new_position = position + shift
                    new_position %= 26
                    crypted_answer += alphabet[new_position]
                elif dif in cap_alphabet:
                    position = cap_alphabet.index(dif)
                    new_position = position + shift
                    new_position %= 26
                    crypted_answer += cap_alphabet[new_position]
                else:
                    crypted_answer += dif
            print(f'{crypted_answer}')

      caesar(direction, text, shift)

      while not restart:
          ask_end = input(
              'Type "yes" if you want to quit, else type no.\n').lower()
          if ask_end == "yes":
              end = True
              restart = True
          elif ask_end == "no":
              restart = True
          elif ask_end != "yes" and ask_end != "no":
              print("Error! Try again!")
