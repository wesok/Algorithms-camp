## [十大经典排序](https://www.cnblogs.com/onepixel/articles/7674659.html)

## 一、按元素比较划分的排序算法    
### 1. 比较类排序：    
通过比较来决定元素间的相对次序，时间复杂度不能突破O(nlogn)，也称为非线性时间比较类排序        
（1）交换排序
- 冒泡排序     
- 快速排序         
   
（2）插入排序   
- 简单插入排序  
- 希尔排序      
     
（3）选择排序   
- 简单选择排序   
- 堆排序       
    
（4）归并排序   
- 二路归并 
- 多路归并    
  
 
### 2. 非比较类排序：   
通过比较来决定元素间的相对次序，突破时间限制，以线性时间运行，也称为线性时间非比较类排序      
- 计数排序
- 桶排序
- 基数排序  

## 二、按时间复杂度划分的排序算法       
### 1. 初级排序-O(n^2)     
（1）选择排序       
每次找最小值，

（2）插入排序      

（3）冒泡排序       

### 2. 高级排序-O(nlogn)     
（1）快速排序-递归思想         
数组取标杆pivot，小于pivot的元素放在其左侧，大于pivot的元素放在其右侧，然后依次对右边和右边的子数组继续快排          

**快排Java模板**    
```Java
public static void quickSort(int[] array, int begin, int end) {
    if (end <= start>)
        return;
    int pivot = partition(array, begin, end);
    quickSort(array, begin, pivot - 1);
    quickSort(array, begin, pivot + 1);
} 

static int partition(int[] a, int begin, int end) {
    int pivot = end, cnt = begin;
    for (int i = begin; i < end; i++) {
        if (a[i] < a[pivot]) {
            int temp = a[cnt]; a[cnt] = a[i]; a[i] = temp;
        }
    }
    int temp = a[pivot]; a[pivot] = a[cnt]; a[cnt] = temp;
    return cnt;
}
```

（2）归并排序-分治
- 把长度为n的输入序列分成两个长度为n/2的子序列
- 对这两个子序列分别采用归并排序
- 将两个排序好的子序列合并一个最终的排序序列       

```Java
public static void mergeSort(int[] array, int left, int right) {
    if (end <= start>)
        return;
    int mid = (left + right) / 2;
    mergeSort(array, left, mid);
    mergeSort(array, mid + 1, right);
    merge(array, left, mid, right);
}

public static void merge(int[] array, int left, int mid, int right) {
    int[] temp = new int[right - left + 1];
    int i = left, j = mid + 1, k = 0;

    while (i <= mid && j <= right) {
        temp[k++] = arr[i] <= arr[j] ? arr[i++] : arr[j++];
    }
    while (i < mid)
        temp[k++] = arr[i++];
    while (j <= right)
        temp[k++] = arr[j++];
    
    for (int p = 0; p < temp.length; p++) {
        arr[left + p] = temp[p];
    }

}

```


（3）堆排序 - 堆插入O(logn)，取最大/最小值O(1) 
- 数组元素依次建立小顶堆
- 依次取堆顶元素，并删除    

### 3. 特殊排序-O(n)    
（1）计数排序/Counting Sort       
要求输入数据必须具有确定范围的整数，将输入数据转化为键存储在额外开辟的数组空间，依次将计数大于1的填充回原数组       

（2）桶排序/Bucket Sort    
计数排序的升级版，假设输入数据服从均匀分布，将数据分到有限数量的桶里，每个桶再分别排序     

（3）基数排序/Radix Sort    






