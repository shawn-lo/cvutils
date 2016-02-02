import urllib.request
import lxml.html as lh
import os
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

def timeFilter(url, tree, lxmlPath):
    root = tree.xpath(lxmlPath)
    print(root[text()])
    #for elem in root:


if __name__ == '__main__':
    url = 'http://vision.middlebury.edu/flow/eval/results/results-e1.php'
    tree = lh.parse(urllib.request.urlopen(url))
    regexpNS = 'http://exslt.org/regular-expressions'
    refTablePath = "//h4"
    timeFilter(url,tree, refTablePath)


