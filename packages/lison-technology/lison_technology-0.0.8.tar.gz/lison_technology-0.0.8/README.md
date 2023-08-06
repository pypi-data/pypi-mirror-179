# 关于lison_output的介绍

---



## 基础

~~~python
import lison_technology
lison_technology.version_declaration()
~~~
run:
~~~
lindy[v0.0.1]-->The program is stable
~~~

-----
## out 对象
~~~
lison_output.out
~~~

motion 函数
~~~python
import lison_technology
txt = ["Hello", "I am Mike", "Welcome to lison_technology"]
for i in range(3):
    lison_technology.out.motion(txt[i], 3, 1)
~~~
