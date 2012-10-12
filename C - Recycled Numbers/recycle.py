def RecyclePossibilities(n, B, pairs):
    len_n = len(str(n))
    num_list=[]
    possibilities = 0
    for i in range(len_n-1):
        num_list = list(str(n))
#        print(num_list)
        num_to_check = num_list[:-(i+1)]
        num_to_check.insert(0, "".join(num_list[-(i+1):]))
        num_to_check = int("".join((num_to_check)))
#        print(num_to_check)
        if (num_to_check > n and num_to_check <= B) and ((str(n) + str(num_to_check)) not in pairs):
            pairs.append(str(n) + str(num_to_check))
            possibilities += 1
#            print("Recycled: (%d, %d)" % (n, num_to_check))
    return possibilities
    
filePrefix = 'C-large'
fin = open(filePrefix + '.in', 'r')
fout = open(filePrefix + '.out', 'w')
T = int(fin.readline())
for i in range(T):
    pairs = []
    A, B = [int(x) for x in fin.readline().split()]
    n = A
    answer = 0
    while n < B:
        answer_to_add = RecyclePossibilities(n, B, pairs)
        if answer_to_add > 0:
            answer+=answer_to_add
        n+=1
    fout.write("Case #%d: %d\n" % ((i+1), answer))