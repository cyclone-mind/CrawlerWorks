require('./03 env')
require('./04 source')

function get_a_bogus(p) {
    arguments = [
        0,
        1,
        14,
        p,
        // "device_platform=webapp&aid=6383&channel=channel_pc_web&source=6&update_version_code=170400&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1778&screen_height=1000&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=128.0.0.0&browser_online=true&engine_name=Blink&engine_version=128.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=0.4&effective_type=3g&round_trip_time=400&webid=7411527779960964618&verifyFp=verify_m0qs0uu2_tvMESWVm_VTGa_44Vf_AGYj_xOl8saGu2gEd&fp=verify_m0qs0uu2_tvMESWVm_VTGa_44Vf_AGYj_xOl8saGu2gEd&msToken=9YCV8ngYySUiGzwIiaY4O2LSgojlhBEcJCdmBO64QILZTXFmmLUG-jVkWJZO2MB7jd53VW9EJt46DbxtNPA0VWk6yX7UHUWdmiEkfIw8T4Z0NLphowiCBzGtc46if5U%3D&msToken=9YCV8ngYySUiGzwIiaY4O2LSgojlhBEcJCdmBO64QILZTXFmmLUG-jVkWJZO2MB7jd53VW9EJt46DbxtNPA0VWk6yX7UHUWdmiEkfIw8T4Z0NLphowiCBzGtc46if5U%3D",
        "",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
    ]
    var r = window.ce._v;
    return (0,
        window.ce._u)(r[0], arguments, r[1], r[2], this)
}

//  传入参数测试
// u = [
//     0,
//     1,
//     14,
//     "device_platform=webapp&aid=6383&channel=channel_pc_web&source=6&update_version_code=170400&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1778&screen_height=1000&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=128.0.0.0&browser_online=true&engine_name=Blink&engine_version=128.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=0.4&effective_type=3g&round_trip_time=400&webid=7411527779960964618&verifyFp=verify_m0qs0uu2_tvMESWVm_VTGa_44Vf_AGYj_xOl8saGu2gEd&fp=verify_m0qs0uu2_tvMESWVm_VTGa_44Vf_AGYj_xOl8saGu2gEd&msToken=9YCV8ngYySUiGzwIiaY4O2LSgojlhBEcJCdmBO64QILZTXFmmLUG-jVkWJZO2MB7jd53VW9EJt46DbxtNPA0VWk6yX7UHUWdmiEkfIw8T4Z0NLphowiCBzGtc46if5U%3D&msToken=9YCV8ngYySUiGzwIiaY4O2LSgojlhBEcJCdmBO64QILZTXFmmLUG-jVkWJZO2MB7jd53VW9EJt46DbxtNPA0VWk6yX7UHUWdmiEkfIw8T4Z0NLphowiCBzGtc46if5U%3D",
//     "",
//     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
// ]

// p = "device_platform=webapp&aid=6383&channel=channel_pc_web&source=6&update_version_code=170400&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1778&screen_height=1000&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=128.0.0.0&browser_online=true&engine_name=Blink&engine_version=128.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=0.4&effective_type=3g&round_trip_time=400&webid=7411527779960964618&verifyFp=verify_m0qs0uu2_tvMESWVm_VTGa_44Vf_AGYj_xOl8saGu2gEd&fp=verify_m0qs0uu2_tvMESWVm_VTGa_44Vf_AGYj_xOl8saGu2gEd&msToken=9YCV8ngYySUiGzwIiaY4O2LSgojlhBEcJCdmBO64QILZTXFmmLUG-jVkWJZO2MB7jd53VW9EJt46DbxtNPA0VWk6yX7UHUWdmiEkfIw8T4Z0NLphowiCBzGtc46if5U%3D&msToken=9YCV8ngYySUiGzwIiaY4O2LSgojlhBEcJCdmBO64QILZTXFmmLUG-jVkWJZO2MB7jd53VW9EJt46DbxtNPA0VWk6yX7UHUWdmiEkfIw8T4Z0NLphowiCBzGtc46if5U%3D",
// console.log(get_a_bogus(p))
