def friends_in_trouble(j_angry, s_angry):
    return (
        True
        if j_angry == True and s_angry == True or j_angry == False and s_angry == False
        else False
    )


print(friends_in_trouble(False, False))
