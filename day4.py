

# Define functions

def get_sections(assigment_pair):
    assigment_pair = assigment_pair.split(",")
    pair1 = assigment_pair[0].split("-")
    pair1 = range(int(pair1[0]),int(pair1[1])+1)
    pair2 = assigment_pair[1].split("-")
    pair2 = range(int(pair2[0]),int(pair2[1])+1)
    both_pairs = [pair1,pair2]
    return both_pairs

def range_subset(range1, range2):
    """Whether range1 is a subset of range2."""
    if not range1:
        return True  # empty range is subset of anything
    if not range2:
        return False  # non-empty range can't be subset of empty range
    if len(range1) > 1 and range1.step % range2.step:
        return False  # must have a single value or integer multiple step
    return range1.start in range2 and range1[-1] in range2

def range_overlap(range1, range2):
    """Whether range1 is a subset of range2."""
    if not range1:
        return True  # empty range is subset of anything
    if not range2:
        return False  # non-empty range can't be subset of empty range
    if len(range1) > 1 and range1.step % range2.step:
        return False  # must have a single value or integer multiple step
    return range1.start in range2 or range1[-1] in range2


## PART 1
duplicated_sections = 0
with open("C:/Users/earam/Desktop/adventofcode22/day4input.txt","r") as in1:
    for line in in1:
        line = line.strip()
        pairs_list = get_sections(line)
        pair1 = pairs_list[0]
        pair2 = pairs_list[1]
        if range_subset(pair1,pair2) or range_subset(pair2,pair1):
            duplicated_sections += 1

print(f'One range fully contains the other in {duplicated_sections} pairs')

## PART 2
overlap_sections = 0
with open("C:/Users/earam/Desktop/adventofcode22/day4input.txt","r") as in1:
    for line in in1:
        line = line.strip()
        pairs_list = get_sections(line)
        pair1 = pairs_list[0]
        pair2 = pairs_list[1]
        if range_overlap(pair1,pair2) or range_overlap(pair2,pair1):
            overlap_sections += 1

print(f'{overlap_sections} pairs overlap')