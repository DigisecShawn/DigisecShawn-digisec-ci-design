# DIGISEC CI Design Repository

DIGISEC 品牌識別（Corporate Identity, CI）資產集中管理倉庫。

本 repo 用於保存、版本化、查找與驗證 DIGISEC 品牌設計資產，包含英文標誌、中文標誌、中英組合標誌、輔助圖形、AI 原始檔，以及基本品牌 token。

## Repo 結構

```text
.
├── assets/
│   └── logo/
│       ├── png/          # 可直接使用的 PNG 品牌圖檔
│       └── source/       # AI 原始設計檔
├── brand/                # 品牌色彩與基本 token
├── docs/                 # 使用規範、資產清單
├── scripts/              # CI 檢查腳本
└── .github/workflows/    # GitHub Actions
```

## 快速使用

| 用途 | 建議檔案 |
|---|---|
| 淺色背景英文 Logo | `assets/logo/png/logo-eng-black.png` |
| 深色背景英文 Logo | `assets/logo/png/logo-eng-white.png` |
| 中文 Logo | `assets/logo/png/logo-ch-black.png` |
| 中英組合 Logo | `assets/logo/png/logo-ch-en-black.png` |
| 橘色輔助圖形 / icon | `assets/logo/png/auxiliary-mark-orange.png` |
| 灰色輔助視覺 | `assets/logo/png/auxiliary-logo-gray.png` |
| 印刷 / 編輯用向量原始檔 | `assets/logo/source/*.ai` |

## 品牌使用原則

1. 不得任意拉伸、壓縮、旋轉 Logo。
2. 不得任意更改 Logo 顏色；需新增版本時，應從 AI 原始檔輸出。
3. Logo 與其他元素之間應保留安全距離。
4. 對外公開文件優先使用 `logo-ch-en-black.png` 或 `logo-eng-black.png`。
5. 印刷品、招牌、大尺寸輸出需優先使用 `assets/logo/source/` 內的 AI 檔。

## CI 檢查

此 repo 內建 GitHub Actions：

- 檢查必要品牌資產是否存在。
- 檢查 PNG 是否可被讀取。
- 輸出資產尺寸清單，方便審查。

本機可執行：

```bash
python scripts/validate_assets.py
```

## 維護流程

新增或替換品牌圖檔時：

1. 放入對應資料夾。
2. 更新 `docs/asset-inventory.md`。
3. 執行 `python scripts/validate_assets.py`。
4. 以 Pull Request 方式提交，方便保留審核紀錄。
