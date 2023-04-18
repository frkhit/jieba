# 对比

## nuitka

```
word_list: [' ', ' ', ' ', ' ', '[', '红楼梦', ' ', '/', ' ', '曹雪芹', ' ', '著', ' ', ']', '\n', ' ', ' ', ' ', ' ', '手机']
[iter 1]time cost 5.306s
[iter 2]time cost 5.626s
[iter 3]time cost 5.015s
[iter 4]time cost 4.949s
[iter 5]time cost 4.967s
[iter 6]time cost 5.034s
[iter 7]time cost 5.248s
[iter 8]time cost 4.903s
[iter 9]time cost 4.899s
[iter 10]time cost 5.275s
[total iter 10][time_cost]avg 5.122s, max 5.626s, min 4.899s!
```

## pure python

```
word_list: [' ', ' ', ' ', ' ', '[', '红楼梦', ' ', '/', ' ', '曹雪芹', ' ', '著', ' ', ']', '\n', ' ', ' ', ' ', ' ', '手机']
[iter 1]time cost 9.367s
[iter 2]time cost 8.453s
[iter 3]time cost 7.749s
[iter 4]time cost 9.467s
[iter 5]time cost 6.602s
[iter 6]time cost 6.210s
[iter 7]time cost 6.180s
[iter 8]time cost 6.440s
[iter 9]time cost 6.195s
[iter 10]time cost 5.721s
[total iter 10][time_cost]avg 7.238s, max 9.467s, min 5.721s!
```