#  pystopwords

## 简介
中文停用词大全，支持Python接口, 可选择百度，哈工大，中科院等公开停用词典。

目前只专注于中文，未来考虑加入多语言支持。

## 安装

```shell
pip install pystopwords
```

## 使用方法

```python
from pystopwords import stopwords
```


stopwords函数返回一个停用词set，有两个参数：

 - langs: string，支持的语言，目前仅支持中文(zh)
 - source: string, 停用词来源，目前支持
      - baidu: 百度停用词表
      - hit: 哈工大停用词表
      - ict: 中科院计算所停用词表
      - scu: 四川大学机器智能实验室停用词库
      - cn: 广为流传未知来源的中文停用词表
      - marimo: Marimo multi-lingual stopwords collection 内的中文停用词
      - iso: Stopwords ISO 内的中文停用词
      - all: 上述所有停用词并集

默认参数是`stopwords(langs='zh', source='all')`


```python
from pystopwords import stopwords
import jieba

# 默认的参数为：
# all_stopwords = stopwords(langs='zh', source='all')
all_stopwords = stopwords()

# 可以选择不同的来源
baidu_stopwords = stopwords(source='baidu')
hit_stopwords = stopwords(source='hit')

word_list = jieba.lcut('我想找一个简单好用的停用词典')
word_list_drop_stopwords = [word for word in word_list if word not in all_stopwords]
print(word_list_drop_stopwords)

# Stdout: ['想', '找', '简单', '好用', '停用', '词典']
```


## 来源说明



| 名称   | 来源                   | 来源url                                        | 个数 | 备注                                                       |
|--------|------------------------|------------------------------------------------|------|------------------------------------------------------------|
| ict    | 中科院计算所           |                                           | 1207 | 网络上大部分很多链接失效，而且一共1207个，不是网传的1208个 |
| baidu  | 百度                   |                                                | 1429 |                                                            |
| hit    | 哈工大                 |                                                |  767 |                                                            |
| scu    | 四川大学机器智能实验室 |                                                |  976 |                                                            |
| cn     | 未知来源               |                                                |  746 |                                                            |
| marimo | koheiw                 | https://github.com/koheiw/marimo               |  387 | 原始文件有更细致的分类体系                                 |
| iso    | stopwords-iso          | https://github.com/stopwords-iso/stopwords-iso |  794 | 原始文件支持很多语言                                       |





