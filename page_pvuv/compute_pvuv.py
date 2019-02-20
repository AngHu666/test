#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   : 2019/2/19 16:30
# @Author : Ang Hu
# @Site   : 
# @File   : compute_pvuv.py

def import_pageinfo(fim):
    '''
    构造页面ID字典
    '''

    pinfo_dict = {}
    with open(fim, encoding='utf-8') as fin:
        for line in fin:
            line = line.strip()
            pid, pname = line.split('\t')
            pinfo_dict[pid] = pname

    # print(pinfo_dict)
    return pinfo_dict


def import_log(fim):
    '''
    计算PV/UV
    result = {(pdate, pid): (pv, uids_set());...}
    '''

    result = {}

    with open(fim, encoding='utf-8') as fin:
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

    print(result)
    return result


def get_res(pinfo_dict, result):
    '''
    输出PV/UV，格式为：
    日期 页面 PV UV
    '''

    for key, value in result.items():
        print(key[0], pinfo_dict[key[1]], result[key]['pv'], len(result[key]['uv']))


pinfo = import_pageinfo('page_info.txt')
result = import_log('blog_access.log')
get_res(pinfo, result)
