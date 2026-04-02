import shutil
import os

# 設定參數
source_file = 'image0.txt'  # 要複製的來源檔案
start_index = 2751          # 起始編號
num_copies = 23             # 要複製的份數

# 檢查來源檔案是否存在
if not os.path.exists(source_file):
    print(f"❌ 錯誤：找不到檔案 '{source_file}'，請確認它是否在當前目錄下！")
else:
    print(f"開始複製檔案，從 image{start_index}.txt 開始...")
    
    # 執行迴圈複製
    for i in range(num_copies):
        # 計算新的檔名 (例如 image2751.txt, image2752.txt...)
        new_filename = f'image{start_index + i}.txt'
        
        # 執行複製動作
        shutil.copy(source_file, new_filename)
        
    end_index = start_index + num_copies - 1
    print("\n" + "="*40)
    print(f"✅ 複製完成！")
    print(f"共產生了 {num_copies} 個檔案：自 {new_filename.replace(str(end_index), str(start_index))} 到 {new_filename}")
    print("="*40)