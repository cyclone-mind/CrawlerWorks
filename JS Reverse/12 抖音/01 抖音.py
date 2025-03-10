# -*- coding: utf-8 -*-
import requests
import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs
import urllib.parse

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cookie': '__live_version__=%221.1.1.4094%22; xgplayer_user_id=953050919486; __ac_nonce=066db094d00d58de97cf0; __ac_signature=_02B4Z6wo00f01t7GzSQAAIDD8EEADOF5Bgbe5smAANF3gydQaEpOHLMA1m5Gz3WAzuM3qiWuBr.B4SJ8KJmv4a5pF-c29WRP6tGux51bRnpAXT1XqCx0NtQ-We-dWmEbLvkl-CsYlZd2lXGXcf; ttwid=1%7CH_jFEQG8ZKVHRe0Ysod6-NE-xKiWydK3R2BBBMGDLSA%7C1725630798%7C3436666e77f8225d9e6141f313386bdc6eefe155aaa0fd892ebf38108b66a51b; UIFID_TEMP=1ee16134db40129a5ff28e6a352dddaa8524f48fc5e4ea6d697d6a182d7836e426bd9e8d6419ef6c7c34189132bda899757af359f448f367a64936629848f9bd33fc1a19b1dac611dd8d5a8eac276b3d; douyin.com; device_web_cpu_core=16; device_web_memory_size=8; architecture=amd64; hevc_supported=true; dy_swidth=1778; dy_sheight=1000; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1778%2C%5C%22screen_height%5C%22%3A1000%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A16%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A0.4%2C%5C%22effective_type%5C%22%3A%5C%223g%5C%22%2C%5C%22round_trip_time%5C%22%3A450%7D%22; csrf_session_id=4d69e632d1ec575ea0fcd633ca159d0b; fpk1=U2FsdGVkX1/MM2KOT2nFAh4WjugK996NCRqfwPQKGiFLDucJuknbHS+JGtZVdMZ3n+O6qvpx9lDx21WVwC9P/w==; fpk2=e8db1a910ee088b469ecfd2b6a9b9da5; s_v_web_id=verify_m0qs0uu2_tvMESWVm_VTGa_44Vf_AGYj_xOl8saGu2gEd; strategyABtestKey=%221725630800.454%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.129%7D; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; passport_csrf_token=885aa3ea1eb849d90a55bcd5431810c4; passport_csrf_token_default=885aa3ea1eb849d90a55bcd5431810c4; bd_ticket_guard_client_web_domain=2; UIFID=1ee16134db40129a5ff28e6a352dddaa8524f48fc5e4ea6d697d6a182d7836e45e495ef0f0aeacb5dfa3d0c5ce964f0cbb4479a3c4c7ac2c7aa4da9a57ac5ec27856a8349536de6176cd742910887d392042e8b44de7a0bdbc733e5e314761eed88cfafd0574d047395cc525106a1f416b304c17e72704e4a40996a5aad03e39cc4bcce278c399ce8560483d463fff9efe03a15dab751cf1d53033ceae58b5e3; odin_tt=e67868fed14d7861c8127a5f0063296e9a22a57b5a2c138044695cacd0a7b1710587f38cf3696743c11362cdd3f5cec4b9c2d68cdc1695f64b282b9e9f6e6f20a5490509adf346a36beb0c74ab63617d; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCUHo1NG9HOWdybFkxYVhMZENVa1BpN2xiQVNFOVZZMncwMllUT0RPdEJDK2FJaHJvQTF0TzFuelE2Mi9hVFFRb0ZIalFOMXZDL2xTYWpaSVdZaXg5b2c9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; biz_trace_id=689680da; download_guide=%222%2F20240906%2F0%22; IsDouyinActive=true; home_can_add_dy_2_desktop=%220%22',
    'priority': 'u=1, i',
    'referer': 'https://www.douyin.com/user/MS4wLjABAAAAQERLUS1XLl1qZMZDkibRWUdHGBAoG0pJq_5hAj3XjIZXnxgtW_CcE17nuHHfikpQ?from_tab_name=main',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}

params = {
    'device_platform': 'webapp',
    'aid': '6383',
    'channel': 'channel_pc_web',
    'sec_user_id': 'MS4wLjABAAAAQERLUS1XLl1qZMZDkibRWUdHGBAoG0pJq_5hAj3XjIZXnxgtW_CcE17nuHHfikpQ',
    'max_cursor': '0',
    'locate_query': 'false',
    'show_live_replay_strategy': '1',
    'need_time_list': '1',
    'time_list_query': '0',
    'whale_cut_token': '',
    'cut_version': '1',
    'count': '18',
    'publish_video_strategy_type': '2',
    'update_version_code': '170400',
    'pc_client_type': '1',
    'version_code': '290100',
    'version_name': '29.1.0',
    'cookie_enabled': 'true',
    'screen_width': '1778',
    'screen_height': '1000',
    'browser_language': 'zh-CN',
    'browser_platform': 'Win32',
    'browser_name': 'Chrome',
    'browser_version': '128.0.0.0',
    'browser_online': 'true',
    'engine_name': 'Blink',
    'engine_version': '128.0.0.0',
    'os_name': 'Windows',
    'os_version': '10',
    'cpu_core_num': '16',
    'device_memory': '8',
    'platform': 'PC',
    'downlink': '0.4',
    'effective_type': '3g',
    'round_trip_time': '450',
    'webid': '7411527779960964618',
    'msToken': 'rhUqfMWpdnNVZZLkInjea_A0aSkcaUlbgD7oYo9zBZY5J7ZvISNzUilRi_BqHEU6l9NvLAAoAIx5hkQfLZ_Szw6txDF_yXbQoKmqSTt-bVnMlZLGk_qo5OXI3H4g0w==',
    # 'a_bogus': 'm680QmghDkdpkD6v56/LfY3q6AF3YMlK0trEMD2f-d3jg639HMP09exo684v96EjN4/kIeEjy4hbTr9QrQIH81wf9SUO/2CZmg00t-P2so0j53inCgDDE0hN-kb3SFq0RXNAEOv0y75SKms0A2nHmhK4bfebY7Y6i6trdE==',
    'verifyFp': 'verify_m0qs0uu2_tvMESWVm_VTGa_44Vf_AGYj_xOl8saGu2gEd',
    'fp': 'verify_m0qs0uu2_tvMESWVm_VTGa_44Vf_AGYj_xOl8saGu2gEd',
}

params_str = urllib.parse.urlencode(params)
# print('params_str:::', params_str)
a_bogus = execjs.compile(open('./02 抖音.js').read()).call('get_a_bogus', params_str)
# print('a_bogus:::', a_bogus)
params['a_bogus'] = a_bogus

response = requests.get('https://www.douyin.com/aweme/v1/web/aweme/post/', params=params, headers=headers)
print(response.text)
