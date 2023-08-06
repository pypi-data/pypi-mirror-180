# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     testlink_parser
   Description :
   Author :       yangzhixiang
   date：          2020/11/4
-------------------------------------------------
"""

from io import BytesIO
from xml.etree.ElementTree import Element, SubElement, Comment, ElementTree
from xmindconvertestlink.const import Tag, Attr, Xmind, Marker, SuiteXML
from xml.sax.saxutils import escape
from xml.dom import minidom


def parse_to_testlink_xml(suites):
    xml_suites = []
    for suite in suites:
        root_suite = Element(Tag.TESTSUITE)
        root_suite.set(Attr.Name, "")
        parser_node(suite, root_suite)
        tree = ElementTree(root_suite)
        f = BytesIO()
        tree.write(f, encoding='utf-8', xml_declaration=True)
        xml_string = f.getvalue()
        xml_suites.append({SuiteXML.TOPIC: suite.get(Xmind.XMIND_TITLE), SuiteXML.XML: pretty_xml(xml_string)})
    return xml_suites


def pretty_xml(xml_string):
    parsed = minidom.parseString(xml_string)
    return parsed.toprettyxml(indent="\t")


def parser_node(item, parent):
    if isinstance(item, dict):
        if is_need_parse(item):
            if not is_testcase_node(item):
                title = item.get(Xmind.XMIND_TITLE)
                topics = item.get(Xmind.XMIND_TOPICS)
                testsuite_node = SubElement(parent, Tag.TESTSUITE)
                if title is not None:
                    testsuite_node.set(Attr.Name, title)
                if topics is not None and len(topics) > 0:
                    if isinstance(topics, list) or isinstance(topics, tuple):
                        for v in topics:
                            parser_node(v, testsuite_node)
            else:
                parse_testcase_node(item, parent)


def parse_testcase_node(item: dict, parent):
    testcase_node = SubElement(parent, Tag.TESTCASE)
    title = item.get(Xmind.XMIND_TITLE)
    if title is not None:
        testcase_node.set(Attr.Name, title)
    note = item.get(Xmind.XMIND_NOTE)
    if note is not None:
        summary = SubElement(testcase_node, Tag.SUMMARY)
        node_set_text(summary, note)
    steps = parse_steps_node(item)
    if len(steps) > 0:
        steps_node = SubElement(testcase_node, Tag.STEPS)
        for i, step in enumerate(steps):
            step_node = SubElement(steps_node, Tag.STEP)
            # step_number
            step_number_node = SubElement(step_node, Tag.STEP_NUMBER)
            node_set_text(step_number_node, str(i + 1))
            actions_node = SubElement(step_node, Tag.ACTIONS)
            node_set_text(actions_node, step)


def node_set_text(node, content):
    content = escape(content, entities={'\r\n': '<br />'})
    content = content.replace('\n', '<br />')
    content = content.replace('<br />', '<br />\n')
    node.append(Comment(' --><![CDATA[' + content.replace(']]>', ']]]]><![CDATA[>') + ']]> <!-- '))


def parse_steps_node(item: dict):
    """
    获取用例节点下所有测试步骤
    :param item:
    :return:
    """
    steps = []
    for step in steps_crawler(item):
        if len(step) > 1:
            step = step[1:]
            steps.append("->".join(step))
    return steps


def steps_crawler(item, pre=None):
    pre = pre[:] if pre else []
    if isinstance(item, dict):
        if is_need_parse(item):
            title = item.get(Xmind.XMIND_TITLE)
            topics = item.get(Xmind.XMIND_TOPICS)
            if topics is not None and len(topics) > 0:
                if isinstance(topics, list) or isinstance(topics, tuple):
                    for v in topics:
                        for d in steps_crawler(v, pre + [title]):
                            yield d
                else:
                    yield pre + [title]
            else:
                yield pre + [title]


def is_need_parse(item) -> bool:
    if isinstance(item, dict):
        markers = item.get(Xmind.XMIND_MARKERS)
        if markers is not None and len(markers) > 0:
            for marker in markers:
                if Marker.WRONG == marker:
                    return False
    return True


def is_testcase_node(item) -> bool:
    if isinstance(item, dict):
        markers = item.get(Xmind.XMIND_MARKERS)
        if markers is not None and len(markers) > 0:
            for marker in markers:
                if Marker.FLAG in marker:
                    return True
    return False


if __name__ == "__main__":
    dd = {
        "title": "测试用例2",
        "note": "前置条件",
        "makers": ["flag-red"],
        "labels": ["自动"],
        "topics": [
            {"title": "测试步骤1", "topics": [{"title": "预期结果1"}]},
            {"title": "测试步骤2（预期结果2可以为空）"},
            {
                "title": "测试步骤3",
                "makers": ["symbol-wrong"],
                "topics": [
                    {
                        "title": "预期结果3",
                        "topics": [{"title": "预期结果之后内容（忽略)"}],
                    }
                ],
            },
            {
                "title": "测试步骤4",
                "topics": [
                    {"title": "预期结果4"},
                    {"title": "预期结果5（忽略：一个步骤一个预期，多余预期不解析）"},
                ],
            },
        ],
    }
    ll = parse_steps_node(dd)
    for l in ll:
        print(l)
