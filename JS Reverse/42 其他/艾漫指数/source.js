Kt = {
    showLoading(e="Loading") {
        ic = ic + 1,
        !(ic <= 0) && cn.loading({
            forbidClick: !0,
            overlayClass: "custom-van-toast",
            message: "\u52A0\u8F7D\u4E2D..."
        })
    },
    hideLoading() {
        setTimeout( () => {
            ic = ic - 1,
            ic <= 0 && cn.clear()
        }
        , 500)
    },
    generateQR: async (e, t) => {
        try {
            var n = {
                errorCorrectionLevel: "H",
                type: "image/jpeg",
                rendererOpts: {
                    quality: .3
                }
            };
            await Ku.toDataURL(e, n, function(r, i) {
                if (r)
                    throw r;
                var a = document.getElementById(t);
                a.src = i
            })
        } catch (r) {
            console.error(r)
        }
    }
    ,
    getScrollTop() {
        return document.body.scrollTop || document.documentElement.scrollTop
    },
    setScrollTop(e) {
        document.body.scrollTop = e,
        document.documentElement.scrollTop = e
    },
    formatParams: function(e) {
        var t = [];
        for (var n in e)
            if (e.hasOwnProperty(n)) {
                var r = e[n];
                t.push(n + "=" + r)
            }
        return t.join("&")
    },
    isInArray: function(e, t) {
        var n = e.indexOf(t);
        return n
    },
    padLeft: function(e, t, n) {
        var r = (e + "").split("");
        if (r.length >= t)
            return e;
        for (var i = t - r.length, a = "", s = 0; s < i; s++)
            a = a + n;
        return a = a + e,
        a
    },
    formatStrToTime: function(e, t) {
        if (!e)
            return "";
        t && e.indexOf(":") >= 0 && t && e.indexOf("-") < 0 && (e = t + " " + e),
        e = e.replace(/-/gi, "/");
        var n = new Date(e)
          , r = n.getFullYear()
          , i = Kt.padLeft(n.getMonth() + 1, 2, "0")
          , a = Kt.padLeft(n.getDate(), 2, "0")
          , s = Kt.padLeft(n.getHours(), 2, "0")
          , c = Kt.padLeft(n.getMinutes(), 2, "0")
          , u = r + "\u5E74" + i + "\u6708" + a + "\u65E5" + s + ":" + c;
        return u
    },
    formatStrToEndDate: function(e, t) {
        return e ? (t && e.indexOf(":") >= 0 && t && e.indexOf("-") >= 0 || (t && e.indexOf(":") >= 0 ? e = t + " " + e : e.split(" ").length <= 1 && (e = e + " 23:59")),
        Kt.formatStrToTime(e)) : ""
    },
    formatStrToDay: function(e) {
        return e ? dayjs(e).format("YYYY\u5E74MM\u6708DD\u65E5") : ""
    },
    checkPhone(e) {
        return !!/^[0-9a-zA-Z]{11}$/.test(e)
    },
    getSign(e) {
        delete e.sign;
        for (var t = [], n = Object.keys(e).sort(), r = 0; r < n.length; r++) {
            var i = n[r]
              , a = e[i];
            t.push(i),
            t.push(a)
        }
        t.push("iIndex");
        var s = t.join("_")
          , c = hae(s);
        return c
    },
    checkRequireLogin(e, t) {
        var r = __iIndexApp__.config.globalProperties.$store.state.maxDate
          , i = null;
        r ? i = new Date(r) : i = new Date;
        var a = i.getFullYear() + "/" + (i.getMonth() + 1) + "/" + i.getDate() + " 23:59:59"
          , s = 7 * 24 * 60 * 60 * 1e3
          , c = new Date(a).getTime() - s;
        t = t.replace(/-/gi, "/");
        var u = new Date(t + " 23:59:59").getTime()
          , A = !e && u <= c;
        return A
    },
    checkRequireLoginForRelativeDate(e, t) {
        var n = {
            \u4E0A\u6620\u65E5: 1,
            \u5F00\u64AD\u65E5: 1,
            \u9996\u64AD\u65E5: 1,
            \u4E0A\u6620\u5468: 1,
            \u5F00\u64AD\u5468: 1,
            \u9996\u64AD\u5468: 1
        }
          , r = t.relativeDate || t
          , i = !e && n[r] != 1;
        return i
    },
    numberFormat(e, t, n, r, i) {
        e = (e + "").replace(/[^0-9+-Ee.]/g, ""),
        i = i || "ceil";
        var a = isFinite(+e) ? +e : 0
          , s = isFinite(+t) ? Math.abs(t) : 0
          , c = typeof r == "undefined" ? "," : r
          , u = typeof n == "undefined" ? "." : n
          , A = ""
          , f = function(h, b) {
            var w = h.toString()
              , I = w.split(".")
              , p = 0;
            try {
                p += I[1].length
            } catch {}
            return b > p ? w : (I[1] = Math[i](Number(I[1]) / Math.pow(10, p - b)),
            I.join("."))
        };
        A = (s ? f(a, s) : "" + Math.floor(a)).split(".");
        for (var g = /(-?\d+)(\d{3})/; g.test(A[0]); )
            A[0] = A[0].replace(g, "$1" + c + "$2");
        return (A[1] || "").length < s && (A[1] = A[1] || "",
        A[1] += new Array(s - A[1].length + 1).join("0")),
        A.join(u)
    },
    formatThousand(e) {
        if (e == null)
            return "-";
        let t = e + "";
        if (t.trim() == "")
            return "-";
        let r = t.split(".").length > 1 ? 2 : 0;
        return td.formatNumber(e, r, ",")
    },
    formatThousandWithWanAndYi(e, t) {
        if (t = t || 2,
        e == null)
            return "-";
        let n = e + "";
        if (n.trim() == "")
            return "-";
        let i = n.split(".")[0];
        if (i.length < 5)
            return td.formatNumber(e, t);
        if (i.length >= 5 && i.length < 9) {
            let a = e / 1e4;
            return td.formatNumber(a, t) + "\u4E07"
        }
        if (i.length >= 9) {
            let a = Number(e / 1e8);
            return td.formatNumber(a, t) + "\u4EBF"
        }
    },
    filterDateType(e) {
        return bt.INTERVAL_TYPE.filter(function(t) {
            return t.type <= 3
        })
    },
    showEndDay(e, t) {
        if (!e || !t)
            return e || "";
        var n = e.replace(/-/gi, "/")
          , r = t.replace(/-/gi, "/");
        return new Date(n).getTime() > new Date(r).getTime() ? t : e
    },
    dataFilter(e, t) {
        var n = e
          , r = n.data;
        if (n.isEncrypt === 1) {
            var i = _m.parse(n.lastFetchTime + "000")
              , a = _m.parse(n.lastFetchTime + "000")
              , s = pae.decrypt(r.toString(), i, {
                iv: a
            })
              , c = s.toString(_m);
            return n.data = JSON.parse(c),
            n
        } else
            return n.isEncrypt === 0 && typeof r == "string" ? (n.data = JSON.parse(r),
            n) : e
    },
    startWXoauth({optionalId: e, picNum: t, currentPrice: n, originPrice: r, maskType: i, objectType: a, toUrl: s, goodsNum: c}) {
        const u = "wx4434b1d45e2d35ef"
          , A = "https://open.weixin.qq.com/connect/oauth2/authorize"
          , f = __iIndexApp__.$route.params
          , g = encodeURIComponent(yfe() + "/paywxok/" + a)
          , h = "code"
          , b = "snsapi_userinfo"
          , w = f.id
          , I = f.name
          , p = `${w}|${I}|${e}|${n}|${r}|${i}|${t}|${encodeURIComponent(s)}|${c}`
          , y = A + "?appid=" + u + "&redirect_uri=" + g + "&response_type=" + h + "&scope=" + b + "&state=" + p + "#wechat_redirect";
        window.location.replace(y)
    },
    startWXoauth2(e, t, n, r, i, a, s) {
        const c = "wx4434b1d45e2d35ef"
          , u = "https://open.weixin.qq.com/connect/oauth2/authorize"
          , A = encodeURIComponent(window.location.protocol + "//" + window.location.host + "/paywxok2/" + i)
          , f = "code"
          , g = "snsapi_userinfo"
          , h = a + "|" + i + "|" + e + "|" + t + "|" + n + "|" + r + "|" + s
          , b = u + "?appid=" + c + "&redirect_uri=" + A + "&response_type=" + f + "&scope=" + g + "&state=" + h + "#wechat_redirect";
        window.location.replace(b)
    },
    firstUrl: "",
    getWXConfig(e, t, n, r) {
        e = `${bt.document_title}${e ? " - " + e : ""}`;
        let i = Kt.isWeixin()
          , a = Kt.isIos();
        if (!i) {
            cn.clear(),
            typeof setShareInfo == "object" && setShareInfo({
                title: e,
                summary: "\u7F51\u7EDC\u8131\u6C34\u5A31\u4E50\u6307\u6570\u5E73\u53F0",
                pic: t,
                url: r || window.location.href.split("#")[0]
            });
            return
        }
        let s = escape(window.location.href.split("#")[0]);
        Kt.firstUrl || (Kt.firstUrl = s),
        __iIndexApp__.config.globalProperties.$store.dispatch("getWxToken", {
            shareUrl: a ? Kt.firstUrl : s
        }).then(function(u) {
            cn.clear();
            const A = _.get(u, "data");
            !A || Kt.initWXConfig(A, e, t, n, r)
        }).catch( () => {
            cn.clear()
        }
        )
    },
    initWXConfig(e, t, n, r, i) {
        let a = {
            title: t,
            imgUrl: n,
            desc: "\u7F51\u7EDC\u8131\u6C34\u5A31\u4E50\u6307\u6570\u5E73\u53F0",
            link: i || window.location.href.split("#")[0],
            success: function() {
                cn("\u5206\u4EAB\u6210\u529F\uFF01")
            },
            cancel: function() {}
        };
        wx.config({
            debug: !1,
            signature: e.signature,
            nonceStr: e.noncestr,
            timestamp: e.timestamp,
            appId: Afe,
            jsApiList: ["onMenuShareTimeline", "onMenuShareAppMessage", "onMenuShareQQ", "onMenuShareWeibo", "onMenuShareQZone"],
            openTagList: ["wx-open-launch-weapp"]
        }),
        wx.ready(function() {
            wx.onMenuShareTimeline(a),
            wx.onMenuShareAppMessage(a),
            wx.onMenuShareQQ(a),
            wx.onMenuShareWeibo(a),
            wx.onMenuShareQZone(a)
        })
    },
    isIos() {
        var e = navigator.userAgent
          , t = !!e.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/);
        return t
    },
    isAndroid() {
        var e = navigator.userAgent
          , t = e.indexOf("Android") > -1 || e.indexOf("Linux") > -1;
        return t
    },
    isWeixin() {
        var e = window.navigator.userAgent.toLowerCase();
        return e.match(/MicroMessenger/i) == "micromessenger"
    },
    isWeibo() {
        var e = window.navigator.userAgent.toLowerCase();
        return e.match(/Weibo/i) == "weibo"
    },
    getScenePage(e, t) {
        if (e) {
            if (t == 1)
                return 2;
            if (t == 2)
                return 4;
            if (t == 3)
                return 6;
            if (t == 4)
                return 8
        } else {
            if (t == 0)
                return 100;
            if (t == 1)
                return 1;
            if (t == 2)
                return 3;
            if (t == 3)
                return 5;
            if (t == 4)
                return 7
        }
    },
    clearPayKey() {
        window.localStorage.removeItem("pay_orderId"),
        window.localStorage.removeItem("pay_service_index")
    },
    getProvince(e, t) {
        for (let n = 0; n < e.provinces.length; n++) {
            const r = e.provinces[n];
            for (let i = 0; i < r.length; i++)
                if (r[i].key == t)
                    return r[i]
        }
    },
    getAreaIndex(e, t) {
        for (let n = 0; n < e.provinces.length; n++) {
            const r = e.provinces[n];
            for (let i = 0; i < r.length; i++)
                if (r[i].key == t)
                    return n
        }
    },
    getIndexFromFilterOPtions(e, t) {
        if (e == 0) {
            let n = bt.filterOPtions[e].provinces;
            for (let r = 0; r < n.length; r++)
                for (let i = 0; i < n[r].length; i++) {
                    const a = n[r][i];
                    if (a.key == t)
                        return a.key
                }
        } else {
            let n = bt.filterOPtions[e].options;
            for (let r = 0; r < n.length; r++)
                if (n[r].key == t)
                    return r
        }
    },
    sendLogByVTracking(e, t) {
        const n = Object.assign({
            isHideLoading: !0,
            funID: e
        }, t);
        if (n.url) {
            const r = window.location;
            n.url = `${r.protocol}//${r.host}${n.url}`
        }
        e && fe("logRecord", n)
    },
    showPlayNum(e) {
        return dayjs(e).isValid() ? dayjs(e).isBefore("2019-01-01") : !1
    },
    showPlayEndDate(e) {
        return dayjs(e).isValid() ? dayjs(e).isSameOrAfter("2019-01-01") ? "2018-12-31" : e : ""
    },
    defaultAvatar(e) {
        return e || Qd
    },
    filterImgForSave(e, t=7) {
        let n = Qd;
        if (t == 4 ? n = qN : t == 5 ? n = rU : t == 680 && (n = iU),
        !e || !e.trim())
            return n;
        if (!e)
            return "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7";
        const r = window.location.protocol + "//" + window.location.host + "/";
        return e.replace("https://istar.aiman.cn/", r).replace("https://pic3.imzs.com/", r).replace("http://pic3.imzs.com/", r)
    },
    filterImgForSaveTranslate(e) {
        if (!e)
            return "";
        const t = window.location.protocol + "//" + window.location.host + "/";
        return e.replace("https://istar.aiman.cn/", t).replace("https://pic3.imzs.com/", t).replace("http://pic3.imzs.com/", t)
    },
    getGenderLabel(e) {
        for (let t = 0; t < tT.length; t++) {
            const n = tT[t];
            if (n.value == e)
                return n.text
        }
        return ""
    }
};