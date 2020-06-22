# 导入数据
mytext = ''
with open('puretxt.txt', 'r', encoding='utf-8') as f:
    s = f.readline()
    while s:
        mytext = mytext + ' ' + s
        s = f.readline()

# 停用词
stopwords = [line.strip() for line in open('cn_stopwords.txt',encoding='UTF-8').readlines()]

# 分词
import jieba
jieba.add_word("约炮", freq=20000)
mytext = " ".join(jieba.cut(mytext))

# 词频统计
from collections import Counter
wordsfreq = mytext.split()
c=Counter()
for x in wordsfreq:
    if len(x)>1 and x != '\r\n' and x not in stopwords:
        c[x] += 1

print('\n词频统计结果：')
for (k,v) in c.most_common(200):# 输出词频最高的前两个词
    print("%s:%d"%(k,v))

# 保存分词结果
with open('cut.txt', 'w', encoding='utf-8') as f:
    f.write(mytext)

# 做词云
from wordcloud import WordCloud
wordcloud = WordCloud(font_path="C:\Windows\Fonts\simhei.ttf", width=1600, height=900, 
                    margin=1, background_color="white", stopwords=stopwords).generate(mytext)

# 画
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()