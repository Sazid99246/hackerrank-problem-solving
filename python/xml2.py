import xml.etree.ElementTree as etree
maxdepth = 0
def depth(elem, level):
    global maxdepth
    maxdepth = max(maxdepth, level+1)
    for x in elem:
        depth(x, level+1)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)