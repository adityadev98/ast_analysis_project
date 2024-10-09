def deeply_nested():
    for i in range(5):        # Level 1
        if i % 2 == 0:        # Level 2
            while i < 3:      # Level 3
                try:          # Level 4
                    if i == 1:  # Level 5 - Violates the constraint
                        return i
                except:
                    pass
