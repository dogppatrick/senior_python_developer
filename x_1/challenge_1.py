from itertools import combinations

class Phone(object):
    def __init__(self,price, camera_count, screen_size):
        self.price = price
        self.camera_count = camera_count
        self.screen_size = screen_size


class GooglePhone(Phone):
    def __init__(self, price=10, camera_count=3, screen_size=5):
        super().__init__(price, camera_count, screen_size)

    def special_freature(self, array):
        """
        輸入一個int list, 回傳偶數且大於10的元素，並由大至小進行排序
        例如: 輸入 [3, 43, 62, 15, 18, 22] 回傳 [62, 22, 18]
        """
        return sorted([n for n in array if n >10 and n%2 ==0],key=lambda x:-x)


class TaiwanPhone(Phone):
    def __init__(self, price=20, camera_count=1, screen_size=3):
        super().__init__(price, camera_count, screen_size)
    
    def special_freature(self, n):
        """
        輸入一個數字自動計算Fibonacci斐波那契數列的運算結果，並取最後二位
        並取最後二位(十位為 x、個位為 y)數字進行 p x 取 y (排序組合) 計算。
        例如: ---
        """
        def fibonacci(n):
            if n <=2:
                return 1
            else:
                return fibonacci(n-1) + fibonacci(n-2)
        tmp = [fibonacci(n) for n in range(1,n+1)]
        x = tmp[-1] // 10
        y = tmp[-1] % 10
        print(f'題意不明無法確定要從 fibonacci 做排列組合 還是要用最後的數字的十位與個位數字做計算')
        return len([c for c in combinations(range(x),y)])

if __name__ == "__main__":
    g1 = GooglePhone()
    g2 = TaiwanPhone()
    res = g1.special_freature([3, 43, 62, 15, 18, 22])
    # print(res, g1.price, g1.camera_count, g1.screen_size)
    res = g2.special_freature(7)
    # print(res, g2.price, g2.camera_count, g2.screen_size)