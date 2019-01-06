class Solution {
public:
    // Function of 2n_or_2n+1    以size奇偶性返回答案（这样可以少写点代码）
    //但是这样当不为空的数组只有一个元素时，会越界。(在第19行进行判断)
    double Odd_or_even(int a, int b, int size){
        if(size % 2 == 0)
            return 0.5 * (a + b);
        else
            return a;
    }
    
    //实现函数
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int size1 = nums1.size();
        int size2 = nums2.size();
        int size = size1 + size2;
        

        if(size == 1)
            if(size1 == 0)  return nums2[0];
            else    return nums1[0];
        //其中一个为空数组的情况 
        if(!size1)
            return Odd_or_even(nums2[size2 / 2], nums2[size2 / 2] - 1, size);
        else if(!size2)
            return Odd_or_even(nums1[size1 / 2], nums1[size1 / 2] - 1, size);
        
        //数组均不为空的情况
        
        int j1 = 0, j2 = 0;        //j1,j2分别对应于nums1，nums2的下标。
        int k1 = 0, k2 = 0;        //每个数组中确定的小于中位数的个数 
        int k = (size + 1)/ 2;      
        while(k > 1)                //排除掉所有小于中位数的数
        {
            if(k % 2 == 0)
                j1 = k * 0.5 > size1 - k1 ? size1 - 1 : k * 0.5 + k1 - 1;
            else
                j1 = k * 0.5 + 1 > size1 - k1? size1 - 1 : k * 0.5 + k1;
            
            
            j2 = (size + 1) / 2 - j1 - 2 > size2 - 1? size2 - 1: (size + 1) / 2 - j1 - 2;
            if(nums1[j1] < nums2[j2])
            {
                k = k - (j1 - k1 + 1);
                k1 = j1 + 1;
                //若数组nums1所有的数都小于中位数，那么return
                if(k1 == size1)
                    if(size % 2 != 0)
                        return nums2[size / 2 - size1];
                    else
                        return 0.5 * 
                                (nums2[size / 2 - size1] + nums2[size / 2 - size1 - 1]);
            }
            else
            {
                k = k - (j2 - k2 + 1);
                k2 = j2 + 1;
                //同上
                if(k2 == size2)
                    if(size % 2 != 0)
                        return nums1[size / 2 - size2];
                    else
                        return 0.5 * 
                                (nums1[size / 2 - size2] + nums1[size / 2 - size2 - 1]);
            }                            
        }




        if(size % 2 == 1)
            return  nums1[k1] > nums2[k2] ? nums2[k2] : nums1[k1];
        else
        {
            if(nums1[k1] < nums2[k2])
            {
                if(k1 == size1 - 1)
                    return 0.5 * (nums1[k1] + nums2[k2]);
                else
                {
                    int x = nums2[k2] < nums1[k1 + 1] ? nums2[k2] : nums1[k1+ 1];
                    return 0.5 * (nums1[k1] + x);
                }
            }
            else
            {
                if(k2 == size2 - 1)
                    return 0.5 * (nums1[k1] + nums2[k2]);
                else
                {
                    int x = nums1[k1] < nums2[k2 + 1] ? nums1[k1] : nums2[k2+ 1];
                    return 0.5 * (nums2[k2] + x);
                }
            }           
        }
        
    }
};