#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence:
        len1 = len(sentence)
        first = sentence[0]
        if len1 == 0:
            first = None
        return(len1, sentence)


if __name__ == " __multiple_sentence__":
    multiple_returns(sentence)
