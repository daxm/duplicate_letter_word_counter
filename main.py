import nltk


def main():
    with_duplicates = 0
    without_duplicates = 0
    for word in nltk.corpus.words.words():
        if len(word) == len(set(word)):
            without_duplicates += 1
        else:
            with_duplicates += 1

    total = with_duplicates + without_duplicates
    print(f"Total words: {total}")
    print(f"With Duplicates: {with_duplicates}: {with_duplicates/total*100:.2f}%")
    print(f"Without Duplicates: {without_duplicates}: {without_duplicates/total*100:.2f}%")


if __name__ == '__main__':
    nltk.download('words')
    main()
