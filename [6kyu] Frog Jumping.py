def solution(a):
    length = len(a)
    current_location = 0
    counter = 0
    visited_locations = [0]
    while True:
        counter += 1
        if current_location+a[current_location]>=length:
            return counter
        if current_location+a[current_location]<0:
            return counter
        else:
            current_location = current_location+a[current_location]
            if current_location in visited_locations:
                return -1
            if current_location < 0:
                return -1
            visited_locations.append(current_location)
print(solution([1, 2, 1, 5]))
