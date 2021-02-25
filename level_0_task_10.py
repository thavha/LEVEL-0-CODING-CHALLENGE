def common_characters(string1, string2):

    common = []

    for i in string1:

        if i in string2:
            common.append(i)
            new_common = ", ".join(common)

    common_sentence = "Common letters: " + new_common

    return common_sentence