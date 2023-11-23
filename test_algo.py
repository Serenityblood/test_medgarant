from datetime import datetime, timedelta
from random import randint

form = '%H:%M'
time = datetime.strptime('09:00', form)
delta = timedelta(minutes=30)
busy = [
    {
        'start': '10:30',
        'stop': '10:50'
    },
    {
        'start': '18:40',
        'stop': '18:50'
    },
    {
        'start': '14:40',
        'stop': '15:50'
    },
    {
        'start': '16:40',
        'stop': '17:20'
    },
    {
        'start': '20:05',
        'stop': '20:20'
    }
]


def partitions(arr, pivot):
    left = []
    right = []
    mid = []
    pivot = datetime.strptime(pivot['start'], form)
    for gap in arr:
        start = datetime.strptime(gap['start'], form)
        if start == pivot:
            mid.append(gap)
        elif start < pivot:
            left.append(gap)
        else:
            right.append(gap)
    return left, mid, right


def sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[randint(0, len(arr) - 1)]
        left, mid, right = partitions(arr, pivot)
        return sort(left) + mid + sort(right)


def get_gaps(busy):
    result = []
    now_time = time
    for gap in busy:
        end = datetime.strptime(gap['start'], form)
        while now_time + delta <= end:
            new_time = now_time + delta
            result.append(
                (f'{now_time.strftime(form)}-'
                 f'{new_time.strftime(form)}')
            )
            now_time = new_time
        now_time = datetime.strptime(gap['stop'], form)
    return result


if __name__ == '__main__':
    busy = sort(busy)
    print(get_gaps(busy))
