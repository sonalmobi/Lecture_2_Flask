#======================================
# Functions
#======================================

def sqr(s):
    return s * s

#======================================
# main
#======================================

def main():
    for lc in range(1):
        print(lc)

    name = ["sona","sopu","vicky",'sunny']


    for n in name:
        print(n)


    for n in range(len(name)):
        print(name[n])


    for i in range(10):
        print("{} == {}".format(i, sqr(i)))

if __name__=="__main__":
    main()
