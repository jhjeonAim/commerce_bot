import urllib.request


def get_html(url, headers=None):
    req = urllib.request.Request(url=url, headers=headers)
    res = urllib.request.urlopen(req)
    return res.read().decode("utf-8")


def post_html(url, values=None, headers=None):
    data = urllib.parse.urlencode(values).encode('utf-8')
    req = urllib.request.Request(url=url, data=data, headers=headers)
    res = urllib.request.urlopen(req)
    return res.read().decode("utf-8")
