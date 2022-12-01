from datetime import date


def get_day(override):
    if override is None:
        day = str(date.today().strftime("%d"))
    else:
        day = str(override)

    if len(day) == 1:
        return "0" + day
    else:
        return day


def split_list(list, at):
    result = []
    indices = all_indices(list, at)
    start = -1
    end = -1
    for i in indices:
        start = end
        end = i
        result.append(list[start + 1:end])
    result.append(list[end + 1:])
    return result


def all_indices(list, value):
    indices = []
    for i in range(len(list)):
        if list[i] == value:
            indices.append(i)
    return indices

def flatten(list):
    return [item for sublist in list for item in sublist]

