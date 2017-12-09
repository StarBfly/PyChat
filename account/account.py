#!/usr/bin/python3
from account.user import User
from account.group import Group
from endpoints.client_endpoint import ClientEndpoint
from endpoints.server_endpoint import ServerEndpoint


class Account:
    def __init__(self, account_data):
        if account_data is None:
            raise ValueError("Account data is undefined.")
        current_user_data = account_data.get("current_user")
        self._current_user = User(current_user_data, ServerEndpoint)
        users_data = account_data.get("users")
        self._users = [User(user_data, ClientEndpoint) for user_data in users_data]
        groups_data = account_data.get("groups")
        self._groups = self._create_groups(groups_data)

    def to_json(self):
        pass

    def _create_groups(self, groups_data):
        result = []
        for group_data in groups_data:
            groupmates_nicknames = group_data.get("groupmates")
            groupmates_users = self._get_users_by_nicknames(groupmates_nicknames)
            result.append(Group(group_data, groupmates_users))
        return result

    def _get_users_by_nicknames(self, nicknames):
        return [user for user in self._users if user.nickname in nicknames]
