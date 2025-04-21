import hashlib
obj = hashlib.md5()
obj.update("actual_played_time=0&aid=115328327621553&appkey=1d8b6e7d45233436&auto_play=0&build=6240300&c_locale=zh_CN&channel=xxl_gdt_wm_253&cid=32884919960&epid=0&epid_status=&from=7&from_spmid=tm.recommend.0.0&last_play_progress_time=0&list_play_time=0&max_play_progress_time=0&mid=0&miniplayer_play_time=0&mobi_app=android&network_type=1&paused_time=0&platform=android&play_status=0&play_type=1&played_time=0&quality=32&s_locale=zh_CN&session=418de6ea56d84d3d2b4ceb64b7be224fe2ed4353&sid=0&spmid=main.ugc-video-detail.0.0&start_ts=0&statistics=%7B%22appId%22%3A1%2C%22platform%22%3A3%2C%22version%22%3A%226.24.0%22%2C%22abtest%22%3A%22%22%7D&sub_type=0&total_time=0&ts=1763129581&type=3&user_status=0&video_duration=204".encode('utf-8'))
obj.update("560c52cc".encode('utf-8'))
obj.update("d288fed0".encode('utf-8'))
obj.update("45859ed1".encode('utf-8'))
obj.update("8bffd973".encode('utf-8'))
res = obj.hexdigest()
print(res)

# 抓包的sign:  a4f893e272c4563742fb258f7dc2f1e6
# 我们执行得到： a4f893e272c4563742fb258f7dc2f1e6