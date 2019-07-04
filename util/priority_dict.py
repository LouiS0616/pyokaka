import collections
import collections.abc


class PriorityDict(collections.abc.MutableMapping):
        
    def __init__(self, default_priority_func):
        self._default_priority_func = default_priority_func

        self._inner_keys = set()
        self._inner_dict = collections.defaultdict(dict)

    # as dict
    def __getitem__(self, key):
        if key not in self._inner_keys():
            raise KeyError(key)

        return self._inner_dict[self._ask_priority(key)][key]

    def __setitem__(self, key, value, *, priority=None):
        if priority is None:
            priority = self._default_priority_func(key)

        if key in self._inner_keys:
            del self[key]

        self._inner_dict[priority][key] = value
        self._inner_keys.add(key)

    def __delitem__(self, key):
        if key not in self._inner_keys:
            raise KeyError(key)

        del self._inner_dict[self._ask_priority(key)][key]
        self._inner_keys.remove(key)

    def __len__(self):
        return len(self._inner_keys)

    def _ask_priority(self, key):
        for priority, dct in self._inner_dict.items():
            if key in dct:
                return priority

        assert False

    # for iterate
    def keys(self):
        for key in sorted(self._inner_dict):
            dct = self._inner_dict[key]
            yield from dct

    def values(self):
        for key in sorted(self._inner_dict):
            dct = self._inner_dict[key]
            yield from dct.values()

    def items(self):
        return zip(self.keys(), self.values())

    def __iter__(self):
        return self.keys()

    # as container
    def __contains__(self, key):
        return key in self._inner_keys

    def __str__(self):
        return 'priority  items\n' + '\n'.join(
            ' -{:>6}: {}'.format(priority, self._inner_dict[priority])
            for priority in sorted(self._inner_dict.keys())
        )
