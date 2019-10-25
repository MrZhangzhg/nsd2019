## nsd1905_devweb_day02

## CSS

- 由两部分组成：选择器 ＋ 样式声明
- 特征：
  - 继承性：子元素可以继承父元素的样式
  - 层叠性：元素的样式可以来自于多个样式声明
  - 优先级：样式设置有冲突时，样式根据优先级来设置

- 选择器：
  - 通用选择器：*，匹配任何元素，用于设置统一的样式
  - 元素选择器：html元素
  - 类选择器：使用class属性，可以理解为分组。
  - id选择器：为元素设置id属性，只针对某一个元素设置样式
  - 群组选择器：通过逗号将选择器放到一个组中，统一设置样式
  - 伪类选择器：一般用于为超链接设置访问前、鼠标悬停、访问后的样式

颜色：采用RGB颜色。每种颜色都用8位2进制数来表示，如果写为10进制数是rgb(d, d, d)，也可以用16进制数表示为#xxxxxx。还可以使用颜色单词。数值越小，表示某种颜色越暗，值越大表示颜色越亮

- R: Red
- G: Green
- B: Blue

### 框模型

- 也称作盒子模型
- 在html中，一切都是框
- 每个框都有外边距、边框和内边距

## bootstrap

- twitter公司推出的开源前端web框架
- 可以简单的理解为它是一个大的样式表文件
- 中文官方站：https://www.bootcss.com/
- 准备环境，将nsd1904班devweb/day02/目录的static目录拷贝到工作目录

```shell
# ls static/
css  fonts  imgs  js
css->样式表目录
fonts->字体
imgs->图片
js->javascript脚本
```

将文件nsd2019/ebooks/web/bootstrap_pdf.tar.gz 解压，可以得到pdf电子书目录。



## 一、排版样式

- Bootstrap 将全局 font-size 设置为 14px,line-height 行高设置为 1.428(即20px);p段落元素被设置等于 1/2 行高(即 10px);颜色被设置为#333333。
- 标题元素大小
  - h1: 36px
  - h2: 30px
  - h3: 24px
  - h4: 18px
  - h5: 14px
  - h6: 12px
- 为了统一，bootstrap还创建了h1到h6 class，样式与标题元素一致
- 内联文本元素，各种加线条的文本、强调的文本

```html
<mark>达内云计算 nsd1904</mark>
<del>达内云计算 nsd1904</del>
<s>达内云计算 nsd1904</s>
<ins>达内云计算 nsd1904</ins>
<u>达内云计算 nsd1904</u>
<small>达内云计算 nsd1904</small>
<strong>达内云计算 nsd1904</strong>
<em>达内云计算 nsd1904</em>
```

- 对齐方式

```html
<p class="text-center">达内云计算 nsd1904</p>
<p class="text-left">达内云计算 nsd1904</p>
<p class="text-right">达内云计算 nsd1904</p>
```

- 颜色
  - danger: 危险红
  - muted：柔和灰
  - primary：首要蓝
  - info：信息蓝
  - success：成功绿
  - warning：警告黄

```html
<p class="text-center text-primary bg-warning">达内云计算 nsd1904</p>
<p class="text-left text-danger bg-success">达内云计算 nsd1904</p>
<p class="text-right text-muted bg-info">达内云计算 nsd1904</p>
```

## 二、表格

```html
<table class="table table-bordered table-striped table-hover">
```

## 三、按钮

```html
<input type="submit" value="查 询"><br>
<input class="btn btn-default btn-sm" type="submit" value="查 询"><br>
<input class="btn btn-primary" type="submit" value="查 询"><br>
<input class="btn btn-info btn-lg" type="submit" value="查 询"><br>
<input class="btn btn-warning" type="submit" value="查 询"><br>
<input class="btn btn-success btn-xs" type="submit" value="查 询"><br>
<input class="btn btn-danger" type="submit" value="查 询"><br>
<input class="btn btn-primary btn-block" type="submit" value="查 询"><br>
<input type="submit" value="查 询"><br>
<input type="submit" value="查 询"><br>
```

## 四、表单

- 为了有很好的间距，应该把各个控件放到form-group中
- 每个文本类型的控件，放到form-control中

```html
<form action="">
    <div class="form-group">
        <label>uname: </label><input class="form-control" type="text">
    </div>
    <div class="form-group">
        <label>upass: </label><input class="form-control" type="text">
    </div>
    <div class="form-group">
        <input class="btn btn-primary" type="submit">
    </div>
</form>
```

- 如果希望表单只占一行，只要设置form的class

```html
<form action="" class="form-inline">
    <div class="form-group">
        <label>uname: </label><input class="form-control" type="text">
    </div>
    <div class="form-group">
        <label>upass: </label><input class="form-control" type="text">
    </div>
    <div class="form-group">
        <input class="btn btn-primary" type="submit">
    </div>
</form>
```

## 五、图片

```html
<!-- 圆角矩形 -->
<img class="img-rounded" src="https://img01.sogoucdn.com/app/a/100520021/c0b43a061bdb06f3b983953f41e7e8d0">
<!-- 圆形 -->
<img class="img-circle" src="https://img01.sogoucdn.com/app/a/100520021/c0b43a061bdb06f3b983953f41e7e8d0">
<!-- 支持自动缩放 -->
<img class="img-thumbnail" src="https://img01.sogoucdn.com/app/a/100520021/c0b43a061bdb06f3b983953f41e7e8d0">
```

## 六、栅格系统

1. 实现页面布局
2. 布局时，要求页面所有的元素位于container中
3. container的直接子元素是row
4. row中的元素是col-xx-yy
5. 一个row最多支持12列。其中的col-xx-yy设置为占多少列
   1. col-lg-3表示大屏幕尺寸下，它占3列
   2. col-md-4表示中等屏幕尺寸下，它占4列
   3. col-sm-2表示小屏幕尺寸下，它占6列
6. 还可以设置自适应屏幕大小

```html
<div class="container">
    <div class="row">
        <div class="col-lg-3 bg-primary col-md-4 col-sm-6">
            云计算<br>
            nsd 1904
        </div>
        <div class="col-lg-3 bg-danger col-md-4 col-sm-6">
            云计算<br>
            nsd 1904
        </div>
        <div class="col-lg-3 bg-success col-md-4 col-sm-6">
            云计算<br>
            nsd 1904
        </div>
        <div class="col-lg-3 bg-warning col-md-4 col-sm-6">
            云计算<br>
            nsd 1904
        </div>
    </div>
</div>
```

## 七、导航

- 水平导航

```html
<div class="container" style="margin-top: 10px">
    <ul class="nav nav-tabs">
        <li class="active"><a href="#">Home</a></li>
        <li><a href="#">News</a></li>
        <li><a href="#">Contact</a></li>
        <li><a href="#">About</a></li>
    </ul>
</div>

<div class="container" style="margin-top: 10px">
    <ul class="nav nav-tabs nav-pills">
        <li class="active"><a href="#">Home</a></li>
        <li><a href="#">News</a></li>
        <li><a href="#">Contact</a></li>
        <li><a href="#">About</a></li>
    </ul>
</div>
```

- 垂直导航

```html
<div class="container" style="margin-top: 10px">
    <div class="row">
        <div class="col-sm-2">
            <ul class="nav nav-stacked nav-pills">
                <li class="active"><a href="#">Home</a></li>
                <li><a href="#">News</a></li>
                <li><a href="#">Contact</a></li>
                <li><a href="#">About</a></li>
            </ul>
        </div>
        <div class="col-sm-7 bg-danger">
            这是中间区域<br>
            这是中间区域
        </div>
        <div class="col-sm-3 bg-warning">
            这是右边区域<br>
            这是右边区域
        </div>
    </div>
</div>
```



