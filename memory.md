# DIGISEC CI Design Repo 執行記錄

本文件記錄 DIGISEC CI Design Repository 的建立、上傳與後續大型設計檔處理流程，作為日後維護與交接依據。

## 1. GitHub Repository

| 項目 | 內容 |
|---|---|
| Repository | `DigisecShawn/DigisecShawn-digisec-ci-design` |
| URL | <https://github.com/DigisecShawn/DigisecShawn-digisec-ci-design> |
| Default branch | `main` |
| 用途 | DIGISEC 品牌識別、Logo、AI 原始檔、品牌 token、使用規範與 CI 檢查集中管理 |

## 2. Repo 結構

```text
.
├── assets/
│   └── logo/
│       ├── png/
│       └── source/
├── brand/
│   ├── tokens.css
│   └── tokens.json
├── docs/
│   ├── asset-inventory.md
│   └── usage-guidelines.md
├── scripts/
│   └── validate_assets.py
├── .github/
│   └── workflows/
│       └── asset-check.yml
├── .gitignore
├── LICENSE.md
├── README.md
└── memory.md
```

## 3. 已上傳的文字檔案

| 檔案 | 狀態 | 用途 |
|---|---|---|
| `README.md` | 已上傳 | Repo 說明、結構與使用方式 |
| `brand/tokens.css` | 已上傳 | CSS 品牌色 token |
| `brand/tokens.json` | 已上傳 | JSON 品牌色與 Logo 路徑 token |
| `docs/asset-inventory.md` | 已上傳 | 品牌資產清單 |
| `docs/usage-guidelines.md` | 已上傳 | Logo 使用規範 |
| `scripts/validate_assets.py` | 已上傳 | 品牌資產檢查腳本 |
| `.github/workflows/asset-check.yml` | 已上傳 | GitHub Actions CI 檢查流程 |
| `.gitignore` | 已上傳 | 忽略系統與暫存檔 |
| `LICENSE.md` | 已上傳 | DIGISEC 品牌資產使用限制 |
| `memory.md` | 已上傳 | 本執行記錄 |

## 4. 二進位資產處理

PNG Logo 可直接放進 Git repository。AI、PSD、PDF、ZIP 等大型或設計原始檔，使用 Git LFS 管理。

本 repo 已設定 Git LFS tracking：

```text
*.ai filter=lfs diff=lfs merge=lfs -text
*.psd filter=lfs diff=lfs merge=lfs -text
*.pdf filter=lfs diff=lfs merge=lfs -text
*.zip filter=lfs diff=lfs merge=lfs -text
```

備份用 ZIP 不建議直接放入 repo，建議改放 GitHub Release 或內部雲端儲存。

## 5. 本機補上 assets 的流程

```bash
git clone https://github.com/DigisecShawn/DigisecShawn-digisec-ci-design.git
cd DigisecShawn-digisec-ci-design
git lfs install
git lfs track "*.ai"
git lfs track "*.psd"
git lfs track "*.pdf"
git lfs track "*.zip"
cp -R ../digisec-ci-design-repo/assets .
python scripts/validate_assets.py
git add .
git commit -m "feat: add DIGISEC logo assets with Git LFS"
git push origin main
```

## 6. CI 檢查方式

本機檢查：

```bash
python scripts/validate_assets.py
```

GitHub Actions：

<https://github.com/DigisecShawn/DigisecShawn-digisec-ci-design/actions>

Workflow 名稱：`DIGISEC Brand Asset Check`

通過條件：

- 必要 PNG 檔案存在。
- 必要 AI 原始檔存在。
- PNG 可被 Python Pillow 正常讀取。
- 腳本未回報 missing 或 invalid。

## 7. 常見問題

### push 被拒絕，提示檔案超過 100 MB

大型 AI 檔可能沒有被 Git LFS 接管。確認 `.gitattributes` 是否存在，並重新加入大型檔案：

```bash
git lfs track "*.ai"
git add .gitattributes
git add assets/logo/source/*.ai
git commit -m "chore: track AI files with Git LFS"
git push origin main
```

如果大型檔案已經被一般 Git commit 過，需要清除歷史或重新 clone 後再操作。

### CI 顯示缺少 assets

確認檔案是否位於：

```text
assets/logo/png/
assets/logo/source/
```

並檢查檔名是否符合 `docs/asset-inventory.md` 與 `scripts/validate_assets.py`。

### 沒有 Git LFS 指令

安裝 Git LFS 後重新執行：

```bash
git lfs install
```

## 8. 後續維護原則

- 新增 Logo 或改版時，先更新 `assets/`。
- 同步更新 `docs/asset-inventory.md`。
- 若新增品牌色，更新 `brand/tokens.css` 與 `brand/tokens.json`。
- 執行 `python scripts/validate_assets.py`。
- 使用 Pull Request 合併，保留審查紀錄。
- AI、PSD、PDF、ZIP 等大型或設計原始檔一律使用 Git LFS。
