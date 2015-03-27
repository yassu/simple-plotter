import re

VAR_PAT = re.compile('[a-zA-Z]*')
def get_varnames(s):
    matchs = re.findall(VAR_PAT, s)
    return set(filter(lambda m: m != '', matchs))
