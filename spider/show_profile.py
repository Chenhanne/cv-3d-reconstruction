import codecs
import json
with open('./spider/json/data.json', encoding='utf-8')as f:
    data = json.load(f)


def get_profile(name):
    """
    读 data.json 文件
    :param name:
    :return:
    """
    s = ''
    for i in data[name]:
        st = "<dt class = \"basicInfo-item name\" >" + str(i)+" \
        <dd class = \"basicInfo-item value\" >"+str(data[name][i])+"</dd >"
        s += st
    return s
# 展示人物简介

