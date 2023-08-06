# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     cli
   Description :
   Author :       yangzhixiang
   date：          2020/11/4
-------------------------------------------------
"""

import sys
from xmindconvertestlink.const import Xmind, SuiteXML
from xmindconvertestlink.loader import loader_xmind_file, parse_to_testlink_xml
import os
import time


def get_absolute_path(path):
    fp, fn = os.path.split(path)
    if not fp:
        fp = os.getcwd()
    fp = os.path.abspath(os.path.expanduser(fp))
    return os.path.join(fp, fn)


def current_time() -> str:
    return time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())


def cli_main():
    if len(sys.argv) <= 1:
        print("please specify a xmind file full path")
        sys.exit(0)
    xmind_path = sys.argv[1]
    if not xmind_path.endswith(Xmind.XMIND_SUFFIX):
        print('error ext format of xmind file')
        sys.exit(0)
    else:
        xmind_path = get_absolute_path(xmind_path)
        xml_path = xmind_path[:-6]
        xmind_content = loader_xmind_file(xmind_path)
        if len(xmind_content) > 0:
            xml_suites = parse_to_testlink_xml(xmind_content)
            for xml_suite in xml_suites:
                suite_xml_path = xml_path + "_" + xml_suite.get(SuiteXML.TOPIC) + "_" + current_time() + ".xml"
                with open(suite_xml_path, 'w', encoding='utf-8') as f:
                    f.write(xml_suite.get(SuiteXML.XML))
    print("xmind to testlink xml completed")


if __name__ == "__main__":
    cli_main()
