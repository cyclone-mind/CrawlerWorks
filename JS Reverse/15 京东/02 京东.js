require('./04 env')
require('./03 source')

/*
params  = '{
    "appid": "search-pc-java",
    "functionId": "pc_search_s_new",
    "client": "pc",
    "clientVersion": "1.0.0",
    "t": 1726125527758,
    "body": "a2ef7b0a6e02612dbfa8a48e53e46497b5a6452c123f8bf6b51a9c7adafc5bf3"
}'


 window.PSign.sign(params ).then(function(res){
     console.log('res.h5st:::',res.h5st)
     process.exit()
 })
 */

let jsonData = __process.argv[2]

params = JSON.parse(jsonData)
 window.PSign.sign(params).then(function(res){
     console.log(':::'+res.h5st+':::')
     process.exit()
 })



