import enchant
import itertools
import enchant

d = enchant.request_pwl_dict('./scrabble.txt')

def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

max_word_length = int(input("Max Word Length: "))
min_word_length = int(input("Min Word Length: "))

if min_word_length > max_word_length:
	print("Min Word Length must be equal to or less than Max Word Length. Please try again.")
	quit()	

if min_word_length < 1:
	print("Min Word Length must be greater than 0")
	quit()	


letters = input("Letters Provided: ")

if max_word_length > len(letters):
	print("Max word size exceeds available letters. Please try again.")
	quit()

all_permutations = []

for i in range(max_word_length,min_word_length-1,-1):
	all_permutations += ([''.join(k) for k in permutations(letters,i)])

real_words = []

for i,k in enumerate(all_permutations):
	if(d.check(k.upper())):
		real_words.append(k)

real_words = list(set(real_words))

for i,k in enumerate(list(sorted(real_words, key=len))):
	print("#"+ str(i) + ": " + k + "\n")