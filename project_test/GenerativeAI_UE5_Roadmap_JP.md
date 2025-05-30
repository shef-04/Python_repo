
# 学習ロードマップ  
## 生成AI／LLMエンジニアリング & リアルタイム3D（Unreal Engine 5）

### 目標
* **6か月** 以内に有料アセットを公開 / フリーランス案件を受注  
* 週あたり学習時間: **約20時間**（状況に応じて調整可）

---

## 0か月目 – 環境構築（Week 1）

| タスク | メモ |
|-------|------|
| 最新の **NVIDIA GPUドライバ** と **CUDA 12.x** をインストール | PyTorch & UE5 の GPU 機能に必須 |
| **Python 3.10+ venv** (`ai_env`) ＆ VS Code セットアップ | `python -m venv ai_env` |
| **PyTorch**, **Diffusers**, **ComfyUI** をインストール | `pip install torch torchvision diffusers` |
| **Epic Games** アカウント登録＆ **UE 5.4** インストール | 「Games → Third‑Person」テンプレプロジェクト |
| **GitHub + Git LFS** リポジトリ初期化 | LoRA 重み・テクスチャ・アセットを管理 |

---

## フェーズ1（Week 2‑8） — 基礎固め

### A. 生成AIトラック
| 週 | マイルストーン | 参考リソース |
|----|---------------|-------------|
| 2‑3 | Hugging Face **Diffusion Course** Unit 0‑4 完了 | <https://huggingface.co/learn/diffusion> |
| 4 | **Stable Diffusion XL** で txt2img → img2img をローカル実行 | |
| 5 | **ComfyUI** を導入し “SDXL → アップスケール” ワークフロー構築 | YouTube「ComfyUI Beginner 2025」 |
| 6 | 20枚の画像で **LoRA 微調整** を体験 | Kohya_ss または Diffusers PEFT |
| 7 | OpenAI API で **GPT‑4o mini** を呼び出し、プロンプト自動生成 | <https://platform.openai.com/docs> |
| 8 | 初の **MLOps スクリプト**: MLflow にチェックポイント保存 | 無料講座「MLOps Zoomcamp」 |

### B. リアルタイム3Dトラック
| 週 | マイルストーン | 参考リソース |
|----|----------------|-------------|
| 2 | **UE 5 Crash Course** を完走 | <https://learn.unrealengine.com> |
| 3 | **Movie Render Queue** で1分のウォークスルー動画をレンダリング | |
| 4‑6 | **Blender** で低ポリ小物を1日1個モデリング → UE にインポート | <https://www.blender.org> |
| 7 | **Lumen** ライティング & Nanite メッシュ導入 → FPS最適化 | |
| 8 | デモクリップを書き出し → YouTube 非公開アップロード | |

---

## フェーズ2（Week 9‑16） — 連携ミニプロジェクト

### 目的
AI生成テクスチャ＆看板で **夜景都市ビジュアライゼーション** を UE5 で制作。

| タスク | トラック |
|-------|---------|
| SDXL でサイバーパンク看板テクスチャを10個生成 | Gen AI |
| 日本語ネオンサインデータセットで LoRA を微調整 | Gen AI |
| テクスチャをインポートし、UE5 でマテリアルを作成 | 3D |
| カメラシーケンサー＆ポストプロセス Bloom を追加 | 3D |
| 30秒ショート動画を X / YouTube Shorts に公開 | 両方 |

---

## フェーズ3（Week 17‑24） — ポートフォリオ & 収益化

1. **アセット公開**  
   * LoRA / スタイルプリセット → Gumroad  
   * 3D プロップ → CGTrader / Sketchfab  

2. **ライブデモ & 案件応募**  
   * **HuggingFace Spaces** に GPT プロンプトヘルパーをデプロイ  
   * Lancers / CrowdWorks で案件検索（キーワード: “StableDiffusion LoRA”, “UE5 Visualization”）  

3. **（任意）認定資格**  
   * **NVIDIA DLI** – Generative AI with Diffusers  
   * **Coursera** – MLOps Specialization  

---

## 毎週ルーチンチェックリスト ✅

- **成果物または WIP を1件以上** SNS投稿（#WIP）  
- **Discord で質問／回答**（StableDiffusion JP, Unreal Slackers）  
- **技術日誌を10行** 記録（バグ、対処、コマンド）

---

## おすすめコミュニティ

* Discord » StableDiffusion JP / ComfyUI JP  
* Discord » Unreal Slackers  
* Reddit » r/MachineLearning, r/Blender  

---

## ハードウェア Tips

| パーツ | アドバイス |
|-------|-----------|
| GPU VRAM | RTX 4060 8 GB → SDXL 768×768 対応（xformers併用推奨） |
| ストレージ | NVMe SSD 1 TB: モデル & UE キャッシュ用 |
| メモリ | 32 GB: UE Lightmass ビルド時に余裕 |

---

## 付録 — よく使うコマンド

```bash
# venv 有効化
source ai_env/bin/activate  # (Windows) .\\ai_env\\Scripts\\activate

# ComfyUI インストール
git clone https://github.com/comfyui/comfyui.git
cd comfyui && pip install -r requirements.txt

# UE5 プロジェクト起動
"C:\\Program Files\\Epic Games\\UE_5.4\\Engine\\Binaries\\Win64\\UE5Editor.exe" MyProject.uproject
```

---

*Document generated by Navis — 2025年4月17日*
