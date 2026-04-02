import os

def remove_class_3_from_labels(label_dir):
    modified_files_count = 0
    removed_lines_count = 0

    print(f"開始掃描與清理資料夾: {label_dir} ...")

    # 走訪資料夾內所有檔案
    for filename in os.listdir(label_dir):
        # 只處理 txt 檔，並跳過 LabelImg 自動產生的 classes.txt
        if not filename.endswith('.txt') or filename == 'classes.txt':
            continue

        filepath = os.path.join(label_dir, filename)

        # 讀取檔案內的所有行
        with open(filepath, 'r') as f:
            lines = f.readlines()

        new_lines = []
        file_changed = False

        # 逐行檢查
        for line in lines:
            parts = line.strip().split()
            if not parts:
                continue

            # 檢查第一個字（類別 ID）是不是 '3'
            if parts[0] == '3':
                file_changed = True
                removed_lines_count += 1
            else:
                # 正常的標籤保留下來
                new_lines.append(line)

        # 如果檔案有被修改過（有發現 3 並剔除），就把新內容覆寫回去
        if file_changed:
            with open(filepath, 'w') as f:
                f.writelines(new_lines)
            modified_files_count += 1

    print("\n" + "="*30)
    print("✨ 清理完成！")
    print(f"總共修改了 {modified_files_count} 個檔案。")
    print(f"總共移除了 {removed_lines_count} 行不需要的標籤。")
    print("="*30)

# ================= 執行區塊 =================
# 請將這裡替換成妳放 txt 標籤檔的實際路徑
# 如果妳的標籤檔跟圖片都混在同一個資料夾，直接填那個資料夾路徑即可
LABEL_DIR = './' # 假設就在當前目錄執行

remove_class_3_from_labels(LABEL_DIR)