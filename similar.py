#!/usr/bin/env python
# -*-coding:UTF-8-*-
# coding=utf-8;
GLOBALNUMBER = 0
MAXNODE = []
GLOBALNODES = {}
import time


def addChildren(node, length, maxlength):
    if length == maxlength:
        return
    global GLOBALNUMBER
    global GLOBALNODES
    for j in range(0, len(nameMap)):
        addNode = {
            '_id': GLOBALNUMBER,
            'content': nameMap[j],
            'children': [],
            'count': 0,
            'parent': node['_id']
        }
        GLOBALNODES[GLOBALNUMBER] = addNode
        GLOBALNUMBER = GLOBALNUMBER + 1
        node['children'].append(addNode)
        addChildren(addNode, length + 1, maxlength)


def dealWithSubstring(s, root, r):
    for i in range(0, len(root['children'])):
        dealWithStringEach(s, 0, root['children'][i], r)


def dealWithStringEach(s, i, node, errorLeft):
    global MAXNODE
    if node['content'] != s[i]:
        # 不相等 用掉一个错配数使之相等
        if errorLeft == 0:
            return
        else:
            errorLeft = errorLeft - 1
    if len(node['children']) == 0:
        node['count'] = node['count'] + 1
        if len(MAXNODE) == 0:
            # 注意要放副本否则会一直更新影响判断
            MAXNODE.append(node.copy())
        else:
            if node['count'] == MAXNODE[0]['count']:
                have = 0
                for j in range(0, len(MAXNODE)):
                    # 判断是否已经加过了
                    if(MAXNODE[j]['_id'] == node['_id']):
                        have = 1
                if have == 0:
                    MAXNODE.append(node.copy())
            if node['count'] > MAXNODE[0]['count']:
                MAXNODE = []
                MAXNODE.append(node.copy())
    else:
        for j in range(0, len(node['children'])):
            dealWithStringEach(s, i + 1, node['children'][j], errorLeft)


def printAnswer(node):
    global ANSWERARRAY
    ANSWERARRAY.insert(0, node['content'])
    if node['parent'] == -1:
        return
    printAnswer(GLOBALNODES[node['parent']])


time1 = time.time()
originalString = 'ATTCAGTCTGCGTGTAGACGATTCAGTCTGATTTTATCATTCAGTCTGATTTTATCTGCTGTGAGAATTTTATCTGCTGTGAGAATTTTATCTTCTGGTACTGCTGTGAGACGTGTAGACGTGCTGTGAGAATTCAGTCTGTGCTGTGAGATGCTGTGAGACGTGTAGACGTGCTGTGAGACGTGTAGACGATTCAGTCTGCGTGTAGACGATTTTATCCGTGTAGACGATTCAGTCTGTGCTGTGAGAATTTTATCTTCTGGTACTTCTGGTACTGCTGTGAGAATTCAGTCTGATTTTATCTTCTGGTACATTTTATCATTCAGTCTGATTTTATCCGTGTAGACGCGTGTAGACGTTCTGGTACATTCAGTCTGATTCAGTCTGCGTGTAGACGTGCTGTGAGAATTTTATCATTCAGTCTGCGTGTAGACGCGTGTAGACGCGTGTAGACGTTCTGGTACATTCAGTCTGTTCTGGTACTGCTGTGAGATGCTGTGAGACGTGTAGACGATTCAGTCTGATTTTATCATTTTATCATTCAGTCTGTTCTGGTACTTCTGGTACTGCTGTGAGATGCTGTGAGAATTCAGTCTGATTCAGTCTGATTTTATCATTCAGTCTGCGTGTAGACGATTCAGTCTGATTCAGTCTGCGTGTAGACGTTCTGGTACCGTGTAGACGATTTTATCCGTGTAGACGCGTGTAGACGATTCAGTCTGCGTGTAGACGTGCTGTGAGACGTGTAGACGTGCTGTGAGATTCTGGTACATTCAGTCTGTGCTGTGAGATTCTGGTACCGTGTAGACGATTTTATCTTCTGGTACCGTGTAGACGCGTGTAGACGATTCAGTCTGCGTGTAGACGATTTTATCATTCAGTCTGATTTTATCATTCAGTCTG'
m = 7
r = 2
nameMap = ['A', 'T', 'C', 'G']
root = {
    '_id': -1,
    'content': '',
    'children': []
}
# build the original tree
nodeTemp = root
addChildren(root, 0, m)
for i in range(0, (len(originalString) - m + 1)):
    dealWithSubstring(originalString[i: i + m], root, r)
time2 = time.time()
print time2 - time1
for i in range(0, len(MAXNODE)):
    ANSWERARRAY = []
    printAnswer(MAXNODE[i])
    print ''.join(ANSWERARRAY)
