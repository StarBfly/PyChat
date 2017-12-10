class Group:
    def __init__(self, group_data, groupmates):
        self._name = group_data.get("name")
        self._groupmates = groupmates

    def send_to(self, message):
        for groupmate in self._groupmates:
            groupmate.send_to(message)
