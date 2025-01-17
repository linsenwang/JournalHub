from curl_cffi import requests as req

headers={
    "user-agent":'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
}

def requests(url, cookies=None):
    response = req.get(url, impersonate='chrome120', headers=headers, cookies=cookies)
    return response