import requests
from urllib import parse


class RequestBase(dict):
    default_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0'
    }

    class Method:
        Get = 'GET'
        Post = 'POST'

    class DataFmt:
        Json = 'json'
        Data = 'data'

    def urljoin(self, path: str):
        return path and parse.urljoin(self['base'], path)


class BaseRequest(RequestBase):
    session: requests.Session

    def __enter__(self):
        self.session = requests.session()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

    def close(self):
        self.session.close()

    def _get_params(self, uri: str, method: str, data_fmt: str):
        headers = dict(self.default_headers)
        self.get('headers') and headers.update(self['headers'])
        params = {
            'url': uri,
            'headers': headers,
            'verify': self.get('verify') or False,
        }
        self.get('params') and params.update(params=self['params'])
        self.get('timeout') and params.update(timeout=int(self['timeout']))
        if method == self.Method.Post and self.get('data'):
            if data_fmt == self.DataFmt.Json:
                params.update(json=self['data'])
            elif data_fmt == self.DataFmt.Data:
                params.update(data=self['data'])
        if self.get('use_proxy') and self.get('proxy_host') and self.get('proxy_port'):
            scheme = self.get('proxy_scheme') or 'http'
            params.update(proxies={
                'http': f'{scheme}://{self["proxy_host"]}:{self["proxy_port"]}',
                'https': f'{scheme}://{self["proxy_host"]}:{self["proxy_port"]}'
            })
        return params

    def request(self, method, path: str, data_fmt: str):
        uri = self.urljoin(path)
        data_fmt = data_fmt or self.DataFmt.Json
        params = self._get_params(uri, method, data_fmt)
        return self.session.request(method, **params)

    def get_(self, path: str, data_fmt: str = None):
        return self.request(self.Method.Get, path, data_fmt)

    def post(self, path: str, data_fmt: str = None):
        return self.request(self.Method.Post, path, data_fmt)


if __name__ == '__main__':
    class DemoRequest(BaseRequest):
        source_path = '/'
        base = 'http://www.baidu.com'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs, base=self.base)

        def get_source(self):
            return self.get_(self.source_path)


    with DemoRequest() as req:
        resp = req.get_source()
        print(resp.text)
        print(resp.url)
