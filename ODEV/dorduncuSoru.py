import random
import time

dizi = [random.randint(0, 10000000) for i in range(1000)]

"""
Quick sort algoritmasinin T(n) gosterimi,
n elemanli bir dizinin siralanmasi icin harcanan zamanin matematiksel ifadesidir.
Bu ifade, pivot elemaninin secimine, dizinin boyutuna ve dizi elemanlarinin ozelliklerine baglidir.

Quick sort algoritmasinin O(n) tablosu, siralanacak verilerin boyutuna gore degisebilir.
Ancak, genel olarak Quick sort, O(n log n) karmasikligina sahiptir.
Bu karmasiklik, dizinin boyutuna gore logaritmik artis gosterir ve n elemanli bir dizi icin O(n log n) zaman alir.

Ornegin, bir dizinin boyutu 1000 olsun.
Quick sort, bu diziyi siralamak icin O(1000 log 1000) = O(1000 x 3) = O(3000) zaman alir.
Bu, büyük veri setleri icin oldukca hizli bir siralama algoritmasidir.

"""

def quick_sort(arr):
    if len(arr) <= 1: #islem degeri = 1
        return arr #islem degeri = 1
    else: #islem degeri = 1
        pivot = arr[0] #islem degeri = 1
        left = [] #islem degeri = 1
        right = [] #islem degeri = 1
        for i in range(1, len(arr)): #for dongusu n kere donecegi icin = n
            if arr[i] < pivot: #islem degeri = 1
                left.append(arr[i]) #islem degeri = 1
            else: #islem degeri = 1
                right.append(arr[i]) #islem degeri = 1
        return quick_sort(left) + [pivot] + quick_sort(right) # O(log n)

#Quick Sort'un ortalama zaman karmasikligi O(n*log n)'dir


"""
sonuc:
(quick sort)
Durum/Zaman Karmasikligi
Worst case O(n^2)
Average case O(n log n)
Best case O(n log n)

"""

def brute_force_sort(arr):
    for i in range(len(arr)): # dongu n kere tekrarlandigi icin islem degeri =  n
        for j in range(i+1, len(arr)): #T(n) = (n-1) + (n-2) + ... + 1 = n(n-1)/2
            if arr[j] < arr[i]: # islem degeri = 1
                arr[i], arr[j] = arr[j], arr[i] # islem degeri = 1
    return arr # islem degeri = 1
# O(n^2) zamana esdegerdir. Bu nedenle, bu algoritma buyuk boyutlu dizilerde verimli bir sekilde calismaz.
"""
sonuc:
(brute force)
Durum/Zaman Karmasikligi
Best Case	O(n)
Average Case	O(n^2)
Worst Case	O(n^2)
"""


def main():

    quick_sort_time_start = time.time()
    quick_sort(dizi)
    quick_sort_time_end = time.time()
    total_time_quick_sort = quick_sort_time_end - quick_sort_time_start
    print("\n")
    print("Quick sort calisma suresi -->", total_time_quick_sort)


    brute_force_sort_start = time.time()
    brute_force_sort(dizi)
    brute_force_sort_end = time.time()
    total_time_brute_force_sort = brute_force_sort_end - brute_force_sort_start
    print("Brute force sort calisma suresi -->", total_time_brute_force_sort)

"""
Debug log:

Quick sort calisma suresi --> 0.004514217376708984
Brute force sort calisma suresi --> 0.11291623115539551

"""