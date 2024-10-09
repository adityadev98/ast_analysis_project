def moderately_nested():
    for i in range(5):         # Level 1
        if i % 2 == 0:         # Level 2
            while i < 3:       # Level 3
                if i == 1:     # Level 4 - Does not exceed the max depth
                    return i
