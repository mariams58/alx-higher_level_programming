#!/usr/bin/python3
if __name__ == "__main__":
    """Prints name from compiled module"""
    import hidden_4
    all_fi = dir(hidden_4)
    for i in range(0, len(all_fi)):
        if "__" not in all_fi[i]:
            print(all_fi[i])
