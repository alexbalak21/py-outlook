import random
import re





def gen_rand_str() -> str:
    rand = ""
    for n in range(4):
        r = random.randint(1,9)
        rand += str(r)
    return rand




def rand_to_file(n):
    f = open('rand.txt', 'w')
    for i in range(n):
        rand = gen_rand_str()
        rand += "\n"
        f.write(rand)
    f.close()


rand_to_file(20)