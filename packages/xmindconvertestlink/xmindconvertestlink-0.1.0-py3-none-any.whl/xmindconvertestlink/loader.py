# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     loader
   Description :
   Author :       yangzhixiang
   date：          2020/11/4
-------------------------------------------------
"""

from xmindparser import xmind_to_dict
from xmindconvertestlink.const import Xmind
from xmindconvertestlink.testlink_parser import parse_to_testlink_xml, pretty_xml


def loader_xmind_file(file_name):
    suites = []
    contents = xmind_to_dict(file_name)
    if len(contents) > 0:
        for content in contents:
            topic = content.get(Xmind.XMIND_TOPIC, None)
            if topic is not None and len(topic) > 0:
                title = topic.get(Xmind.XMIND_TITLE)
                topics = topic.get(Xmind.XMIND_TOPICS)
                suites.append({Xmind.XMIND_TITLE: title, Xmind.XMIND_TOPICS: topics})
    return suites


if __name__ == "__main__":
    fn = "/Users/yangzhixiang/Downloads/0831报表三期II.xmind"
    # fn = "/Users/yangzhixiang/Downloads/产品名称.xmind"
    ss = loader_xmind_file(fn)
    ll = parse_to_testlink_xml(ss)
    for l in ll:
        # print(l)
        with open("1.xml", "w", encoding='utf-8') as f:
            f.write(l)
