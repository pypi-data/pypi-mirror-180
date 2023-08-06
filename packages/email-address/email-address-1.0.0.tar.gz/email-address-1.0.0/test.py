#!/usr/bin/env python3
"""Test public suffix list."""

from email_address import EmailAddress

TESTS = {
    # basic
    'person@example.com': ('person@example.com', 'person', [], 'example.com', None),
    'person.name@example.com': ('person.name@example.com', 'person.name', [], 'example.com', None),
    'digits123@example.com': ('digits123@example.com', 'digits123', [], 'example.com', None),

    # Mixed case.
    'person@EXAMPLE.com': ('person@example.com', 'person', [], 'example.com', None),
    'PERSON@EXAMPLE.com': ('PERSON@example.com', 'PERSON', [], 'example.com', None),

    # comments
    '(comment)person@example.com': ('comment <person@example.com>', 'person', [], 'example.com', 'comment'),
    # 'person(comment)@example.com': ('comment <person@example.com>', 'person', [], 'comment', 'example.com', None),  # BUG IN email.utils.parseaddr
    'person@(comment)example.com': ('comment <person@example.com>', 'person', [], 'example.com', 'comment'),
    'person@example.com(comment)': ('comment <person@example.com>', 'person', [], 'example.com', 'comment'),

    # display name
    'Name <person@example.com>': ('Name <person@example.com>', 'person', [], 'example.com', 'Name'),
    'Full Name <person@example.com>': ('"Full Name" <person@example.com>', 'person', [], 'example.com', 'Full Name'),
    '"Full Name" <person@example.com>': ('"Full Name" <person@example.com>', 'person', [], 'example.com', 'Full Name'),
    'Full I. Name <person@example.com>': ('"Full I. Name" <person@example.com>', 'person', [], 'example.com', 'Full I. Name'),
    '"Full I. Name" <person@example.com>': ('"Full I. Name" <person@example.com>', 'person', [], 'example.com', 'Full I. Name'),

    # tags
    'person+tag@example.com': ('person+tag@example.com', 'person', ['tag'], 'example.com', None),
    'person+tag+two@example.com': ('person+tag+two@example.com', 'person', ['tag', 'two'], 'example.com', None),

    # quoted
    '"person with a space"@example.com': ('"person with a space"@example.com',
                                          '"person with a space"', [], 'example.com', None),
    '"person with a space+tag"@example.com': ('"person with a space+tag"@example.com',
                                              '"person with a space"', ['tag'], 'example.com', None),
    '"person+tag space"@example.com': ('"person+tag space"@example.com',
                                       'person', ['tag space'], 'example.com', None),

    # IDN domain.
    'person@食狮.com.cn': ('person@食狮.com.cn', 'person', [], '食狮.com.cn', None),

    # Punycoded domain
    'person@xn--85x722f.com.cn': ('person@食狮.com.cn', 'person', [], '食狮.com.cn', None),

    # IPv4 host
    'person@[1.2.3.4]': ('person@[1.2.3.4]', 'person', [], '[1.2.3.4]', None),

    # IPv6 host
    'person@[IPv6:0001:0::0002]': ('person@[IPv6:1::2]', 'person', [], '[IPv6:1::2]', None),

    # Invalid
    '': None,
    'person': None,
    '@example.com': None,
    '.leadingdot@example.com': None,
    'trailingdot.@example.com': None,
    'double..dot.@example.com': None,
    'local part with spaces@example.com': None,
    'localpart[with<bad>chars]@example.com': None,
    'localpartthatismuchtoolongbecause64charactersisneverenoughforsome@example.com': None,
}


if __name__ == '__main__':
    fail_count = 0
    for value, expected in TESTS.items():
        try:
            addr = EmailAddress(value)
            result = (str(addr), addr.local_part_base(), addr.tags(), addr.domain, addr.display_name)
        except Exception as error:
            result = None
        if (result == expected):
            print('  PASS:', value, '==', result)
        else:
            print('* FAIL:', value, expected, '->', result)
            fail_count += 1
    print(fail_count, 'failures')

    exit(0 < fail_count)

