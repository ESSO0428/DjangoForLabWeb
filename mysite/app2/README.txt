def degradome 為蝴蝶蘭降解組網站所用的 view
  template 用的是 OrchidWebTable.html
  對應的 url 寫在 urls.py 如下:
    path('V3deg/'                                   , views2.degradome)      ,
    path('V3deg/detail/'                            , views2.degradome)      ,
    path('V3deg/detail/deg_miRNA_seq/'              , views2.degradome)      ,
    分別為 :
      1. 主頁面
        主要列出每個 miRNA 對於其 target transcript 的剪切位點
      2. 跳轉的頁面 (呈現 T-plot)
        呈現感興趣的 transcript 的 miRNA 切位
          通過前一頁的 Transcript_ID link 可篩選感興趣的 transcript 有哪些切位 (T-plot 顯示的切位則為前面點的那個 row 的切位)
          通過前一頁的 Cleavage_Position link 可篩選感興趣的 transcript 和 切位的結果 (T-plot 顯示同上)
          通過前一頁的 miRNA_ID link 可篩選感興趣的 miRNA 對於 感興趣的 transcript 的所有切位的結果 (T-plot 顯示同上)
      3. 通過跳轉的頁面跳轉的頁面 (呈現 pre-miRNA)
        呈現感興趣的 miRNA 其對應的感興趣的 transcript 的所有切位
        並附上 pre-miRNA 的預覽

