# nsd_1908_devweb_day01

w3school：https://www.w3school.com.cn/

## web开发

前端：在用户一侧执行、渲染的部分。HTML ＋ CSS ＋ JS(JavaScript)

后端：在服务一侧执行。PYTHON / PHP / JAVA

## HTML

### 标记

- 也叫标签、元素
- 标记又分为双标记和单标记

```html
<h1>双标记</h1>  <!--双标记-->
<hr>  <!--单标记-->
```

- 元素可以嵌套
- 元素可以设置属性，但是大多数的属性应该通过CSS样式表来设置
- 标记分为块级标记和行内标记
  - 块级标记至少占一行，如h1~h6标题、p、div、ul、ol
  - 行内标记不会产生换行
- 基础html样式

```html
<!DOCTYPE html>  <!--声明文档类型-->
<html lang="en">  <!--html是根标记，其他内容必须在html标记中-->
<head>   <!--用于声明一些说明内容-->
    <meta charset="UTF-8">  <!--元数据-->
    <title>我的测试网页</title>  <!--网页标题-->
</head>
<body>   <!--浏览器窗体中显示的内容，都要放到body中-->

</body>
</html>
```

### 静态文件的位置

- 一般会在网站的目录下建立

```shell
(nsd1908) [root@room8pc16 day01]# mkdir -p  static/{imgs,js,css}
(nsd1908) [root@room8pc16 day01]# ls static/
css  imgs  js
```

## CSS：层叠样式表

- 也叫级联样式表
- 作用
  - 实现了将内容与表现分离
  - 提高代码的可重用性和可维护性
- CSS样式表分类
  - 内联样式表：与元素属性一样使用。内容与形式混杂在一起，不推荐
  - 内部样式表：将样式统一声明到head中的style标签中
  - 外部样式表：将样式集中声明到一个单一的样式表文件中

