# part 1
gwith open('file.text','w+') as file:
    file.write('Puackich, hvhnkrally oaths phufhck. All ymr nhhd is Pykemn.\n')
    file.write('J.U.U.U Kmltin.\n')
    file.write('mmps iks nmk eio; ---> hkmu\n')
    file.seek(0)
    text = file.read()
    text = text.lower()
    dict1 = {}
    most_common = ['e', 't', 'o', 'r']
    def func(x):
        for letter in x:
            if letter.isalpha() :
                dict1[letter] = x.count(letter)
            text_common = list(dict1.items())
            y = sorted(text_common, key=lambda z: z[1])
            w = y[-4:]
            m = w[::-1]
            dict2 = {}

            for (k, v) in m:
                v= most_common[0]
                if k in dict2:
                    dict2[k].append(v)
                else:
                    dict2[k] = [v]
        return dict2
    print(func(text))

# part 2
def function(str):
    letters = {'h':'e' , 'k':'t', 'm':'o','u':'r','e':'h','t':'k','o':'m','r':'u'}
    print(''.join(letters.get(char,char)for char in str))
function('///bha Taa3add, bha Tdaer, enr b7ha Fdcccccbbb...')

#  # part 3
def decrypt_file(file_name: str, result_file: str):
    mapped_lines = ''
    with open(file_name, 'r+') as f:
        lines = f.readlines()
        message = ' '.join(lines).replace('\n', '')
        mapping_dict = get_mapping(message)
        f.write('The encryption for the above text is:\n')
        for l in lines:




# part 4
def longest_word_in_file(file_name: str):
    result = None
    with open(file_name, 'r') as filedata:
        wordsList = filedata.read().split()
        longestWordLength = len(max(wordsList, key=len))
        result = [textword for textword in wordsList if len(textword) == longestWordLength]
    return result

def number_of_lines(file_name: str):
    number_of_lines = -1
    with open(file_name, 'r') as fp:
        number_of_lines = len(fp.readlines())
    return number_of_lines

