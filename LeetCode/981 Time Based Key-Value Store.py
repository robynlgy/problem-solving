# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

# Implement the TimeMap class:

# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".


class TimeMap:
# dont really need a hashmap for key value or a 'times' list, just keep it as a list of lists
# the order of that list would already be ordered by timestamp so you can just look through
# the whole list

    def __init__(self):
        self.timemap = defaultdict(dict)    # dont need a dict

    def set(self, key: str, value: str, timestamp: int) -> None:
        key_obj = self.timemap[key]
        key_obj[timestamp] = value
        if key_obj.get('times'):
            key_obj['times'].append(timestamp)
        else:
            key_obj['times'] = [timestamp]

    def get(self, key: str, timestamp: int) -> str:
        key_timemap = self.timemap[key]
        if not key_timemap: return ''
        ret_idx = self.max_prev_time(key_timemap,timestamp)
        return key_timemap[ret_idx] if ret_idx != -1 else ''

    def max_prev_time(self, timemap: dict , timestamp: int) -> int:
        times = timemap['times']
        if timestamp < times[0]: return -1
        #max less than timestamp
        l , r = 0 , len(times)
        while l < r:
            m = (l + r )//2

            if times[m] <= timestamp:
                l = m + 1
            elif times[m] > timestamp:
                r = m
        return times[l-1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)