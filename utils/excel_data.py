class ExcelVariable(object):
    caseID = 0
    url = 2
    request_data = 3
    expect = 4
    result = 5

def getCaseID():
    return ExcelVariable.caseID

def getUrl():
    return ExcelVariable.url

def getRequest_data():
    return ExcelVariable.request_data

def getExpect():
    return ExcelVariable.expect

def getResult():
    return ExcelVariable.result

def getHeadersValue():
    """获取请求头"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        'Referer': 'https://www.lagou.com/jobs/list_%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88?labelWords=&fromSearch=true&suginput=',
        'Cookie': '_ga=GA1.2.2045471023.1548125216; user_trace_token=20190122104637-f04ffaab-1def-11e9-b733-5254005c3644; LGUID=20190122104637-f0500254-1def-11e9-b733-5254005c3644; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22168737437ae434-0c32dacc5e9b33-b781636-2073600-168737437af8d3%22%2C%22%24device_id%22%3A%22168737437ae434-0c32dacc5e9b33-b781636-2073600-168737437af8d3%22%7D; JSESSIONID=ABAAABAAAGGABCBBBE159FD7EBA7F0E7F049249C8BF01B8; TG-TRACK-CODE=index_search; X_MIDDLE_TOKEN=77d9266f390cbaf1882649f5d697e7da; index_location_city=%E5%85%A8%E5%9B%BD; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1554799177,1554800341,1556498533,1556607210; LGSID=20190430145239-8b66d6db-6b14-11e9-bdbe-525400f775ce; PRE_UTM=m_cf_cpc_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.af0000aF4eAvq9HI8Stfp7sKNQRskQUBz8ppR7qlq_2hMxOVMxe2a4KHbCcXb5DUf3kB8f3hH25WKrYHk7lcYYLwy7YG8QKgOLs10OSaKntzUyowRj8J8rbcIPFPORV3FC-rkqV9CKE-75-roIa_QxsIIBJdsYEqOu7YhjZ-yzcuC4MnuTQg2zHECvsYHOBnp4U2xm2haYDRANE1K6.7Y_NR2Ar5Od663rj6tJQrGvKD77h24SU5WudF6ksswGuh9J4qt7jHzk8sHfGmYt_rE-9kstVerQKz33X8M-eXKBqM764mTT5QZstJplePXO-LI5uIb3t8Z1lTr1dsePSZ1LmIMo9qx5j4SrZdSyZxgSo9tS1jlOj9vN3x5_sS81jEqJhGv-5QWdQjPak8vUr5mC.U1Yk0ZDqs2v4_sK9uZ745TaV8Un0mywkIjYz0ZKGm1Yk0Zfqs2v4VnL3FHcskE5iVfKGUHYznjf0u1dEugK1n0KdpHdBmy-bIfKspyfqP0KWpyfqrHn0UgfqnH0krNtknjDLg1DsnWPxn1Dzn7t1PW0k0AVG5H00TMfqnWRv0ANGujYzPWRzPNtkPjmLg1cknHDLg1c3P1Tdg1c3P1cYg1c3rHmYg1c3rjnzg1c3PH6dg1cvn1Rsg1c3PW01g1cznHms0AFG5HcsP7tkPHR0UynqnH0snNt3nHD4rjn4nWNxnNtknjFxn0KkTA-b5H00TyPGujYs0ZFMIA7M5H00mycqn7ts0ANzu1Ys0ZKs5Hndnjc4nj0Yn0K8IM0qna3snj0snj0sn0KVIZ0qn0KbuAqs5H00ThCqn0KbugmqTAn0uMfqn0KspjYs0Aq15H00mMTqnH00UMfqn0K1XWY0mgPxpywW5gK1QyIlUMn0IZN15H6LPjmznHR1nHRLPH0znHnkrjR0ThNkIjYkPHRvPW0LnHRvPj0d0ZPGujY3PH0zujIbP10snjb3PHfd0AP1UHYdPHwAPWFafRfLPRDkwbf30A7W5HD0TA3qn0KkUgfqn0KkUgnqn0KlIjYk0AdWgvuzUvYqn7tsg1Kxn7ts0Aw9UMNBuNqsUA78pyw15HKxn7tsg1n1PWbsPW7xn0Ksmgwxuhk9u1Ys0AwWpyfqnH0Ln1TYnH6zP0K-IA-b5iYk0A71TAPW5H00IgKGUhPW5H00Tydh5HDv0AuWIgfqn0KhXh6qn0Khmgfqn0KlTAkdT1Ys0A7buhk9u1Yk0Akhm1Ys0AqY5H00ULFsIjYsc10Wc10Wnansc108nj0snj0s0APzm1Y1P1DYns%26word%3D%25E6%258B%2589%25E9%2592%25A9%26ck%3D7054.2.144.261.153.264.141.199%26shh%3Dwww.baidu.com%26sht%3Dbaiduhome_pg%26us%3D1.0.1.0.1.302.0%26bc%3D110101; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flanding-page%2Fpc%2Fsearch.html%3Futm_source%3Dm_cf_cpc_baidu_pc%26m_kw%3Dbaidu_cpc_sz_e110f9_564d23_%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%2B%25E4%25BC%2581%25E4%25B8%259A; X_HTTP_TOKEN=1b7919cd1cbf0b740617066551dfab02284508df64; _gid=GA1.2.625990885.1556607211; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1556607211; LGRID=20190430145241-8c78b30f-6b14-11e9-bdbe-525400f775ce; SEARCH_ID=5584f30f5f10477e92c35f798035a1cc',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    return headers


# def getHeadersInfo():
#     """获取查看详情请求头"""
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
#         'Referer': 'https://www.lagou.com/jobs/list_%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88?labelWords=&fromSearch=true&suginput=',
#         'Cookie': '_ga=GA1.2.2045471023.1548125216; user_trace_token=20190122104637-f04ffaab-1def-11e9-b733-5254005c3644; LGUID=20190122104637-f0500254-1def-11e9-b733-5254005c3644; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22168737437ae434-0c32dacc5e9b33-b781636-2073600-168737437af8d3%22%2C%22%24device_id%22%3A%22168737437ae434-0c32dacc5e9b33-b781636-2073600-168737437af8d3%22%7D; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAAAIAACBIDF3674D1FD941D4E0FC1627B01467751; _gid=GA1.2.2034755479.1557130753; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1556498533,1556607210,1557130749,1557188574; LGSID=20190507082200-2184cce3-705e-11e9-9ec2-5254005c3644; PRE_UTM=m_cf_cpc_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.K600000F3Z4zzZ2Y9fA_1Tv4Qwm5CE5-hHEQXMlBDsM_H179oAt8w0oxZ9UJurwEi-5xJKCUrOpxJdxPCPLvNRaUaYwVr7wyUhp-hZmw8dW1qlZbTq2oQQnBovyo-RaJ1EvrhdALcUlm9S9nxnO8DDUV2MfyBjA3lL2SXFXPYzx-00_RSdy4q-Ppa8L1uIqOgPsXhnp9t0h9JZfAp0.7Y_NR2Ar5Od663rj6tJQrGvKD77h24SU5WudF6ksswGuh9J4qt7jHzk8sHfGmYt_rE-9kstVerQKz33X8M-eXKBqM764mTT5QZstJplePXO-LI5uIb3t8Z1lTr1dsePSZ1LmIMo9qx5j4SrZdSyZxgSo9tS1jlOj9vN3x5_sS81jEqJhGv-5QWdQjPak8vUr5mC.U1Yk0ZDqs2v4_sK9uZ745TaV8Un0mywkIjYz0ZKGm1Yk0Zfqs2v4VnL3FHcskE5iVfKGUHYznWR0u1dsT1c0Iybqmh7GuZR0TA-b5Hf0mv-b5Hb10AdY5HDsnH-xnH0kPdtknjc1g1nsnjFxn1msnfKopHYs0ZFY5HcdP6K-pyfqnWmdnWNxnHfvPdtznHDkPdtzrjTLPNtzrjTzP7tzrjbvP7tzrj61n-tzrjR3PNtzPWndn7tzrjmsndtznWDvn0KBpHYznjwxnHRd0AdW5HDsnj7xrjDkrH61rHcdg17xnH0zg100TgKGujYs0Z7Wpyfqn0KzuLw9u1Ys0A7B5HKxn0K-ThTqn0KsTjY1PH0zrH0sPj00UMus5H08nj0snj0snj00Ugws5H00uAwETjYs0ZFJ5H00uANv5gKW0AuY5H00TA6qn0KET1Ys0AFL5HDs0A4Y5H00TLCq0A71gv-bm1dsTzdMXh410ZwdT1Y3P1fvnWDdn1DdP1RsnWD1nH6d0ZF-TgfqnHRdP1D3rjRkPW6vnfK1pyfqm1uBmHc3PHDsnjDdrH9WnfKWTvYqPHRYwWmzfb7DP1NKnRuDr0K9m1Yk0ZK85H00TydY5H00Tyd15H00XMfqnfKVmdqhThqV5HKxn7tsg1Kxn0Kbmy4dmhNxTAk9Uh-bT1Ysg1Kxn7t1n1mvnHmvg100TA7Ygvu_myTqn0Kbmv-b5H00ugwGujYVnfK9TLKWm1Ys0ZNspy4Wm1Ys0Z7VuWYkP6KhmLNY5H00uMGC5H00uh7Y5H00XMK_Ignqn0K9uAu_myTqnfK_uhnqn0KEIjYs0AqzTZfqnanscznsc10WnansQW0snj0sn0KWThnqPWRYrHc%26word%3D%25E6%258B%2589%25E9%2592%25A9%26ck%3D4015.3.111.152.145.234.186.186%26shh%3Dwww.baidu.com%26sht%3Dbaiduhome_pg%26us%3D1.0.1.0.1.338.0%26bc%3D110101; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flanding-page%2Fpc%2Fsearch.html%3Futm_source%3Dm_cf_cpc_baidu_pc%26m_kw%3Dbaidu_cpc_sz_e110f9_564d23_%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%2B%25E4%25BC%2581%25E4%25B8%259A; SEARCH_ID=7246d7e9fb254d30b3667b84354c93af; X_HTTP_TOKEN=1b7919cd1cbf0b741358817551dfab02284508df64; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1557188585; LGRID=20190507082211-285e74d6-705e-11e9-9ec2-5254005c3644; TG-TRACK-CODE=search_code',
#     }
#     return headers