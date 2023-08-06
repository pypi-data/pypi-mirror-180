# rqrcode.py

![CI](https://github.com/korykim/rqrcode/workflows/CI/badge.svg)
# 使用方法(usage)

### 安装(install)
```shell
pip install rqrcode
```

### 测试(test)
```python
from rqrcode import rqrcode

if __name__ == '__main__':
    # 生成二维码PNG图片保存(Generate QR code PNG picture and save)
    rqrcode.qrcode_img("hello","C:\\Users\\user\\Desktop\\qrcode.png")
    # 生成二维码SVG图片保存(Generate QR code SVG picture and save)
    rqrcode.qrcode_svg("hello","C:\\Users\\user\\Desktop\\qrcode.svg")
    # 生成二维码unicode(Generate QR code unicode)
    rqrcode.qrcode_unicode("hello")
```


# 扩展(extend)
### 如果使用源码自定义扩展(If you use the source code to customize the extension)
- 1.下载源码(Download source code)
```shell
git clone https://github.com/korykim/rqrcode
```
- 2.安装(Install)
```shell
python -m venv C:\Users\user\myenv # 创建虚拟环境(Create virtual environment)

cd C:\Users\user\myenv\Scripts # 进入虚拟环境目录(Enter the virtual environment directory)

.\activate # 激活虚拟环境(Activate virtual environment)

pip install maturin # 安装maturin(Install maturin)

cd rqrcode # 进入源码目录(Enter the source code directory)

maturin develop # 会自动打包出一个 wheel 包，并且安装到当前的 venv 中(Automatically package a wheel package and install it to the current venv)

```
- 3.现在可以在python中正常使用了(Now you can use it normally in python)
- 4.发布whl包(Publish whl package)
```shell
maturin build --release --interpreter python
```

此时在./target/wheels目录下会生成whl包，可以上传到pypi或者使用pip install安装(At this time, a whl package will be generated in the ./target/wheels directory, which can be uploaded to pypi or installed using pip install).
