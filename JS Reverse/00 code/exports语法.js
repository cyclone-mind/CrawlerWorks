/*### 【6】导入模块

当涉及到实际案例时，我将给出一个常见的示例，以说明如何在 JavaScript 中使用 `require` 或 `import` 导入模块。

假设我们有两个文件：`math.js` 和 `main.js`。

首先，让我们创建 `math.js` 文件，它包含一个简单的数学函数：*/

```js
// math.js
const add = (a, b) => {
  return a + b;
};

const multiply = (a, b) => {
  return a * b;
};

module.exports = {
  add,
  multiply
};
```

/*在 `math.js` 中，我们定义了两个函数 `add` 和 `multiply`，并使用 `module.exports` 导出这些函数，使其可以在其他文件中使用。

接下来，我们创建 `main.js` 文件，它将使用 `math.js` 中的函数：

使用 `require`（CommonJS 模块系统）的示例：*/

```js
// main.js
const math = require('./math');

console.log(math.add(2, 3)); // 输出：5
console.log(math.multiply(2, 3)); // 输出：6
```

/*在这个示例中，我们使用 `require` 函数将 `math.js` 文件导入到 `main.js` 文件中。`require('./math')` 表示我们导入与 `main.js` 文件相同目录下的 `math.js` 文件。

然后，我们可以使用 `math.add()` 和 `math.multiply()` 调用 `math.js` 中导出的函数。

使用 `import`（ES 模块系统）的示例：*/

```js
function add(a, b) {
    return a + b;
}

function multiply(a, b) {
    return a * b;
}

export default {
    add: add,
    multiply: multiply,
}
```

```js
// main.js
import cal from './cal.js'

console.log(cal.add(1,2))
console.log(cal.multiply(1,2))
```

```html
 <script type="module" src="main.js"></script>
```