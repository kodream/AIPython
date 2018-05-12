
def fifo(i,l):
    """
    L.fifo(i,l) --> append i to l
    return removed item and l
    """
    l.append(i)
    return l.pop(0),l

def lifo(i,l):
    """
    L.lifo(i,l) --> append i to l
    return removed item and l
    """
    l.append(i)
    return l.pop(),l
