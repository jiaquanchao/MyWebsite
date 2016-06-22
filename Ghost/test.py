def count_words(s, n):
    """Return the n most frequently occuring words in s."""

    # TODO: Count the number of occurences of each word in s
    words = {}
    s = s.split(" ")
    s_num = len(s)
    for i in s:
        words[i] = words.get(i, 0) + 1
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    word_sort = []
    word_sort = sorted(words.iteritems(), words.values(), reverse=False)
    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    for name, num in word_sort:
        word_sort_dic[num] = word_sort_dic.get(num, [name]).append(name)

    for i, ii in word_sort_dic:
        print (i,ii)
    # for i in range(s_num-1):
    #     if word_sort[i][1] != word_sort[i][1]:
    #         new_word_sort.append(word_sort[i])
    #     else:
    #         for ii in range(s_num-1)[i::]
    return top_n


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()
