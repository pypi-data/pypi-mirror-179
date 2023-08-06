# typecho-password
Typecho（数据库中）用户密码的生成及验证


## 使用方法

1. 安装

```python
pip install typecho-password
```

2. 使用

```python
from typecho_password import PasswordContext

m = PasswordContext()
hashed_password = m.hash('123456789ABCabc')
print(m.verify('123456789ABCabc', hashed_password))
```
