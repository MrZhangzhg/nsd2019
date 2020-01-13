import wget
import os

def get_patt(fname, patt):
    '用于在文件中找到相关的模式'

if __name__ == '__main__':
    url = 'http://www.163.com'
    down_dir = '/tmp/163'
    fname = '/tmp/163/163.html'
    img_patt = ''
    img_list = get_patt(fname, img_patt)  # 取得图片url列表
    # 下载目录不存则创建
    if not os.path.exists(down_dir):
        os.mkdir(down_dir)
    # 如果网易首页文件不存在，则创建
    if not os.path.exists(fname):
        wget.download(url, fname)

    for img_url in img_list:
        wget.download(img_url, down_dir)
