require('./03 env')
require('./04 source')


// let i = {
//     "cursor_score": "",
//     "num": 31,
//     "refresh_type": 1,
//     "note_index": 27,
//     "unread_begin_note_id": "",
//     "unread_end_note_id": "",
//     "unread_note_count": 0,
//     "category": "homefeed.cosmetics_v3",
//     "search_key": "",
//     "need_num": 6,
//     "image_formats": [
//         "jpg",
//         "webp",
//         "avif"
//     ],
//     "need_filter_image": false
// }

function get_headers(i) {
    let c = '/api/sns/web/v1/homefeed'
    return window._webmsxyw(c, i)
}

// console.log(get_headers(c, i))