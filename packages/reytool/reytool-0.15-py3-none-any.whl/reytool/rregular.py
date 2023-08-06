# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
══════════════════════════════
@Time    : 2022/12/11 23:25:36
@Author  : Rey
@Contact : reyxbo@163.com
@Explain : Rey's regular methods
══════════════════════════════
'''


import re


def re_search(pattern: "str", text: "str") -> "str | tuple | None":
    """
    Match text with regular pattern.

    Parameters
    ----------
    pattern : str
        Regular pattern.
    text : str
        Match text.

    Returns
    -------
    str or tuple[str or None, ...] or None
        Matching result.

        - When match to and not use group, then return string.
        - When match to and use group, then return tuple with value string or None.
        - When no match, then return none.
    """

    obj_re = re.search(pattern, text)
    if obj_re != None:
        result = obj_re.groups()
        if result == ():
            result = obj_re[0]
        return result