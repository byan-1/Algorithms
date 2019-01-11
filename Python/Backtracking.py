def permutation(l,start,end):
    if start == end:
        print(l)
    else:
        for i in range(start, end):
            l[start], l[i] = l[i], l[start]
            permutation(l, start+1, end)
            l[start], l[i] = l[i], l[start]

#think of the result array as a means of building up solutions.
#the final results of the recursion function will be "appended" to the initial value
#added to the result array.
def permutation2(result, tobepermuted):
    if len(tobepermuted) == 0:
        print(result)
    for i in range(len(tobepermuted)):
        permutee = [x for x in tobepermuted if x != tobepermuted[i]]
        permutation2(result + [tobepermuted[i]], permutee)

def permutation3(result, tobepermuted):
    if len(tobepermuted) == 0:
        print(result)
    for i in range(len(tobepermuted)):
        elem = tobepermuted.pop(i)
        result.append(elem)
        permutation3(result, tobepermuted)
        tobepermuted.insert(i,result.pop())


def generateSubsets(result, rest):
    if len(rest) == 0:
        print(result)
    else:
        generateSubsets(result + [rest[0]], rest[1:])
        generateSubsets(result, rest[1:])


def generateSubsets2(result, rest):
    if len(rest) == 0:
        print(result)
    else:
        first = rest.pop(0)
        result.append(first)

        generateSubsets2(result, rest)
        result.pop()
        generateSubsets2(result, rest)

        rest.insert(0,first)



l=[1,2,3,4]
permutation3([],l)



