s = 'hoaftrrelltheudlospdaotw'
c = 4
height = len(s)/c
result = " ".join(['' for i in range(len(s)+1)])

print(len(result))

i = 0
while i < height:
    j = (i)*c

    counter = 0

    while counter != c:
        # print(s[j])

        if i%2 == 0:
            result_j = counter * height + i
            result = result[:result_j] + s[j] + result[result_j+1:]
        else:
            result_j = (c - 1 - counter) * height + i
            result = result[:result_j] + s[j] + result[result_j+1:]


        j += 1
        counter += 1

    i += 1

print(result)


