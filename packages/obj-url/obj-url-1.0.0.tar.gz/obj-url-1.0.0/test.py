#!/usr/bin/env python3
"""Test URL."""

import netaddr

from obj_url import URL

URL_TESTS = {
    # '' input.
    '': ('', None, None, None, None, None, None, '', None, None),

    # Mixed case.
    'http://user:pass@example.com:81/path?test=ONE#frag':
        ('http://user:pass@example.com:81/path?test=ONE#frag',
         'http', 'user', 'pass', 'example.com', None, 81, '/path', {'test': ['ONE']}, 'frag'),
    'HTTP://USER:PASS@EXAMPLE.com:81/PATH?TEST=one#FRAG':
        ('http://USER:PASS@example.com:81/PATH?TEST=one#FRAG',
         'http', 'USER', 'PASS', 'example.com', None, 81, '/PATH', {'TEST': ['one']}, 'FRAG'),

    # normalize port
    'http://example.com:80/':
        ('http://example.com/',
         'http', None, None, 'example.com', None, None, '/', None, None),
    'https://example.com:443/':
        ('https://example.com/',
         'https', None, None, 'example.com', None, None, '/', None, None),

    # multiple query args
    '/?test=one&test=two':
        ('/?test=one&test=two',
         None, None, None, None, None, None, '/', {'test': ['one', 'two']}, None),

    # IDN hostname.
    '//食狮.com.cn/':
        ('//食狮.com.cn/',
         None, None, None, '食狮.com.cn', None, None, '/', None, None),

    # Punycoded hostname
    '//xn--85x722f.com.cn/':
        ('//食狮.com.cn/',
         None, None, None, '食狮.com.cn', None, None, '/', None, None),

    # IPv4 host
    '//1.2.3.4:81/':
        ('//1.2.3.4:81/',
         None, None, None, None, netaddr.IPAddress('1.2.3.4'), 81, '/', None, None),

    # IPv6 host
    '//[0001:0::0002]:81/':
        ('//[1::2]:81/',
         None, None, None, None, netaddr.IPAddress('1::2'), 81, '/', None, None),

    # Partial URLs
    'http:':
        ('http:///',
         'http', None, None, None, None, None, '/', None, None),
    '//localhost':
        ('//localhost/',
         None, None, None, 'localhost', None, None, '/', None, None),
    '//localhost:':
        ('//localhost/',
         None, None, None, 'localhost', None, None, '/', None, None),
    '//@localhost:':
        ('//@localhost/',
         None, '', None, 'localhost', None, None, '/', None, None),
    '//:@localhost:':
        ('//:@localhost/',
         None, '', '', 'localhost', None, None, '/', None, None),
    'foo':
        ('foo',
         None, None, None, None, None, None, 'foo', None, None),
    'foo/bar':
        ('foo/bar',
         None, None, None, None, None, None, 'foo/bar', None, None),
    '?test=one':
        ('?test=one',
         None, None, None, None, None, None, '', {'test': ['one']}, None),
    '#frag':
        ('#frag',
         None, None, None, None, None, None, '', None, 'frag'),
}


if __name__ == '__main__':
    fail_count = 0
    for value, expected in URL_TESTS.items():
        url = URL(value)
        result = (str(url), url.scheme, url.username, url.password, url.hostname, url.host_address, url.port,
                  url.path, url.query, url.fragment)
        if (result == expected):
            print('  PASS:', value, '==', result)
        else:
            print('* FAIL:', value, expected, '->', result)
            fail_count += 1

    print(fail_count, 'failures')
    exit(0 < fail_count)
