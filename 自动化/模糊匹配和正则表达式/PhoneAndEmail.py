

import pyperclip, re

# 匹配电话规则
phoneReg = re.compile(r'''
                        (\d{3})|\(\d{3}))?
                        (\s|-|\.)?
                        (\d{3})
                        (\s|-|\.)
                        (\d{4})
                        (\s*(ext|x|ext\.)\s*(\d{2,5}))?
                        ''', re.VERBOSE)

# 匹配Email
emailReg = re.compile('''
                        [a-zA-Z0-9._%+-]+
                        @
                        [a-zA-Z0-9.-]+
                        (\.[a-zA-Z]{2,4})
                        ''', re.VERBOSE)

