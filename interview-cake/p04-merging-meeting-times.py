def condense_meeting_times(meeting_times):
    meeting_times.sort(key=lambda x: x[0])
    base_interval = meeting_times[0]
    merged_meeting_times = []
    for index, interval in enumerate(meeting_times):
        if is_intersecting(base_interval, interval):
            base_interval = merge_intervals(base_interval, interval)
            if index == len(meeting_times) - 1:
                merged_meeting_times.append(base_interval)
        else:
            merged_meeting_times.append(base_interval)
            base_interval = interval

    return merged_meeting_times


def is_intersecting(earlier_interval, later_interval):
    return later_interval[0] <= earlier_interval[1]


def merge_intervals(earlier_interval, later_interval):
    return earlier_interval[0], max(earlier_interval[1], later_interval[1])

print condense_meeting_times([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
# => [(0, 1), (3, 8), (9, 12)]
print condense_meeting_times([(1, 2), (2, 3)])
# => [(1, 3)]
print condense_meeting_times([(1, 5), (2, 3)])
# => [(1,5)]
print condense_meeting_times([(1, 10), (2, 6), (3, 5), (7, 9)])
# => [(1, 10)]
