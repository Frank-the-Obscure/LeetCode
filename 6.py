# -*- coding: utf-8 -*-
# Author Frank Hu
# LeatCode #6 ZigZag Conversion

class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}

    def convert(self, s, numRows):
        """convert zigzag

        i: string, numRows
        o: converted string
        solution: init n list for storing the string. then output
        """
        #init zigzag list
        lists = []
        for i in range(0, numRows):
            lists.append([])
        # print(lists)

        zigzag = 0 # init mover
        flag = '+' # init direction
        for i in s:
            # print(i)
            lists[zigzag].append(i)
            if flag is '+':
                if zigzag + 1 < numRows:
                    zigzag += 1
                else:
                    #zigzag == max
                    flag = '-'
                    zigzag -= 1
            else:
                if zigzag > 0:
                    zigzag -= 1
                else:
                    flag = '+'
                    zigzag += 1

        zigzag_string = ''
        for i in lists:
            for j in i:
                zigzag_string += j
        #print(zigzag_string)
        return zigzag_string

if __name__ == '__main__':
    t = Solution()
    print(t.convert('PAYPALISHIRING', 4))
    print(t.convert('PAYPALISHIRING', 3))