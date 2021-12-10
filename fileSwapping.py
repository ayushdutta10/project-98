def swapfileData():

    Sample1 = input("enter the original file: ")
    Sample2 = input("enter the file to be swapped: ")

    with open(Sample1, 'r') as a:
        data_a = a.read()
    with open(Sample2, 'r') as b:
        data_b = b.read()


    with open(Sample1, 'w+') as a:
        a.write(data_b)
    with open(Sample2, 'w+') as b:
        b.write(data_a)

swapfileData()