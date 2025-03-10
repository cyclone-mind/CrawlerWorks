// fs模块 用于操作文件的读写
const fs = require("fs")

;
// @babel/parser 用于将JavaScript代码转换为ast树
const parser = require("@babel/parser");
// @babel/traverse 用于遍历各个节点的函数
const traverse = require("@babel/traverse").default;
// @babel/types 节点的类型判断及构造等操作
const types = require("@babel/types");
// @babel/generator 将处理完毕的AST转换成JavaScript源代码
const generator = require("@babel/generator").default;

// 混淆的js代码文件
const encode_file = "./encode.js"
// 反混淆的js代码文件
const decode_file = "./decode.js"

// 读取混淆的js文件
let jsCode = fs.readFileSync(encode_file, {encoding: "utf-8"});
// 将javascript代码转换为ast树
let ast = parser.parse(jsCode,{
    sourceType:"script"
})

//ast反混淆插件编写
function decrypt_str(ast){ //1.字符解码
    traverse(ast,{
        //遍历字符串节点和数字节点(因为有科学计数法表示的数组)
        'StringLiteral|NumericLiteral'(path){
            //删除节点中的extra属性
            delete path.node.extra.raw
        }
    })
    return ast
}
function func_replace(path){
    const node = path.node;
    if(node.declarations.length !== 3)return
    if(generator(node.declarations[0].init).code !== "mwbxQ.$_Cg")return
    node.declarations = [node.declarations[0],node.declarations[2]]
    node.declarations[1].init = node.declarations[0].init
    path.getNextSibling().remove()
    path.getNextSibling().node.declarations[0].init = node.declarations[0].init
}
function func_replaces(path){
    const node = path.node
    const scope = path.scope
    const leftName = node.id.name
    if(generator(node.init).code !== "mwbxQ.$_Cg")return
    let binding_left = scope.getBinding(leftName)
    if(binding_left.referencePaths.length !== 0){
        binding_left.referencePaths.forEach(function (path){
            const left_path = types.identifier("mwbxQ")
            const right_path = types.identifier("$_Cg")
            const replace_path = types.memberExpression(left_path,right_path);
            path.replaceWithMultiple(replace_path)
        })
    }
    path.remove()
}
function func_decrypt_str(ast){
    //将解密代码执行
    let end = 5
    let newAst = parser.parse('')
    newAst.program.body = ast.program.body.slice(0,end)
    let stringDecryptFunc = generator(newAst,{compact:true,}).code
    eval(stringDecryptFunc)
    //获取解密函数的名字
    const stringDecryptFuncAst = ast.program.body[2]
    const  DecryptLeftFuncName = stringDecryptFuncAst.expression.left.object.name
    const DecryptRightFuncName = stringDecryptFuncAst.expression.left.property.name
    //调用解密函数的代码执行，将执行后的值替换调用解密函数的代码
    traverse(ast,{
        CallExpression(path){
            if(types.isMemberExpression(path.node.callee) &&
                path.node.callee.object.name &&
                path.node.callee.object.name === DecryptLeftFuncName &&
                path.node.callee.property.name &&
                path.node.callee.property.name === DecryptRightFuncName){
                    path.replaceWith(types.valueToNode(eval(path.toString())))
            }
        }
    })
    return ast
}
function func_switch(path){
    const node = path.node
    if(!(node.body.body[0] && node.body.body[0].type === "VariableDeclaration"))return
    if(!(node.body.body[0].declarations && node.body.body[0].declarations.length === 1))return
    if(!(node.body.body[1].body.body[0].cases[0]))return
    if(!(node.body.body[1].body.body[0].cases[0].consequent))return
    const consequent = node.body.body[1].body.body[0].cases[0].consequent
    const consequent_length = consequent.length
    const conseq_two = consequent[consequent_length-2]
    if(node.body.body[1].body.body[0].cases.length === 1){
        if(conseq_two.type === "ExpressionStatement" &&
            conseq_two.expression &&
            conseq_two.expression.type === "AssignmentExpression" &&
            conseq_two.expression.right &&
            conseq_two.expression.right.type === "MemberExpression" &&
            conseq_two.expression.right.property &&
            conseq_two.expression.right.property.type === "NumericLiteral"){
            node.body.body = consequent.slice(0,-2)
        }else{
            node.body.body = consequent.slice(0,-1)
        }
    }else{
        var merge_array = []
        var case_length = node.body.body[1].body.body[0].cases.length
        node.body.body[1].body.body[0].cases.forEach(function (node){
            case_length -= 1
            if(case_length === 0){
                const node_consequent_length = node.consequent.length
                const node_second = node.consequent[node_consequent_length - 2]
                if(node_second.type === "ExpressionStatement" &&
                    node_second.expression &&
                    node_second.expression.type === "AssignmentExpression" &&
                    node_second.expression.right &&
                    node_second.expression.right.type === "MemberExpression" &&
                    node_second.expression.right.property &&
                    node_second.expression.right.property.type === "NumericLiteral"){

                    merge_array = merge_array.concat(node.consequent.slice(0,-2))
                }else{
                    merge_array = merge_array.concat(node.consequent.slice(0,-1))
                }
            }else{
                merge_array = merge_array.concat(node.consequent.slice(0,-2))
            }
        })
        node.body.body = merge_array
    }
}
function delete_func(path){
    if(path + '' === "mwbxQ.$_DW()"){
        path.parentPath.parentPath.parentPath.parentPath.remove()
    }
}
//1.字符解码
decrypt_str(ast)
//2.重复引用赋值反混淆
traverse(ast,{VariableDeclaration:func_replace,})
traverse(ast,{VariableDeclarator:func_replaces,})
//3.带数字参数的函数返回字符串替换该函数的调用
func_decrypt_str(ast)
//4.switch控制流处理
traverse(ast,{FunctionDeclaration: func_switch,})
//5.删除无用函数(还有一些swith为空的代码进行删除)
traverse(ast,{CallExpression:delete_func,})
ast.program.body = ast.program.body.slice(5)

// const visitor = {}
// traverse(ast,visitor)

// 将处理后的ast转换为js代码(反混淆后的代码)
let {code} = generator(ast);
// 保存代码
fs.writeFile('decode.js', code, (err)=>{});