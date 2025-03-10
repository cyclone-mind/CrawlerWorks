require("./03 loader.js")

let d = {
    encode: function (m, w) {
        if (!w)
            w = commonjsGlobal.i2.Writer.create()
        if (m.policyType != null && Object.hasOwnProperty.call(m, "policyType"))
            w.uint32(10).string(m.policyType)
        if (m.centralId != null && Object.hasOwnProperty.call(m, "centralId"))
            w.uint32(18).string(m.centralId)
        if (m.province != null && Object.hasOwnProperty.call(m, "province"))
            w.uint32(26).string(m.province)
        if (m.city != null && Object.hasOwnProperty.call(m, "city"))
            w.uint32(34).string(m.city)
        if (m.downtown != null && Object.hasOwnProperty.call(m, "downtown"))
            w.uint32(42).string(m.downtown)
        if (m.garden != null && Object.hasOwnProperty.call(m, "garden"))
            w.uint32(50).string(m.garden)
        if (m.sort != null && Object.hasOwnProperty.call(m, "sort"))
            w.uint32(56).uint32(m.sort)
        if (m.pageNum != null && Object.hasOwnProperty.call(m, "pageNum"))
            w.uint32(64).uint32(m.pageNum)
        if (m.pageSize != null && Object.hasOwnProperty.call(m, "pageSize"))
            w.uint32(72).uint32(m.pageSize)
        if (m.homePageFlag != null && Object.hasOwnProperty.call(m, "homePageFlag"))
            w.uint32(80).uint32(m.homePageFlag)
        return w
    }
}


function get_data(pageNum, policyType) {
    let a = {
        data: {
            centralId: "",
            city: "",
            downtown: "",
            garden: "",
            homePageFlag: 1,
            pageNum: pageNum,
            pageSize: 7,
            policyType: String(policyType),
            province: "",
            sort: 0,
        }
    }
    a["data"] = d["encode"](a["data"])["finish"]()['slice']()
    return a["data"]
}

console.log(get_data())