#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    hidden = dir(hidden_4)

    for name in hidden:
        if not name.startswith("__"):
            print(name)
