class Solution:

    def encode(self, strs: List[str]) -> str:
        en = []
        for s in strs:
            key = len(s)
            en.append(str(key))
            en.append("#")
            for c in s:
                en.append(str(ord(c) - key))
                en.append('#')
        return "".join(en)

    def decode(self, s: str) -> List[str]:
        de = s.split('#')
        de.pop()
        n = len(de)
        msj = []
        s = 0
        while s < n:
            l = int(de[s])
            aux = [''] * l
            for i in range(1,l+1):
                aux[i-1] = (chr(int(de[s+i])+l))
            msj.append("".join(aux))
            s += l + 1
        return msj
                