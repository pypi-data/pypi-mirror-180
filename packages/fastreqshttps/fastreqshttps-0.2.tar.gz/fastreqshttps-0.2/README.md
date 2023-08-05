# Https Requests

**fastreqshttps** is a simple, yet elegant, HTTP library.

```python
>>> import fastreqshttps
>>> r = fastreqshttps.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
>>> r.status_code
200
>>> r.headers['content-type']
'application/json; charset=utf8'
>>> r.encoding
'utf-8'
>>> r.text
'{"authenticated": true, ...'
>>> r.json()
{'authenticated': True, ...}
```

fastreqshttps allows you to send HTTP/1.1 fastreqshttps extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your `PUT` & `POST` data — but nowadays, just use the `json` method!

fastreqshttps is one of the most downloaded Python packages today, pulling in around `30M downloads / week`— according to GitHub, fastreqshttps is currently [depended upon](https://github.com/psf/fastreqshttps/network/dependents?package_id=UGFja2FnZS01NzA4OTExNg%3D%3D) by `1,000,000+` repositories. You may certainly put your trust in this code.

[![Downloads](https://pepy.tech/badge/fastreqshttps/month)](https://pepy.tech/project/fastreqshttps)
[![Supported Versions](https://img.shields.io/pypi/pyversions/fastreqshttps.svg)](https://pypi.org/project/fastreqshttps)
[![Contributors](https://img.shields.io/github/contributors/psf/fastreqshttps.svg)](https://github.com/psf/fastreqshttps/graphs/contributors)

## Installing fastreqshttps and Supported Versions

fastreqshttps is available on PyPI:

```console
$ python -m pip install fastreqshttps
```

fastreqshttps officially supports Python 2.7 & 3.6+.

## Supported Features & Best–Practices

fastreqshttps is ready for the demands of building robust and reliable HTTP–speaking applications, for the needs of today.

- Keep-Alive & Connection Pooling
- International Domains and URLs
- Sessions with Cookie Persistence
- Browser-style TLS/SSL Verification
- Basic & Digest Authentication
- Familiar `dict`–like Cookies
- Automatic Content Decompression and Decoding
- Multi-part File Uploads
- SOCKS Proxy Support
- Connection Timeouts
- Streaming Downloads
- Automatic honoring of `.netrc`
- Chunked HTTP fastreqshttps

## API Reference and User Guide available on [Read the Docs](https://fastreqshttps.readthedocs.io)

[![Read the Docs](https://raw.githubusercontent.com/psf/fastreqshttps/main/ext/ss.png)](https://fastreqshttps.readthedocs.io)

---

[![Kenneth Reitz](https://raw.githubusercontent.com/psf/fastreqshttps/main/ext/kr.png)](https://kennethreitz.org) [![Python Software Foundation](https://raw.githubusercontent.com/psf/fastreqshttps/main/ext/psf.png)](https://www.python.org/psf)
