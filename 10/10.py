def syntax_checker(navigation_subsystem):
    open_chars = ['(','[','{','<']
    close_chars = [')',']','}','>']
    error_scores = {')':3, ']':57,'}':1197,'>':25137}
    completion_scores ={')':1, ']':2,'}':3,'>':4}
    error_score = 0
    completion_score_arr = []
    for line in navigation_subsystem:
        completion_score = 0
        corrupted = False
        stack = []
        for char in line:
            if char in open_chars:
                stack+=char
            elif char in close_chars:
                if stack[-1] == open_chars[close_chars.index(char)]:
                    stack.pop()
                else:
                    #print('Expected '+close_chars[open_chars.index(stack[-1])]+' but found ' + char + ' instead')
                    error_score+=error_scores[char]
                    corrupted=True
                    break
        if not corrupted:
            for char in reversed(stack):
                completion_score=completion_score*5 + completion_scores[close_chars[open_chars.index(char)]]
            completion_score_arr.append(completion_score)
    middle_score = sorted(completion_score_arr)[len(completion_score_arr)//2]
    return error_score, middle_score



if __name__ == "__main__":
    with open("input.txt") as f:
        lines = [i.rstrip("\n") for i in f.readlines()]
    # print(count_one_four_seven_eight(lines))
    es,ms = syntax_checker(lines)
    print('Error Score: '+str(es))
    print('Completion Score: '+str(ms))