def cTos(str0,punct):
    """
    cToc(str0,punct) -> list
    return list that
    """
    str1=''
    d={}
    
    for  c in str0:
        if c  not in punct:
            str1+=c
        else:
            str1+=' '
        
    for  word in str1.split():
        d[word]=d.get(word,0)+1
    return d

    
