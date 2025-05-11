# meeting with maximum guest between arrival and departure time

def meet_max_guests(arrival_list, departure_list):
    """
    """
    # sort arrival and departure
    arrival_list.sort()
    departure_list.sort()

    i = 1
    j = 0
    time = arrival_list[0]
    n = len(arrival_list)
    curr = 1
    res = 1

    while i < n and j < n:
        if arrival_list[i] <= departure_list[j]:
            curr += 1
            if curr > res:
                time = arrival_list[i]
            i += 1
        else:
            curr -= 1
            j += 1
        res = max(curr, res)
    
    return res, time


arrival_list = [1, 2, 10, 5, 5]
departure_list = [4, 5, 12, 9, 12]
print(meet_max_guests(arrival_list, departure_list))