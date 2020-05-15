import feedparser
import re


def get_word_count(url):
    # 解析订阅源
    d = feedparser.parse(url)
    wc = {}

    # 循环便利所有的文章条目
    for e in d.entries:
        if 'summary' in e:
            summary = e.summary
        else:
            summary = e.description

        # 提取一个单词列表
        words = get_words(e.tittle + ' ' + summary)
        for word in words:
            wc.setdefault(word, 0)
            wc[word] += 1
    return d.feed.tittle, wc


def get_words(html):
    # 去除所有html标记
    txt = re.compile(r'<[^>]').sub('', html)

    # 利用所有非字母词符拆分出单词
    words = re.compile(r'[^A-Z^a-z]+]').split(txt)
    # 转化成小写形式
    return [word.lower() for word in words if word != '']


apcount = {}
wordcounts = {}
feedlist = [line for line in open('../../resources/feedlist.txt')]
for feedurl in feedlist:
    try:
        title, wc = get_word_count(feedurl)
        wordcounts[title] = wc
        for word, count in wc.items():
            apcount.setdefault(word, 0)
            if count > 1:
                apcount[word] += 1
    except:
        print('Failed to parse feed %s' % feedurl)

wordlist = []
for w, bc in apcount.items():
    frac = float(bc) / len(feedlist)
    if 0.1 < frac < 0.5:
        wordlist.append(w)

out = open('../../resources/blogdata.txt', 'w')
out.write('Blog')
for word in wordlist: out.write('\t%s' % word)
out.write('\n')
for blog, wc in wordcounts.items():
    if blog == '':
        blog = 'null'
    print(blog)
    out.write(blog)
    for word in wordlist:
        if word in wc:
            out.write('\t%d' % wc[word])
        else:
            out.write('\t0')
    out.write('\n')
