book_path = 'frankenstein.txt'
with open(f'./books/{book_path}', 'r') as file:
    text = file.read()
    lines = text.split('\n')
    word_count = 0
    characters_count = {}
    for line in lines:
        # I need to split the line per character
        characters_list = line.lower().split(' ')
        words = line.lower().split()
        word_count += len(words)
        for word in words:
            for char in word:
                if char not in characters_count:
                    characters_count[char] = 1
                else:
                    characters_count[char] += 1
    print(f"--- Begin report of books/{book_path} ---")
    print(f"{word_count} words found in the document")
    characters_count = dict(sorted(characters_count.items(), key=lambda item: item[1], reverse=True))
    for char, count in characters_count.items():
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")
