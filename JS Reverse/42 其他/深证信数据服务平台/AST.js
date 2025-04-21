// 该代码同全国招标公告反混通用。解混淆只是为了能清晰的了解加密逻辑，可以压缩后替换到浏览器中，方便查看加密逻辑。最终解密还是需要扣 JS
// 特征：OB混淆、解密函数的引用链（分为三次：第一次收集所有作用域信息、第二次追踪所有变量的引用、第三次追踪函数调用）
// 特征：字符串还原、字符串拼接、控制流、表达式计算、解编码、删除未引用的变量

// 引入必要的babel解析和转换工具
const parse = require('@babel/parser').parse  // 用于将JS代码解析为AST
const generator = require('@babel/generator').default;  // 用于将AST转换回JS代码
const traverse = require('@babel/traverse').default;  // 用于遍历和修改AST
const types = require('@babel/types')  // 用于创建AST节点
const fs = require('fs')  // 文件系统操作

// 读取待反混淆的JS文件
let jsCode = fs.readFileSync('./encode.js', { encoding: 'utf-8' })

// 将JS代码解析为AST
let ast = parse(jsCode);

//////////////////
// 递归解密函数的引用，添加到数组中
let startFuncName = '_0x1181';  // 起始解密函数名
let decodeFuncArr = [];  // 存储解密函数引用链的数组
let scopeRedefinesU = {};  // 存储作用域中U函数重定义情况的对象

// 第一次遍历: 收集所有作用域信息
traverse(ast, {
    VariableDeclarator(path) {
        // 获取当前变量声明所在的作用域名称
        let scopeName = 'global';  // 默认为全局作用域
        let currentPath = path;
        while (currentPath.parentPath) {
            if (currentPath.parentPath.isFunctionDeclaration()) {
                scopeName = currentPath.parentPath.get('id').node.name;
                break;
            }
            currentPath = currentPath.parentPath;
        }

        // 初始化作用域信息
        if (!scopeRedefinesU[scopeName]) {
            scopeRedefinesU[scopeName] = false;
        }

        // 检查是否重定义了U函数
        // 只有在非全局作用域中才可能"重定义"U
        if (path.get('id').isIdentifier() &&
            path.get('id').node.name === startFuncName &&
            scopeName !== 'global') {
            scopeRedefinesU[scopeName] = true;
            console.log(`在作用域 ${scopeName} 中重定义了U`);
        }
    }
});

console.log('作用域重定义情况:', scopeRedefinesU);

// 添加起始解密函数到追踪数组
decodeFuncArr.push({
    name: startFuncName,
    scope: 'global'
});

// 第二次遍历: 追踪所有变量的引用
traverse(ast, {
    VariableDeclarator(path) {
        // 检查是否是变量声明且初始值为标识符
        if (
            path.get('id').isIdentifier() &&
            path.get('init').isIdentifier()
        ) {
            const idName = path.get('id').node.name;  // 声明的变量名
            const initName = path.get('init').node.name;  // 初始值变量名

            // 获取当前作用域名称
            let scopeName = 'global';
            let currentPath = path;
            while (currentPath.parentPath) {
                if (currentPath.parentPath.isFunctionDeclaration()) {
                    scopeName = currentPath.parentPath.get('id').node.name;
                    break;
                }
                currentPath = currentPath.parentPath;
            }

            console.log(`检查变量: ${idName} = ${initName} 在作用域 ${scopeName}`);

            // 如果当前作用域重定义了U，直接跳过
            if (scopeRedefinesU[scopeName]) {
                console.log(`  跳过: 作用域 ${scopeName} 重定义了U`);
                return;
            }

            // 检查是否引用了我们已经追踪的变量
            const isReferencing = decodeFuncArr.some(item =>
                item.name === initName &&
                (item.scope === 'global' || item.scope === scopeName)
            );

            console.log(`  是否引用追踪变量: ${isReferencing}`);

            // 如果引用了已追踪的变量，则加入追踪列表
            if (isReferencing) {
                // 检查是否已经存在
                const exists = decodeFuncArr.some(item =>
                    item.name === idName && item.scope === scopeName
                );

                if (!exists) {
                    console.log(`  添加到追踪列表: ${idName} 在作用域 ${scopeName}`);
                    decodeFuncArr.push({
                        name: idName,
                        scope: scopeName
                    });
                }
            }
        }
    }
});

// 第三次遍历: 追踪函数调用
const callExpressions = [];  // 存储函数调用表达式
traverse(ast, {
    CallExpression(path) {
        if (path.get('callee').isIdentifier()) {
            const calleeName = path.get('callee').node.name;

            // 获取当前作用域名称
            let scopeName = 'global';
            let currentPath = path;
            while (currentPath.parentPath) {
                if (currentPath.parentPath.isFunctionDeclaration()) {
                    scopeName = currentPath.parentPath.get('id').node.name;
                    break;
                }
                currentPath = currentPath.parentPath;
            }

            // 如果当前作用域重定义了U，直接跳过
            if (scopeRedefinesU[scopeName]) {
                return;
            }

            // 检查是否调用了已追踪的变量
            const isCalling = decodeFuncArr.some(item =>
                item.name === calleeName &&
                item.scope === scopeName
            );

            if (isCalling) {
                callExpressions.push(`函数调用: ${calleeName}() 在作用域 ${scopeName} 中`);
            }
        }
    }
});

// 输出结果
console.log('\n======= 结果 =======');
callExpressions.forEach(call => console.log(call));

console.log('\n变量引用链:');
console.log(decodeFuncArr);

decodeFuncArr.forEach(item => {
    console.log(`变量 ${item.name} 在作用域 ${item.scope} 中`);
});

let newAst = parse('')  // 创建新的AST
// 将原始AST的前3个节点复制到新AST中
newAst.program.body = ast.program.body.slice(0, 3)

// 生成解密函数代码
let stringDecryptFunc = generator(newAst, { compact: true, }).code

// 执行解密函数代码
eval(stringDecryptFunc)

let argsType = ['isNumericLiteral', 'isMemberExpression']  // 参数类型列表
let originalDecodeFunc = null;
// 创建对象存储所有变量的值
let variableValues = {};

// 收集所有变量的值
traverse(ast, {
    VariableDeclarator(path) {
        if (path.get('id').isIdentifier()) {
            const varName = path.get('id').node.name;
            // 处理数字字面量
            if (path.get('init').isNumericLiteral()) {
                variableValues[varName] = path.get('init').node.value;
            }
            // 处理对象表达式
            else if (path.get('init').isObjectExpression()) {
                const obj = {};
                path.get('init').get('properties').forEach(prop => {
                    const key = prop.get('key').node.name;
                    if (prop.get('value').isNumericLiteral()) {
                        obj[key] = prop.get('value').node.value;
                    }
                });
                variableValues[varName] = obj;
            }
        }
    }
});
// 遍历AST处理函数调用
traverse(ast, {
    CallExpression: {
        exit: function (path) {
            if (path.get('callee').isIdentifier()) {
                const calleeName = path.get('callee').node.name;

                // 获取当前作用域名称
                let scopeName = 'global';
                let currentPath = path;
                while (currentPath.parentPath) {
                    if (currentPath.parentPath.isFunctionDeclaration()) {
                        scopeName = currentPath.parentPath.get('id').node.name;
                        break;
                    }
                    currentPath = currentPath.parentPath;
                }

                // 检查是否是解密函数调用（包括通过变量引用链的调用）
                const isDecodeFunc = decodeFuncArr.some(item =>
                    item.name === calleeName &&
                    (item.scope === 'global' || item.scope === scopeName)
                );

                // 如果是解密函数调用且只有一个参数
                if (isDecodeFunc && path.get('arguments').length === 1) {
                    let arg = path.get('arguments.0').node;
                    let argValue;

                    // 处理不同类型的参数
                    if (types.isNumericLiteral(arg)) {
                        // 如果是数字字面量，直接获取值
                        argValue = arg.value;
                    }

                    // 如果成功获取参数值，则进行解密
                    if (argValue !== undefined) {
                        // 调用解密函数获取结果
                        const result = eval(`${startFuncName}(${argValue})`);
                        console.log(path.toString(), '-->', result);

                        // 用解密后的字符串替换原节点
                        path.replaceWith(types.stringLiteral(result));
                    }
                }
            }
        }
    }
})

// 处理字符串拼接
traverse(ast, {
    BinaryExpression: {
        exit: function (path) {
            // 检查是否是字符串字面量的拼接
            let left = path.get("left").node.value
            let right = path.get("right").node.value
            if (path.get("left").isStringLiteral() && path.get("right").isStringLiteral()) {
                // 直接替换为拼接后的字符串
                path.replaceInline(types.valueToNode(left + right))
            }
        }
    }
})

// 定义内置函数名列表，用于排除这些属性
let buildInFunc = [
    'apply', 'slice', 'shift', 'which', 'split', 'index', 'input', 'clone', 'token', 'refer', 'scene', 'width',
    'style', 'round', 'parse', 'match', 'catch'
]
// 从对象中还原字符串
traverse(ast, {
    MemberExpression: {
        exit: function (path) {
            // 检查是否是对象属性访问
            if (
                path.get('object').isIdentifier() &&
                path.get('property').isStringLiteral()
            ) {
                // console.log(path.toString())
                let identifier = path.get('object.name').node
                let property = path.get('property.value').node

                // 只处理长度为5的属性名
                if (property.length !== 5) return
                // 排除内置函数名
                if (buildInFunc.indexOf(property) !== -1) return
                // 检查标识符是否在当前作用域中定义
                if (!path.scope.getAllBindings()[identifier]) return

                // 获取绑定信息
                const binding = path.scope.getAllBindings()[identifier];
                if (!binding || !binding.path) {
                    return;
                }

                // 安全地获取属性节点
                const init = binding.path.get('init');
                if (!init || !init.node || !init.node.properties) {
                    return;
                }
                // 获取对象所有属性 
                let property_nodes = init.get('properties');
                if (!property_nodes) {
                    return;
                }

                // 遍历属性查找匹配的字符串值
                for (let i = 0; i < property_nodes.length; i++) {
                    let obj_property = property_nodes[i].get('key.value').node
                    if (
                        obj_property === property &&
                        property_nodes[i].get('value').isStringLiteral()
                    ) {
                        console.log(path.toString(), '-->', property_nodes[i].get('value.value').node)
                        // 用实际的字符串值替换属性访问
                        path.replaceWith(types.valueToNode(property_nodes[i].get('value.value').node))
                    }
                }
            }
        }
    }
})

// 从对象中还原函数调用
traverse(ast, {
    CallExpression: {
        exit: function (path) {
            // 检查是否是对象方法的调用
            if (
                path.get('callee').isMemberExpression() &&
                path.get('callee.property').isStringLiteral()
            ) {
                // console.log(path.toString())
                let identifier = path.get('callee.object.name').node
                let property = path.get('callee.property.value').node

                // 只处理长度为5的属性名
                if (property.length !== 5) return
                // 排除内置函数名
                if (buildInFunc.indexOf(property) !== -1) return


                // 获取绑定信息
                const binding = path.scope.getAllBindings()[identifier];
                if (!binding || !binding.path) {
                    return;
                }

                // 安全地获取属性节点
                const init = binding.path.get('init');
                if (!init || !init.node || !init.node.properties) {
                    return;
                }

                let property_paths = init.get('properties');
                if (!property_paths) {
                    return;
                }
                // 获取对象的所有属性
                property_paths = Array.from(property_paths)

                // 遍历属性查找匹配的函数
                property_paths.forEach(node_path => {
                    let obj_property = node_path.get('key.value').node
                    if (
                        obj_property === property &&
                        node_path.get('value').isFunctionExpression()
                    ) {
                        // 获取函数体
                        let func_bodys = node_path.get('value.body.body')
                        func_bodys = Array.from(func_bodys)

                        // 处理函数体中的return语句
                        func_bodys.forEach(body => {
                            if (body.isReturnStatement()) {
                                if (body.get('argument').isBinaryExpression()) {
                                    // 处理二元表达式（操作符）
                                    let operator = body.get('argument.operator').node
                                    let left = path.get('arguments.0')
                                    let right = path.get('arguments.1')
                                    console.log(path.toString(), '-->', left.toString(), operator, right.toString())
                                    path.replaceWith(types.binaryExpression(operator, left.node, right.node))
                                } else if (body.get('argument').isCallExpression()) {
                                    // 处理函数调用
                                    let origin_args = path.get('arguments')
                                    origin_args = Array.from(origin_args)
                                    let args
                                    if (origin_args.length === 1) {
                                        args = []  // 没有参数
                                    } else {
                                        args = origin_args.slice(1).map(arg => arg.node)
                                    }
                                    let old_path_string = path.toString()
                                    path.replaceWith(types.callExpression(origin_args[0].node, args))
                                    console.log(old_path_string, '-->', path.toString())
                                } else if (body.get('argument').isLogicalExpression()) {
                                    // 处理逻辑表达式
                                    let operator = body.get('argument.operator').node
                                    let left = path.get('arguments.0')
                                    let right = path.get('arguments.1')
                                    console.log(path.toString(), '-->', left.toString(), operator, right.toString())
                                    path.replaceWith(types.logicalExpression(operator, left.node, right.node))
                                }
                            }
                        })
                    }
                })
            }
        }
    }
})

// 处理控制流
let controler_code = {}  // 存储控制流代码
let controler = {}  // 存储控制器

traverse(ast, {
    WhileStatement: {
        exit: function (path) {
            // 检查是否是空数组或一元表达式作为条件
            if (
                path.get('test').isUnaryExpression() ||
                (path.get('test').isArrayExpression() && path.get('test').toString() === '[]')
            ) {
                // 跳过空循环体或try语句
                if (path.get('body.body').length === 0) return
                if (path.get('body.body.0').isTryStatement()) return

                // console.log(path.toString())
                let switch_condition
                try {
                    // 获取控制器名称
                    switch_condition = path.get('body.body.0.discriminant.object.name').node
                } catch (e) {
                    return
                }

                // 初始化控制器代码对象
                controler_code[switch_condition] = {}

                // 检查控制器初始化是否使用字符串字面量
                if (!path.scope.getAllBindings()[switch_condition].path.get('init.callee.object').isStringLiteral()) return

                // 获取控制器值
                eval(`controler['${switch_condition}'] = ` + path.scope.getAllBindings()[switch_condition].path.get('init').toString())

                // 获取所有case节点
                let cases_path = path.get('body.body.0.cases')

                // 处理每个case
                for (var i = 0; i < cases_path.length; i++) {
                    let case_num = cases_path[i].get('test.value').node
                    controler_code[switch_condition][case_num] = []
                    let case_content = cases_path[i].get('consequent')
                    case_content = Array.from(case_content)

                    // 处理case内容，排除continue语句
                    case_content.forEach(c => {
                        if (!c.isContinueStatement()) {
                            controler_code[switch_condition][case_num].push(c)
                        }
                    })
                }

                // 按控制器顺序重组代码
                let code_node = []
                for (var i = 0; i < controler[switch_condition].length; i++) {
                    let index = controler[switch_condition][i]
                    controler_code[switch_condition][index].forEach(n => {
                        code_node.push(n.node)
                    })
                }

                // 替换while语句为重组后的代码
                path.replaceWithMultiple(code_node)
            }
        }
    }
})

// 处理字面量
const transform_literal = {
    // 处理数字字面量，移除进制前缀
    NumericLiteral({ node }) {
        if (node.extra && /^0[obx]/i.test(node.extra.raw)) {
            node.extra = undefined;
        }
    },
    // 处理字符串字面量，移除转义序列
    StringLiteral({ node }) {
        if (node.extra && /\\[ux]/gi.test(node.extra.raw)) {
            node.extra = undefined;
        }
    }
}
traverse(ast, transform_literal)

// 处理表达式计算
traverse(ast, {
    BinaryExpression: {
        exit(path) {
            // 尝试计算表达式的值
            let { confident, value } = path.evaluate();
            if (!confident) return
            // 用计算结果替换表达式
            path.replaceInline({ type: "NumericLiteral", value: value })
        }
    }
})

// 删除未引用的变量
ast = parse(generator(ast, { compact: true }).code)
traverse(ast, {
    VariableDeclarator: {
        exit(path) {
            let { init, id } = path.node;
            // 只处理对象表达式和标识符
            if (!types.isObjectExpression(init) && !types.isIdentifier(id)) return;
            let { scope } = path;
            let binding = scope.getBinding(id.name);
            // 如果变量没有被引用，则删除
            if (binding.referencePaths.length !== 0) return;
            path.remove();
        }
    }
})

//////////////////

// 将AST转换回JS代码
let { code } = generator(ast, { compact: false });

// 保存反混淆后的代码
fs.writeFile('./decode.js', code, (err) => {
});