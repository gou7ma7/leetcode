# 举一反三
1. 本题本质与[11]题，数轴装水问题等基本上是一个类型的，都是暴力循环，通过找规律剪枝：
2. 一般来说是通过一个变量一次的改变代表一类的情况 / 找出两个变量间的线性关系，直接干掉不会出现的情况，将双重循环 -> 一次循环

# 多题一解

# 套路
1. 首先这种题都是通过暴力解O(n^2)，两重循环遍历完；
2. 这是所谓的双指针的第一道套路题，本质上就是两个参数之间不会同时变化，且有交集，因此类似于概率中的加法原则而不是乘法原则。
依次移动两个指针，化O(n^2) -> O(n*2)。（同[11])
3. 剪枝规律： 2nd < 3rd，因此第二重可以从 2nd_index到 len之间倒着遍历找3rd:
4. (解释一下)当前2nd确定之后，下一个2nd`对应的3rd绝对是在之前的 2nd_index到 len之间的，上一个3rd之后的数可以直接抛弃；
3. 或者前面两个数照例循环，第三个数建立hash，将本来应该遍历O(n) 找到的3rd O(1)时间找到，剪枝。