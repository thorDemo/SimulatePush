with open('ua.txt', 'r+') as file:
    for line in file:
        print('\'%s\',' % line.strip('\n'))