def get_substring(string):
	if string=="":
		return set()
	elif len(string)==1:
		return {string}
	else:
		return {*get_substring(string[:-1]), *get_substring(string[1:]), string}


from itertools import permutations as p    


def MSCT(substring_set, target):
    valid_substring_set = set()
    for substring in substring_set:
        if substring in target:
            valid_substring_set.add((substring))
    del substring_set
    maximum = 0
    # max_coverage = target
    for permutation in p(valid_substring_set):
        masked_target = target
        for element in permutation:
            masked_target = masked_target.replace(element, '|'*len(element))
        coverage = masked_target.count("|")/len(masked_target)
        if coverage>maximum:
            maximum = coverage
            # max_coverage = masked_target
    return maximum #, max_coverage

def MaxMSCT(A, B):
    return max(MSCT(A, B), MSCT(B, A))
def MinMSCT(A, B):
    return min(MSCT(A, B), MSCT(B, A))
def AveMSCT(A, B):
    return (MSCT(A, B)+MSCT(B, A))/2
