# Vaststream2.0

This is a root repo for vaststream 2.0. It's only used for compiling and delivering vaststream SDK. All source codes of SDK lib are put in respective repo as submodule.

## python库
### 工程结构
> tips: 外层vaststream只做引导，具体的接口封装实现在各自模块的python目录中  
```bash
.
├── all_gen
├── env
├── extern
│   └── pybind11                 # 引入pybind11三方库
├── python
│   ├── CMakeLists.txt           # python接口主模块 bind 实现编译入口
│   ├── src                      # python接口主模块 bind 实现源码入口
│   │   └── vaststream.cc
│   ├── test                     # python接口主模块 vaststream单元测试目录
│   │   └── test_vaststream.py
│   └── vaststream               # python主模块入口
│       └── __init__.py
├── sample                     
│   ├── python                   # python sample目录
│   └── README.md
├── .pypirc                      # pypi账户信息管理
├── setup.py                     # python打包入口脚本
├── vace
├── vacl
├── vacm
├── vame
│   └── python
│       ├── CMakeLists.txt       # python子模块接口 bind 实现编译入口
│       ├── src                  # python子模块接口 bind 实现源码目录
│       │   ├── vame.cc
│       │   ├── decoder.cc
│       │   ├── encoder.cc
│       │   └── utils.cc
│       ├── test                 # python子模块接口 单元测试目录
│       │   ├── test_common.py
│       │   ├── test_decoder.py
│       │   └── test_encoder.py
│       └── vame                 # python子模块模块入口
│           ├── __init__.py
│           ├── decoder.py
│           ├── encoder.py
│           └── utils.py
├── vaml
└── README.md
```

### 安装编译
> tips: 当前runtime等基础库没有进入打包范围，需要将其路径暴露到 LD_LIBRARY_PATH，将TVM下拉到vaststream2.0下编译即可
```bash
# 初始化环境变量
source env/set_env.sh
# 编译安装
python3 setup.py install
```

### 单元测试
> tips: 数据集统一管理，数据统一放到vaststream2.0/data目录下，按照模块进行管理
* 下载数据
```bash
# 同步云存储数据到本地
python3 python/dataManager.py -d
```
* 上传数据
```bash
# 新增数据放到数据存储目录后执行该脚本同步到云存储
python3 python/dataManager.py -u
```
* 测试代码对数据的使用
```python
# 定位数据存储目录
DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))), "data")
# 定位具体文件位置，其使用可以参考 vaststream2.0/vame/python/test/test_decoder.py
image_path = os.path.join(DATA_PATH, "vame", "images", "1920x1080.jpg")
```
> tips: 单元测试文件写到各个模块的 python/test目录下
```bash
python3 setup.py test
```
单独测试某一个case
```bash
# 先安装编译
python3 setup.py install
# 指定测试case
pytest vame/python/test/test_common.py
```

### 包管理
> tips: 不同平台需要分别编译发布，这里以linux平台为例
* 打包
```bash
python3 setup.py bdist_wheel --plat-name=manylinux1_x86_64
```

* 上传发布
```bash
twine upload dist/* --config-file ./.pypirc
```