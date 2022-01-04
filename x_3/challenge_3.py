import random
import os
from glob import glob
from statistics import mean, median, multimode
import pandas as pd
class CsvHandler:
    def __init__(self):
        self.name_list = ['Chandler', 'Rubi', 'Marina', 'Riyad', 'Nawal'
                        , 'Celeste', 'Jonh', 'Rache', 'Alima', 'Amelia']
        self.exist_customer_mobile = set()
        self.check_ilovecoffee()

    def check_ilovecoffee(self):
        if '.\\ilovecoffee' not in glob("./*"):
            os.mkdir('./ilovecoffee')
            self.create_csv()

    def create_csv(self,count=500):
        result = []
        for i in range(count):
            customer_id = self.customer_id()
            customer_name = self.customer_name(customer_id)
            customer_mobile = self.customer_mobile()
            frequency = self.frequency()
            data = [customer_id, customer_name, customer_mobile, frequency]
            result.append(data)
        df = pd.DataFrame(result, columns=['customer_id', 'customer_name', 'customer_mobile', 'frequency'])
        df.to_csv("./ilovecoffee/customers.csv", encoding='utf-8', index=False)

    def random_str(self,wc):
        word = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxy'
        return "".join(word[random.randint(1,len(word)-1)] for i in range(wc))
    
    def random_str_int(self,wc):
        word = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxy0123456789'
        return "".join(word[random.randint(1,len(word)-1)] for i in range(wc))

    def random_name(self):
        return self.name_list[random.randint(1,len(self.name_list)-1)]

    def customer_id(self):
        return f'{self.random_str(1)}{self.random_str_int(7)}'

    def customer_name(self, customer_id):
        return f'{customer_id}.{self.random_name()}'

    def customer_mobile(self):
        def random_phonenumber():
            tmp = f'{random.randint(1,10**8-1):08d}'
            if tmp in self.exist_customer_mobile:
                return random_phonenumber()
            else:
                self.exist_customer_mobile.add(tmp)
                return tmp
        return f'+8869{random_phonenumber()}'
    
    def frequency(self):
        return random.randint(1,20)
    
    def calculate_csv(self):
        """並列印出 frequency 中數、眾數及平均數 (取至小數點後 5 位)"""
        df = pd.read_csv("./ilovecoffee/customers.csv")
        frequency = df['frequency']
        tmp = [f'{n:.5f}' for n in multimode(frequency)]
        print(f'中位數{median(frequency):.5f}, 眾數:{tmp}, 平均數:{mean(frequency):.5f}')
        
if __name__ == "__main__":
    c = CsvHandler()
    c.calculate_csv()
