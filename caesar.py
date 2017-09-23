lower_case = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper_case = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def encrypt(text,rot):
    text = list(text)
    sentence = ''
    for char in text:
        new_val = rotate_character(char, rot)
        sentence = sentence + new_val
    return sentence

def alphabet_position(letter):
    lower_case = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upper_case = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    if letter.isalpha():
        if letter in lower_case:
           position = lower_case.index(letter)
        else:
            position = upper_case.index(letter)
        return position
    else:
        return letter
        

def rotate_character(char, rot):
    lower_case = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upper_case = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    if char.isalpha():
        if char in lower_case:
            new_val = (int(alphabet_position(char)) + int(rot)) % 26
            return  lower_case[new_val]
        else: 
            new_val = (int(alphabet_position(char))+ int(rot)) % 26
            return upper_case[new_val]
    else:
        return char

def main():

    
    text = input('enter text: ')
    rot = input('rotate by: ')
    print(encrypt(text, rot))



if __name__ == "__main__":
    main()