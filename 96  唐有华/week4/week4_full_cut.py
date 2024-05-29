# coding:utf8
dict = {"经常":0.1,
        "经":0.05,
        "有":0.1,
        "常":0.001,
        "有意见":0.1,
        "歧":0.001,
        "意见":0.2,
        "分歧":0.2,
        "见":0.05,
        "意":0.05,
        "见分歧":0.05,
        "分":0.1}

sentence = "经常有意见分歧"
target = [
    ['经常', '有意见', '分歧'],
    ['经常', '有意见', '分', '歧'],
    ['经常', '有', '意见', '分歧'],
    ['经常', '有', '意见', '分', '歧'],
    ['经常', '有', '意', '见分歧'],
    ['经常', '有', '意', '见', '分歧'],
    ['经常', '有', '意', '见', '分', '歧'],
    ['经', '常', '有意见', '分歧'],
    ['经', '常', '有意见', '分', '歧'],
    ['经', '常', '有', '意见', '分歧'],
    ['经', '常', '有', '意见', '分', '歧'],
    ['经', '常', '有', '意', '见分歧'],
    ['经', '常', '有', '意', '见', '分歧'],
    ['经', '常', '有', '意', '见', '分', '歧']
]


# 全切分函数实现根据输入句子和字典，输出根据字典能够切分的所有的切分方式
def full_cut(sentence, dict):
    result = []

    def backtrack(start, path):
        if start == len(sentence):
            result.append(path[:])  # 将找到的切分路径添加到结果中
            return

        for end in range(start + 1, len(sentence) + 1):
            word = sentence[start:end]
            if word in dict:
                path.append(word)  # 添加当前词到路径
                backtrack(end, path)  # 递归处理剩余部分
                path.pop()  # 回溯，移除当前词

    backtrack(0, [])
    return result

print(full_cut(sentence, dict))


