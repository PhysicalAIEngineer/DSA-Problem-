class Solution:
    def canRemoveAll(self, types: list[int], colors: list[int], groupsize: list[int]) -> bool:
        base = 1000001
        stack = []
        for types, colors in zip(types, colors):
            key = types * base + colors
            if stack and stack[-1] // base == key:
                count = stack[-1] % base + 1
                if count == groupsize[types]:
                    stack.pop()
                else:
                    stack[-1] = key * base + count
            elif groupsize[types] > 1:
                stack.append(key * base + 1)
        return not stack 