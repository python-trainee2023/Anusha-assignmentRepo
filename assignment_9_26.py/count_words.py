def countwords_end_with_e(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words=text.split()
            count=0
            for word in words:
                if word.endswith('e'):
                    count +=1
            return count

    except FileNotFoundError:
        print(f"file {filename} not found.")


result = countwords_end_with_e('girl.txt')
print(f"Number of words ending with 'e': {result}")