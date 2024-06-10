def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count


def sort_on(dict_item):
    return dict_item["num"]


def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)

    sorted_char_count = sorted(
        [{"char": char, "num": count} for char, count in char_count.items()],
        key=sort_on,
        reverse=True
    )

    print(f'--- Begin report of books/frankenstein.txt ---')
    print(f'{word_count} words found in the document\n')

    for item in sorted_char_count:
        print(f"The '{item['char']}' character was found {item['num']} times")

    print('--- End report ---')


if __name__ == "__main__":
    main()
