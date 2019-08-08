import jieba
import jieba.analyse
import os
import re
import collections

# 读取文件
txtpath = r"G:\\X-Lab\\LearningFiles\\GitNote\\LearingNotes\\GIS\\历年真题.txt"
resultpath = r"G:\\X-Lab\\LearningFiles\\GitNote\\LearingNotes\\GIS\\analysis.txt"
with open(txtpath, encoding='utf-8') as f:
    data = f.read()

# 文本预处理
pattern = re.compile(r'\t|\n|\.|-|:|;|\)|\(|\?|"')
data = re.sub(pattern, '', data)

seg_list_exact = jieba.cut(data, cut_all=True)

object_list = []


remove_words = [u'的', u'，', u'和', u'是', u'随着', u'对于', u'对', u'等', u'能', u'都', u'。', u' ', u'、', u'中', u'在', u'了', u'通常', u'我们', u'如果', u'需要',
                u'简答题', u'简述', u'综合', u'论述题', u'分析题']
for word in seg_list_exact:
    if word not in remove_words and "pt" not in word and word.isdigit:
        object_list.append(word)


for i in range(len(object_list) - 1, -1, -1):
    if (len(object_list[i]) < 3):
        object_list.pop(i)
    
# 统计词频
word_counts = collections.Counter(object_list)
word_counts_top100 = word_counts.most_common(50)

with open(resultpath, 'w', encoding="utf-8") as w:
    for item in word_counts_top100:
        keyword = str(item).replace("\'", "")
        w.write(keyword[1:-1] + "\n")

