crypto = require("crypto")
a = function() {
	return crypto.randomUUID ? crypto.randomUUID() : (new Date).getTime()
}
console.log(a())