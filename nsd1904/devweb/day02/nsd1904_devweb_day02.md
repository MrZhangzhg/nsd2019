# nsd1904_devweb_day02

## CSS: 层叠样式表

- 构成
  - 选择器：为谁设置样式
  - 样式声明：设置成什么样

### CSS特点

- 继承性：大多数 CSS 的样式规则可以被继承
- 层叠性：可以定义多个样式，不冲突时,多个样式表中的样式可层叠为一个
- 优先级：样式定义冲突时,按照不同样式规则的优先级来应用样式

### 选择器

- \*：通用选择器，可以与任何元素匹配
- 元素选择器：html 文档的元素就是选择器
- 类选择器：每个元素都可以通过class来设置类，可以理解为分组
- id选择器：每个元素都可以通过id设置一个唯一标识
- 群组选择器：用逗号将多个选择器分隔，统一设置样式
- 伪类选择器：通常用于为a标签设置访问前、鼠标悬停、访问后的样式

### 颜色表示

- 使用三元色：RGB。每种颜色都采用一个字节表示，10进制从0到255，16进制从00到FF。
- Red
- Green
- Blue
- 10进制表示方式：rgb(r, g, b)
- 16进制表示方式：#rgb
- 数值越大表示该颜色越亮，值越小表示该颜色越暗

### 框模型/盒子模型

- 元素由这几个部分构成：
  - 元素
  - 内边距：padding
  - 边框：border
  - 外边距：margin

## 样式示例：导航栏

```shell
1. 创建ul
<ul>
    <li><a href="#">Home</a></li>
    <li><a href="#">News</a></li>
    <li><a href="#">Contact</a></li>
    <li><a href="#">About</a></li>
</ul>
2. 默认的ul拥有内边距、外边距。每个li前面有个项目标识符出现在内边距中。为了一切都自行定义，将这些默认样式清除。
ul {
    list-style-type: none;   /*删除标号*/
    padding: 0;
    margin: 0;
}
3. 将导航栏设置为水平方向
li {
	display: inline;
}
4. 因为li的宽度与其中的文字有关，为了精确设置，首先将其设置为左浮动
li {
	float: left;
}
5. 为了能给a标签设置宽度，需要把它转换成块元素
a {
    display: block;
    width: 60px;
}
6. 进一步设a标签
a {
    text-align: center;   /*文字居中*/
    background-color: #BEBEBE;   /*背景色*/
    display: block;   /*将a转为块元素，以便设置宽度*/
    width: 80px;    /*宽度为80px*/
    text-decoration: none;   /*取消下划线*/
    border-bottom: 2px solid #900B09;   /*添加红色下边框*/
}
7. 鼠标悬停时，变换背景色
a:hover {
	background-color: #900B09;
}
```













