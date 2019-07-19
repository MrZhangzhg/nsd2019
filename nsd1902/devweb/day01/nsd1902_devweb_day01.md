# nsd1902_devweb_day01

## HTML：超文本标记语言

做网页时，可以使用dreamweaver，它是一款所见即所得的网页制作工具，可以像写word一样做网页。

标记：

- 双标记
```html
<h1>这是一号标题</h1>
```

- 单标记

  ```html
  <br>
  <hr>
  ```

- 标记也称作元素

- 元素还可以嵌套

  ```html
  <html>
      <head>
          <title>标题</title>
      </head>
      <body>
          <p>这是一个段落</p>
      </body>
  </html>
  ```

> 注意：HTML制作不是所见即所得的样式，往往编写时看的代码和最终显示出来的效果，完全不一样。

### 块级元素

不管内容有多少，至少要占一行。

- 标题元素：h1 - h6
- 段落元素：p
- 区块元素：div

### 跳转到页面内的链接

1. 跳转到的位置，先设置一个锚点

   ```html
   <h1 id="id1">这是一号标题</h1>
   ```

2. 创建a标记，指向锚点

   ```html
   <a href="#id1">跳转到id1</a>
   ```

3. href的值如果只是#号，将跳转到顶部

## CSS：层叠样式表、级联样式表

### CSS样式表的应用方式

- 内联方式，类似于HTML标记属性。内容和表现形式混在一起，不建议

  ```html
  <p style="font-weight: bold">这是一个测试</p>
  ```

- 内部样式，将样式表写在html页面的head标记中

  ```html
  <head>
      <meta charset="UTF-8">
      <title>my css1</title>
      <style>
          body {
              background: silver;
              color: darkblue;
          }
          hr {
              color: red;
          }
      </style>
  </head>
  ```

- 外部样式，样式表单独是一个文件，所有的HTML页面都可以使用这个外部样式表文件。外部样式表文件不一定在本地，也可以是一个URL。

  ```html
  <head>
      ... ...
      <link rel="stylesheet" href="static/css/bootstrap.min.css">
  </head>
  ```

  







