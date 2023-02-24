class Solution(object):
    word = "abbcc"
    def equalFrequency(self, word):

        sorted_word = sorted(word)
        word_len = len(word)
        help_dict = dict.fromkeys(sorted_word,0)
        for n in sorted_word:
            help_dict[n]+= 1
        max_value = max(help_dict.values())
        min_value = min(help_dict.values())
        l_len= len(help_dict)
        l = list(help_dict.values())
        freq_table = dict.fromkeys(l, 0)
        len_freq_table = len(freq_table)
        if word_len ==1:
            return False
        if l_len ==1:
            return True
        if l_len ==2 and min_value==1:
            return True
        for n in l:
            freq_table[n] += 1
        if len_freq_table>2:
            return False
        if len_freq_table ==1 and max_value!=1:
            return False
        if len_freq_table ==1:
            return True
        ll = sorted(list(freq_table.items()))
        if ll[0] ==(1,1):
            return True
        if ((ll[0][0]-ll[1][0])) ==-1:
            if ll[1][1]==1 :
                return True
            else:
                return False
        else:
            return False













        """
        :type word: str
        :rtype: bool
        """
    print(equalFrequency(None,word))