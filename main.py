with open("./books/frankenstein.txt") as file:
    file_contents = file.read()


def main():
    final_count = count_characters(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(file_contents)} words found in the document")
    for char in final_count:
        if char.isalpha():
            print(f"The '{char}' character was found {
                  final_count[char]} times")
    print("--- End report ---")


def count_words(text):
    words = text.split()
    num_of_words = len(words)
    return num_of_words


def count_characters(text):
    char_count = {}
    for i in range(0, len(text)):
        lowered_char = text[i].lower()
        if lowered_char in char_count:
            char_count[lowered_char] += 1
        else:
            char_count[lowered_char] = 0
            char_count[lowered_char] += 1
    return char_count


main()
