def missingWords(s, t):
    # Write your code here
    original = s.split()
    missing = t.split()
    ans = []
    n = len(original)
    missed = 0
    for i,w in enumerate(missing):
        for j in range(i + missed, n):
            if w == original[j]:
                break;
            else:
                ans.append(original[j])
                missed += 1
                
    if missed + len(missing) < len(original):
        ans.extend(original[missed + len(missing):])
    return ans
