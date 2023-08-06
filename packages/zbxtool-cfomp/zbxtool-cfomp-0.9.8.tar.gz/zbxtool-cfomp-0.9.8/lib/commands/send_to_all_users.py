#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Gary
# Datetime: 2022/12/8 16:05
# IDE: PyCharm
"""
    Functions:
        - update_action_send_users()
          - get users by "media" name
          - get "operation" and "send to users" by "action" name
          - merge "media" users and "send to users"
          - update "action"
        - main(): main function
"""
import argparse
import logging


def update_action_send_users(zapi, media_name: str, action_name: str):
    """
        根据 Action 名称更新 operation 的 "send to users" 列表：
            1. 首先根据 Media 名称获取这个 Media 下的所有用户信息（即哪些用户配置了这个 Media）；
            2. 然后，根据 Action 名称获取 Operation 信息，如果 Action 存在多个 Operation，默认更新第一个；
            3. 其次，获取此 Action 原有的 "send to users" 列表；
            4. 再比对 "send to users" 列表和根据 Media 名称获取的用户列表；
            5. 最后追加不在原有 "send to users" 列表里的用户信息。
    :param zapi:
    :param media_name:
    :param action_name:
    :return:
    """
    zapi.login(user="zhanggao", password="zhanggao711A")
    medias = zapi.mediatype.get(
        {
            "filter": {"name": media_name},
            "selectUsers": ["userid"],
            "output": ["users"]
        }
    )
    operations = zapi.action.get(
        {
            "output": ["actionid", "name"],
            "selectOperations": ["operationid", "operationtype", "opmessage", "opmessage_usr"],
            "filter": {"name": action_name}
        }
    )
    operation = operations[0].get("operations")[0]
    media_users = medias[0].get("users")
    action_users = operation.get("opmessage_usr")
    for user in media_users:
        user["operationid"] = operation.get("operationid")
    action_users.extend(media_users)
    users = []
    [users.append(i) for i in action_users if i not in users]
    zapi.action.update(
        {
            "actionid": operations[0].get("actionid"),
            "operations": [
                {
                    "operationtype": operation.get("operationtype"),
                    "opmessage_usr": users,
                    "opmessage": {
                        "default_msg": operation.get("opmessage").get("default_msg")
                    }
                }
            ]
        }
    )
    logging.info(f"update success! Action -> [{operations[0].get('name')!r}]")


def main(args):
    """Main Function"""
    update_action_send_users(
        zapi=args.zapi,
        media_name=args.media,
        action_name=args.action
    )


parser = argparse.ArgumentParser(
    description="Automatically search for the media type configured by the user,"
                "and then configure it as action"
)
parser.add_argument(
    "--media",
    required=True,
    type=str,
    help="user configured media type"
)
parser.add_argument(
    "--action",
    required=True,
    type=str,
    help="the alarm action"
)
parser.set_defaults(handler=main)
