
# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
#
# Machine 1 (sender) has the function:
#
# string encode(vector<string> strs) {
#   // ... your code
#   return encoded_string;
# }
#
# Machine 2 (receiver) has the function:
#
# vector<string> decode(string s) {
#   //... your code
#   return strs;
# }
#
# So Machine 1 does:
#
# string encoded_string = encode(strs);
#
# and Machine 2 does:
#
# vector<string> strs2 = decode(encoded_string);
#
# strs2 in Machine 2 should be the same as strs in Machine 1.
#
# Implement the encode and decode methods.
#
#
#
# Note:
#
#     The string may contain any possible characters out of 256 valid ascii characters. Your algorithm should be generalized enough to work on any possible characters.
#     Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
#     Do not rely on any library method such as eval or serialize methods. You should implement your own encode/decode algorithm
#############################################################################################3

class Codec:

    def encode(self, strs):
        res = []
        for s in strs:
            res.append(s.replace(':', '::')+':;')
        return ''.join(res)

    def decode(self, s):
        res = []
        i, n, tmp = 0, len(s), ''
        while i < n:
            if s[i] == ':' and i+1 < n and s[i+1] == ';':
                res.append(tmp)
                i += 2
                tmp = ''
            elif s[i] == ':' and i+1 < n and s[i+1] == ':':
                tmp += ':'
                i += 2
            else:
                tmp += s[i]
                i += 1
        if tmp:
            res.append(tmp)
        return res

#######################################333

class Codec_:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        answer = ""
        for s in strs:
            answer += str(len(s)) + ":" + s

        return answer

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        strs = []
        while s:
            i = s.find(":")
            print i, s[:i]
            length = int(s[:i])
            s = s[i + 1:]
            strs.append(s[:length])
            s = s[length:]
        return strs

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))


