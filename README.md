# Python / Django Developer Interview

Hi,

感謝您，若您決定要開始這項挑戰，請 fork 此專案，並將每個問題的答案放至對應的資料夾

完成後，請 PR 到此專案

大約會花費 3- 5 小時的挑戰時間


### 挑戰一: 實作出 2 隻手機 (folder: x_1)

> 現在您的手上有 2 支手機，手機來自不同品牌，其規格屬性大同小異，但各自擁有一項特殊功能，請設計出這 2 支手機的 class，並完成其特殊功能。

```
手機共通屬性: price, camera_count, screen_size
特殊功能: special_freature() 

手機一 google phone:
price=10, camera_count=3, screen_size=5
special_freature 輸入一個int list, 回傳偶數且大於10的元素，並由大至小進行排序
例如: 輸入 [3, 43, 62, 15, 18, 22] 回傳 [62, 22, 18]

手機二 taiwan phone:
price=20, camera_count=1, screen_size=3
special_freature
輸入一個數字自動計算Fibonacci斐波那契數列的運算結果，並取最後二位(十位為 x、個位為 y)數字進行 p x 取 y (排序組合) 計算。
例如: ---

```


### 挑戰二: Django 實作  (folder: x_2)


1) 使用 pip 將你安裝的所有 python 模組及其版本變成一個 requirement 檔案
2) 將 Django 後台路徑從 /admin 修改成 /superadmin 
3) 新增一個 django app "ilovecoffee", 並於 settings.py 啟用它
4) 在 ilovecoffee 中，新增 models.py 檔 ，並創建一個 coffee 資料表，欄位有 name, bean_from, price
5) 在當前的虛擬環境中使用 python manage.py shell，並將 Coffee import 進來，將結果截圖放至此資料夾，取名為 coffee.jpg



### 挑戰三: 資料操作 (folder: x_3)
> 請設計一個 CsvHanlder class，當它被初始化時，會偵測相同目錄下是否存在一個 ilovecoffee 資料夾，若無則建立，有則略過。賦予此 class 一個 create_csv() method, 當被呼叫時，會隨機寫入 500 筆客戶資料至 /ilovecoffee/customers.csv，結構如下:
```
customer_id,customer_name, customer_mobile, frequency
"y88xTa", "tom.y88xTa","+886938766119", "4"
"uYt49x", "peter.uYt49x","+886938922440", "6"
"p9g5As", "hank.p9g5As","+886918300227", "1"
.....
````

##### customer_id:
長度8, 由數字[0-9], 大寫[A-Z]，小寫[a-z]隨機組成，但開頭不可為數字

##### customer_name: 
隨意用10個英文名字建立一組list: 如 ['tom','peter','hank'....]
將customer_id與隨機從 name list 中取出的一個元素進行合併，例如產出"tom.y88xTa"

##### customer_mobile
隨機產生一個+886開頭的台灣電話號碼，若新產出的電話號碼有重複，則需要重新產生

##### frequency
從 [0-20] 中隨機進行選擇

>
> 賦予此 class 一個 calculate_csv() method, 當被呼叫時，會讀取 /ilovecoffee/customers.csv，並列印出 frequency 中數、眾數及平均數 (取至小數點後 5 位)
>


### 最後，請在您的最後一次 commit 中輸入您對此份工作，在程式上的期待
### 並於 PR 中針對以下題目提出您的看法，謝謝您。

身為一位專業開發者 ，現在是周一早上 10 點，請問以下工作項目，您會如何安排一周的工作次序

例如:
CDEFBA
原因為: .............

(A) 重量級客戶10天前提出的改進需求，需耗時6小時完成，此需求評估為非常實用。
(B) 昨天晚上系統發出的 alert, 警示訊息為客戶操作出錯
(C) 早上 9 點系統發出的 alert, 警示訊息為 DB 連線異常
(D) 正在開發中的功能，你發現 PM 規劃的架構圖可能會有嚴重瑕疵
(E) 近三天專注開發的一項功能，如果現在不接著工作，很可能會忘記重要事項
(F) 這周預計完成的某項功能，上周已被順手處理掉，可向 PM 進行回報

