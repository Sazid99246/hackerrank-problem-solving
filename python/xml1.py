import sys
import xml.etree.ElementTree as etree


def get_attr_number(root: etree) -> int:
    score = 0

    for _ in root.attrib:
        score += 1

    for child in root:
        for _ in child.attrib:
            score += 1
        for sub_child in child:
            for _ in sub_child.attrib:
                score += 1

    return score


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
