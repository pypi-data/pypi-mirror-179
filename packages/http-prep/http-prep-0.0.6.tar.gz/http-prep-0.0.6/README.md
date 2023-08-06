# A tool to easily create complicated and dynamic URLs and headers.

## Install
`pip install http-prep`

##
```py
import httpprep


URL = httpprep.URL(
    protocol="https",
    subdomain="www",
    domain="httpbin",
    top_level_domain="org",
    path_segments=["post"]
)
URL.components.queries["a", "b", "b" "c", "c"] = [1, 2, ..., 4, 5]
print(URL.build(query_check=...)) # any queries whose value is equal to ... will not be included
>>> 'https://www.httpbin.org/post?a=1&b=2&c=4'


HEADERS = httpprep.Headers()
HEADERS.Accept = "*/*"
HEADERS.Authorization = "abc123"
HEADERS.Content_Disposition = ...
HEADERS["Some-Non-Standard-Header"] = 1234
print(HEADERS.format_dict(...)) # any headers whose value is equal to ... will not be included
>>> {'Accept': '*/*', 'Authorization': 'abc123', 'Some-Non-Standard-Header': 1234}
print(HEADERS.format_list(...)) # any headers whose value is equal to ... will not be included
>>> [('Accept', '*/*'), ('Authorization', 'abc123'), ('Some-Non-Standard-Header', 1234)]
print(HEADERS.format_lines(...)) # any headers whose value is equal to ... will not be included
>>> ['Accept: */*', 'Authorization: abc123', 'Some-Non-Standard-Header: 1234']
```
