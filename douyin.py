# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2019/1/16 8:37'

import json
import requests

headers = {
    'User-Agent': 'com.ss.android.ugc.aweme/420 (Linux; U; Android 7.0; zh_CN; HUAWEI CAZ-AL10; Build/HUAWEICAZ-AL10; Cronet/58.0.2991.0)'
}

cookies = {
    'sid_guard': '68ad6b414994f414240d6e2af4586e01%7C1547560681%7C5184000%7CSat%2C+16-Mar-2019+13%3A58%3A01+GMT',
    'uid_tt': '792a29ee869e17cf017c793512bbee82',
    'sid_tt': '68ad6b414994f414240d6e2af4586e01',
    'sessionid': '68ad6b414994f414240d6e2af4586e01',
    'odin_tt': '416e34366c5756556c616d504776684493987a9f0fd3c9d0a637c19ae22af02238e0bf723c19eb09a78a34cd3c452a546c01ccbd8935f41f43417a16b7696418',
    'install_id': '57735775743',
    'ttreq': '1$28b3ec761c4f8d29e8e1b9df0b188e049e674c5e',
    'qh[360]': '1'
}

s = requests.session()
for i in range(50):
    douyin = s.get(
        'https://api-eagle.amemv.com/aweme/v1/user/?user_id=6556303280&retry_type=no_retry&iid=57735775743&device_id=40079516756&ac=wifi&channel=gdt_growth14_ys5&aid=1128&app_name=aweme&version_code=179&version_name=1.7.9&device_platform=android&ssmix=a&device_type=HUAWEI+CAZ-AL10&device_brand=HUAWEI&language=zh&os_api=24&os_version=7.0&openudid=17eb6ec21a6e433&manifest_version_code=179&resolution=1080*1788&dpi=480&update_version_code=1790&_rticket=1547598735649&ts=1547598736&as=a1853783d0996cab8e1426&cp=7d9ec85204ed3fbfe1leux&mas=0058522e2abca9f6c908a112733756f52e6c4c2c8ca61c4686c66c',
        cookies=cookies, headers=headers)
    douyin1 = s.get(
        'https://api.amemv.com//aweme/v1/aweme/post/?user_id=6556303280&max_cursor=0&count=20&retry_type=no_retry&iid=57735775743&device_id=40079516756&ac=wifi&channel=gdt_growth14_ys5&aid=1128&app_name=aweme&version_code=179&version_name=1.7.9&device_platform=android&ssmix=a&device_type=HUAWEI+CAZ-AL10&device_brand=HUAWEI&language=zh&os_api=24&os_version=7.0&openudid=17eb6ec21a6e433&manifest_version_code=179&resolution=1080*1788&dpi=480&update_version_code=1790&_rticket=1547599438570&ts=1547599439&as=a1853733bf540c0e9e3929&cp=754ec455feef31e6e1prcd&mas=006010f82cb00bbec9c1f30703ec7a8a6e9c4c9ccca69ca60cc60c',
        cookies=cookies, headers=headers)
    douyin2 = s.get(
        'https://api.amemv.com/aweme/v1/aweme/post/?user_id=6556303280&max_cursor=1546513537000&count=10&retry_type=no_retry&iid=57735775743&device_id=40079516756&ac=wifi&channel=gdt_growth14_ys5&aid=1128&app_name=aweme&version_code=179&version_name=1.7.9&device_platform=android&ssmix=a&device_type=HUAWEI+CAZ-AL10&device_brand=HUAWEI&language=zh&os_api=24&os_version=7.0&openudid=17eb6ec21a6e433&manifest_version_code=179&resolution=1080*1788&dpi=480&update_version_code=1790&_rticket=1547604858737&ts=1547604859&as=a1b589c37b672ce3ce6763&cp=9a7cca5ebee73f3ce1qsys&mas=00579eaaf911f5b0c29417c035f33b411ecc6cec6ca6c6cca6c64c',
        headers=headers
    )
content = douyin2.text
print(content)
pass
