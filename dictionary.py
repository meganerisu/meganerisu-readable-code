def read_txt(filename):
    """Read chars from text file."""
    with open("data.txt", 'r', encoding='UTF-8') as f:
        data = f.read()
    print(data)


if __name__ == '__main__':
    filename = 'data.txt'
    read_txt(filename)
