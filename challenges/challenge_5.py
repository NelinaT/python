import re


def parse_wishlist(christams_wishes):
    list_of_wishes = []
    splitted_wishes = re.split('^\(',christams_wishes,0,re.MULTILINE)
    for wish in splitted_wishes:
       all_wishes =[]
       if wish:
            number = float( re.search(r"[-+]?\d*\.?\d+|\d+", wish).group(0))
            name = re.search(r"^.*\)(.*)\[.*$",wish, re.MULTILINE).group(1).strip()
            age = int(re.search(r"\[(\d{1,3})(.*)\]",wish, re.MULTILINE).group(1).strip())
            wishes = re.split(r"- | \*  |\n", wish)

            for index in range(1,len(wishes)):
                wishes[index]=wishes[index].replace("\n", "").strip()
                wishes[index]=wishes[index].replace("*", "").strip()

                if wishes[index]:
                    all_wishes.append(wishes[index])

            all_wishes = tuple(all_wishes)
            list_of_wishes.append((number, name, age, all_wishes))

    return list_of_wishes

txt ='''(3.14) Иван Иванов [10 г.]

 - Плейстейшан
 - Количка с дистанционо
 * Братче

(1.94)   Georgi "Jorkata" Georgiev  [43] 

 - Novo BMW (3-ka ili 5-ca)
 - 
  - Vancheto ot tretiq etaj

 - Pleistei6an'''

print(parse_wishlist(txt))

