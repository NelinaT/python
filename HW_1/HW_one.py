def beginning(word):
    size = len(word)
    remainder = size % 3

    if size == 0:
        return ''
    elif remainder == 2:
        index = int(size / 3) + 1
    else:
        index = int(size / 3) 

    return word[:index]
    
def middle(word):
    size = len(word)
    remainder = size % 3

    if size == 1:
       return word[0]
    elif size == 2:
       return ''
    elif remainder in (0 , 1):
       index = int(size / 3)
       return word[index : size - index]
    else:
       index = int(size / 3)
       return word[index + 1 : size - index - 1]

def end(word):
    size = len(word)
    remainder = size % 3

    if size <= 1:
        return ''
    elif remainder == 2:
        index = int(size / 3) + 1
    else:
        index = int(size / 3) 

    return word[size - index :]       

def split_sentence(sentence):
    words_list = sentence.split()
    result_list=[]

    for i in words_list:
        result_list.append((beginning(i), middle(i), end(i)))
        
    return result_list

# some test cases I checked:

# print(beginning("nelina"), middle("nelina"), end("nelina"))
# print( beginning("Пица"), middle("Пица"), end("пица"))
# print(beginning("барабани"), middle("барабани"), end("барабани"))
# print(beginning("Враца"), middle("Враца"),end("Враца"))
# print(beginning("123456654321"), middle("1234567654321"), end("1234567654321"))
# print(beginning("домашно"), middle("домашно"), end("домашно"))
# print(beginning("aheloy"), middle("aheloy"), end("aheloy"))
# print(beginning("шах"), middle("шах"), end("шах"))
# print(beginning("пайтън"), middle("пайтън"), end("пайтън"))
# print(beginning("pa"), middle("pa"), end("pa"))
# print(beginning("p"), middle("p"), end("p"))
# print(beginning(""), middle(""), end(""))
# print(beginning("pa/ra"), middle("pa/ra"), end("pa/ra"))

# print(split_sentence('Kазвам се Джон Сноу'))
# print(split_sentence('аз купих домати и краставици от магазина'))
# print(split_sentence('О'))
# print(split_sentence('Ок'))