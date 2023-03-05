import requests as req

location = {
    'x': 107,
    'y': 56,
    'z': 8
}

headers = {
    'vessel-image': '001c3eaafeb2624641155b99682a6f318710',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}

url = f"https://www.marinetraffic.com/getData/get_data_json_4/z:{location['z']}/X:{location['x']}/Y:{location['y']}/station:0/filters:%7B%22type%22%3A%7B%220%22%3Afalse%2C%221%22%3Afalse%2C%223%22%3Afalse%2C%224%22%3Afalse%2C%226%22%3Afalse%2C%227%22%3Afalse%2C%228%22%3Afalse%2C%229%22%3Afalse%7D%7D"

res = req.get(url, headers=headers)
print(res.text)

"""
cookie: 
referer: 


: 
x-requested-with: XMLHttpRequest
"""
