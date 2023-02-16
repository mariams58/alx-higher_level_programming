#!/usr/bin/python3


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return(None)
    m_value = 0
    for x in my_list:
        if x > m_value:
            m_value = x
    return(m_value)


if __name__ == "__max_integer__":
    max_integer(my_list=[])
