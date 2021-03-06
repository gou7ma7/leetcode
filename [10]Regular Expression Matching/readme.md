# lhr
## 方法论
很明显前面的状态会影响到之后的匹配情况，因此是很明显的动态规划，  
又因为假如当前匹配时候遇到'.*'这个匹配符号，会影响之前的状态，使用动态规划不如递归描述逻辑简单，
因此使用递归 + 备忘录最优。

## 思路
1. 采用递归(不用最外面的while True了，判定递归出口就行)；
2. 递归出口： 若p已经匹配完成，则检查s，也匹配完(True)，还有剩(False);
3. now_match： 当前开始匹配的状态；
4. 判断p连续两个的情况，分为是否有*（因为*会影响到前一个匹配状态，如果不检查往后一个，就要在检查的时候往前搜索，更加的麻烦；
5. 如果后面紧着的不是*，那么直接返回比较结果；
6. 否则 now_match：s往后走（当前匹配，又*，看当前的这个p是否还能继续往后匹配）；  
not now_match： p往后走（当前不匹配，因为有*，所以直接跳过这个，对p之后的进行比较）。

## 情况本质
1. 没有*： 一一匹配，然后下一对；
2. \*：匹配0个，s不动，p往下两个，跳过当前字母和紧跟着的*；
3. *：匹配1～n个，p不动，s依次往下匹配；
4. 写递归推导式的是把2、3用or连接；
5. 递归基为s匹配完成 或当前字母匹配失败且p后面没有紧跟着*；

## 做不出来的分析
老生常谈的问题了，还是递推写的不够好，覆盖不了边界情况。

## 递归备忘录的优化
O(递归 + 备忘录) == O(dp)
按照高中时候llc的教育，很自然的还是使用了一张dp表，记录发生关系之间的两个变量之间的值；  
那么当变量变成3个的时候呢，构造高维队列开销实在太大，同时极大浪费。  

正巧有一位提到了functools中的lru_cache装饰器，因此顺便去了解了一下LRU算法。  
LRU（Least recently used，最近最少使用）算法根据数据的历史访问记录来进行淘汰数据，其核心思想是 “如果数据最近被访问过，那么将来被访问的几率也更高”。  
相比备dp表格忘录，最大的不同就是把所有的输入变量hash，然后装入一个dict中，并且借助轮子不需要手写维护。 
在工程上绝对这样做是ok的，将备忘录限制在1维，仅注意输入变量不考虑递推情况，多个变量只需要调整hash key等，  
但是做题的时候还是要手动维护表格的，毕竟做题练的就是一个递推公式和边际情况的判断。