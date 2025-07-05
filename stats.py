def count_words(book_contents):
    split_words = book_contents.split()
    #print (split_words)
    word_count = len(split_words)
    return word_count
def count_letters (book_content):
    lower_case = book_content.lower()
    symbol = {}
    for char in (lower_case):
        if char in symbol:
            symbol[char] +=1
            #print (symbol)
        else:
            symbol[char] = 1
    return symbol
def dict_sort(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse = True))
    #print(sorted_dict)
    return sorted_dict