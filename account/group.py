#!/usr/bin/python3


class Group:
    def __init__(self, group_data, groupmates):
        if group_data is None:
            raise ValueError("Group data is undefined.")
        self._name = group_data.get("name")
        self._groupmates = groupmates

    def send_to(self, message):
        if not message:
            raise ValueError("Message is undefined.")
        for groupmate in self._groupmates:
            groupmate.send_to(message)
