def split_and_join(line):
    line=line.split(" ")
    #line="-".join(line)
    return line

#if __name__ == '__main__':
line = input("enter line:")
result = split_and_join(line)
print(result)
