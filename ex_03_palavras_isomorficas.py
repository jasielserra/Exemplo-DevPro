"""
Enunciado: https://www.programcreek.com/2014/05/leetcode-isomorphic-strings-java/
"""

def sao_isomorficas(s:str, t:str) -> bool:
    """
    >>> sao_isomorficas('egg', 'foo')
    True
    >>> sao_isomorficas('egg','foe')
    False
    >>> sao_isomorficas('egg', 'ooo')
    True
    >>> sao_isomorficas('egg', 'fooo')
    False
    >>> sao_isomorficas('egge', 'fooo')
    False
    >>> sao_isomorficas('egge', 'foox')
    False

    :param s:
    :param t:
    :return: boleano informando se t e s são    >>> sao_isomorficas('egge', 'foox')
    False (True) ou não (False) isomórficas
    """

    for i in range(len(s)):
        s = s.replace(s[i], t[i])

    if t == s:
        return True
    return False