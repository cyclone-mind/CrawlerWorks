const traverse = require('@babel/traverse').default;
const parser = require('@babel/parser');

// 示例混淆代码
const code = `
let U = function() { console.log('Original Function'); };
let V = U;
function someFunction() {
    let V = U;  // 这是我们要追踪的引用
    V();
}
function anotherFunction() {
    let U = function(){}
    let Y = U
    let V = function() { console.log('Different Function'); };  // 同名但不同的函数
    V();
}
let W = V;
let X = W;
X();
`;

// 解析代码为 AST
const ast = parser.parse(code);

let startFuncName = 'U';
let decodeFuncArr = [];
let scopeRedefinesU = {};

// 第一次遍历: 收集所有作用域信息
traverse(ast, {
    VariableDeclarator(path) {
        // 获取作用域名称
        let scopeName = 'global';
        let currentPath = path;
        while (currentPath.parentPath) {
            if (currentPath.parentPath.isFunctionDeclaration()) {
                // console.log(currentPath.parentPath);
                
                scopeName = currentPath.parentPath.get('id').node.name;
                break;
            }
            currentPath = currentPath.parentPath;
        }

        // 初始化作用域信息
        if (!scopeRedefinesU[scopeName]) {
            scopeRedefinesU[scopeName] = false;
        }

        // 检查是否重定义了U
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
