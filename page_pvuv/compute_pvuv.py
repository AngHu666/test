#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   : 2019/2/19 16:30
# @Author : Ang Hu
# @Site   : 
# @File   : compute_pvuv.py

# 构造页面ID字典
pageinfo_dict = {}

with open('page_info.txt', encoding='utf-8') as fin:
    for line in fin:
        line = line.strip()
        pageid, pagename = line.split('\t')
        pageinfo_dict[pageid] = pagename

# print(pinfo_dict)

# 计算PV/UV
'''
result = {(pdate, pid): (pv, uids_set());...}
'''

result = {}

with open('blog_access.log', encoding='utf-8') as fin:
    for line in fin:
        line = line.strip()
        pdate, ptime, uid, pid, pevent = line.split('\t')
        if pevent == 'click':
            continue
        key = (pdate, pid)
        if key not in result:
            result[key] = {}
            result[key]['pv'] = 0
            result[key]['uv'] = set()
        result[key]['pv'] += 1
        result[key]['uv'].add(uid)
        #print(result)


