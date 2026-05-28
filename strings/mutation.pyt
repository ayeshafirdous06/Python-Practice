def mutate_string(string, position, character):

    return  string[:position]+character+string[position+1:]

if __name__ == '__main__':
    s = input("enter string:")
    i, c = input("enter position and character:").split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)