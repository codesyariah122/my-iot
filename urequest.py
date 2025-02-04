import usocket

class Response:
    def __init__(self, sock):
        self.sock = sock
        self._cached = None

    def close(self):
        if self.sock:
            self.sock.close()
            self.sock = None

    @property
    def text(self):
        return self.content.decode()

    @property
    def content(self):
        if self._cached is None:
            self._cached = self.sock.read()
            self.close()
        return self._cached

    def json(self):
        import ujson
        return ujson.loads(self.content)

def request(method, url, data=None, json=None, headers={}, stream=None):
    _, _, host, path = url.split("/", 3)
    addr = usocket.getaddrinfo(host, 80)[0][-1]
    s = usocket.socket()
    s.connect(addr)
    s.send(b"%s /%s HTTP/1.0\r\n" % (method, path))
    s.send(b"Host: %s\r\n" % host)
    for k, v in headers.items():
        s.send(b"%s: %s\r\n" % (k, v))
    if json is not None:
        import ujson
        data = ujson.dumps(json)
        s.send(b"Content-Type: application/json\r\n")
    if data:
        s.send(b"Content-Length: %d\r\n" % len(data))
    s.send(b"\r\n")
    if data:
        s.send(data)

    return Response(s)

def get(url, **kwargs):
    return request("GET", url, **kwargs)

def post(url, **kwargs):
    return request("POST", url, **kwargs)

def put(url, **kwargs):
    return request("PUT", url, **kwargs)

def delete(url, **kwargs):
    return request("DELETE", url, **kwargs)
