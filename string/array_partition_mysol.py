def listPartition(list):
    print('before sort : ' + str(list))
    list.sort()
    print('after sort : ' + str(list))

    groupPartition=[]
    result=0

    for item in list:
        print('popping list : '+ str(list))
        temp = []
        for i in range(0,2):
            temp.append(list.pop(0))
        groupPartition.append(temp)



    for item in groupPartition:
        result+=min(item)

    return result

if __name__ == '__main__':
    n = [1,4,3,2]

    result = listPartition(n)

    print('result : ' + str(result))