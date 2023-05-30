if __name__ == '__main__':
    data_filename = 'docs/arrhythmia.data'
    name_filename = 'docs/arrhythmia.names'
    try:
        with open(data_filename, 'r') as file:
            content = file.read()
            print(content)
    except IOError as e:
        if isinstance(e, FileNotFoundError):
            print(data_filename, 'not found!')
        else:
            print('An error occurred while reading the file: ', data_filename)
