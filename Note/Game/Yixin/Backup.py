import shutil
from pathlib import Path

# 定義來源與目標路徑
src_dir = Path(r"D:\Yixin")
dest_dir = Path(r"D:\Desktop\Profile\Note\Game\Yixin")

# 確保目標資料夾存在（若不存在則自動建立）
dest_dir.mkdir(parents=True, exist_ok=True)

# 檢查來源資料夾是否存在
if not src_dir.exists():
  print(f"錯誤：來源資料夾不存在 ({src_dir})")
else:
  # 僅搜尋第一層底下的 .sav 檔案（不遞迴搜尋子資料夾）
  sav_files = [p for p in src_dir.glob("*.sav") if p.is_file()]

  if not sav_files:
    print("在 D:\Yixin 第一層找不到任何 .sav 檔案。")
  else:
    for file_path in sav_files:
      dest_path = dest_dir / file_path.name
      # 使用 copy2 保留檔案的 metadata（如修改時間）
      shutil.copy2(file_path, dest_path)
      print(f"已複製: {file_path.name}")

    print(f"\n完成！共複製 {len(sav_files)} 個檔案。")