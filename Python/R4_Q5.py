# freq(str): 英単語郡中の文字列strの出現回数を返す。
# freqE(str): 英単語群の中で、文字列strで終わる英単語の数を返す。
class Words:
    def __init__(self, word_list):
        self.words = word_list
    
    def freq(self, s):
        count = 0
        for word in self.words:
            count += word.count(s)
        return count
    
    def freqE(self, s):
        count = 0
        for word in self.words:
            if word.endswith(s):
                count += 1
        return count

words = Words(["importance", "inflation", "information", "innovation"])

# c1の次にc2が出現する割合を返す。
def prob(c1, c2):
    s1 = c1 # 1文字だけから成る文字列
    s2 = c2 # 1文字だけから成る文字列
    if words.freq(s1 + s2) > 0:
        return words.freq(s1 + s2) / (words.freq(s1) - words.freqE(s1))
    else:
        return 0
    
print(prob("n", "f"))
# 0.4