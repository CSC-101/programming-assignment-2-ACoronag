#from curses.textpad import rectangle

import data

# Write your functions for each part in the space below.

# Part 1
def create_rectangle(point1,point2):
    if point1.x < point2.x and point1.y > point2.y:
        return  data.Rectangle(point1,point2)
    elif point1.x > point2.x and point1.y < point2.y:
        return data.Rectangle(point2, point1)
    elif point1.x > point2.x and point1.y > point2.y:
        return data.Rectangle(data.Point(point2.x, point1.y), data.Point(point1.x, point2.y))
    else:
        return data.Rectangle(data.Point(point1.x, point2.y), data.Point(point2.x, point1.y))

# Part 2
def shorter_duration_than(duration1, duration2):
    if duration1.minutes < duration2.minutes:
        return True
    elif duration1.minutes > duration2.minutes:
        return False
    else:
        if duration1.seconds < duration2.seconds:
            return True
        else:
            return False

# Part 3
def songs_shorter_than(lista, duration):
    listb = []
    for song in lista:
        if song.duration.minutes < duration.minutes:
            listb.append(song)
        elif song.duration.minutes == duration.minutes and song.duration.seconds < duration.seconds:
            listb.append(song)
    return listb

# Part 4
def running_time(lista, listb):
    sum = data.Duration(0,0)
    for idx in listb:
        sum = data.Duration(sum.minutes + lista[idx].duration.minutes, sum.seconds + lista[idx].duration.seconds)
    while sum.seconds > 60:
        sum.seconds -= 60
        sum.minutes += 1
    return sum

# Part 5
def valid_route(links, route):
    connection = 0
    for i in range(len(route)-1):
        for j in range(len(links)):
            if (route[i] == links[j][0] or route[i] == links[j][1]) and (route[i+1] == links[j][0] or route[i+1] == links[j][1]):
                connection += 1
                break
    if connection == len(route)-1:
        return True
    else:
        return False

# Part 6

def longest_repetition(lista):
    if lista == []:
        return None
    best_streak = 1
    best_idx = 0
    for i in range(len(lista)-1):
        if lista[i] == lista[i+1]:
            best_streak += 1
        else:
            new_idx = i + 1
            break
    while new_idx != len(lista)-1:
        streak1 = 1
        temp_idx = new_idx
        for i in range(new_idx,len(lista)-1):
            if lista[i] == lista[i+1]:
                streak1 += 1
            else:
                break
        if best_streak < streak1:
            best_streak = streak1
            best_idx = temp_idx
        new_idx = i + 1
    return best_idx



