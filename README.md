# 📊 Linear Regression Demo (CRISP-DM 教學版)

本專案是一個基於 **Streamlit + scikit-learn** 的線性迴歸互動式展示。  
使用者可以透過側邊欄調整參數，生成不同的模擬數據，並即時查看回歸結果與異常值 (Outliers)。  

---

## 🔍 CRISP-DM 教學流程

以下將依照 **CRISP-DM 六大步驟**，帶你一步一步完成線性迴歸專案。  

---

### 🟢 Step 1. Business Understanding（業務理解）
**Prompt：**  
我們要建立一個小型的互動系統，幫助初學者理解線性迴歸的概念。  

**過程：**  
- 線性迴歸模型： `y = ax + b + noise`  
- 目標：讓使用者能調整 `a`、`noise`、資料點數量，觀察對結果的影響。  
- 展示：用回歸直線擬合資料，並找出「離群值 (outliers)」。  

---

### 🟢 Step 2. Data Understanding（資料理解）
**Prompt：**  
我們沒有真實資料，要自己用數學公式生成資料。  

**過程：**  
- `X`：隨機產生在 `[0,10]` 區間的數字  
- `y`：依公式 `y = ax + b + noise` 生成  
- `noise`：加入高斯雜訊 (Gaussian noise)，模擬真實世界的不確定性  

📌 **觀察**：噪音越大，資料點分布越分散；噪音越小，資料點越貼近直線。  

---

### 🟢 Step 3. Data Preparation（資料準備）
**Prompt：**  
在建模之前，資料要轉成合適的格式。  

**過程：**  
- 使用 **NumPy** 建立 X 與 y 的陣列  
- 使用 **Pandas** 整理成 DataFrame，方便分析與找離群值  

---

### 🟢 Step 4. Modeling（建模）
**Prompt：**  
用 scikit-learn 訓練線性迴歸模型。  

**過程：**  
- 匯入 `LinearRegression`  
- 呼叫 `fit(X, y)` 來訓練模型  
- 獲得模型參數：  
  - **係數 (a_hat)** → 預測斜率  
  - **截距 (b_hat)** → 預測截距  
- 繪製「散點圖 + 回歸直線」  

---

### 🟢 Step 5. Evaluation（評估）
**Prompt：**  
模型的表現如何？有哪些資料點不符合模型？  

**過程：**  
- 計算 **殘差 (residuals)** = `y - y_pred`  
- 找出 **Top 5 離群值 (Outliers)**（依照殘差絕對值排序）  
- 評估指標（可選）：  
  - R²  
  - MSE  

📌 **觀察**：噪音越大 → R² 下降，離群值越多。  

---

### 🟢 Step 6. Deployment（部署）
**Prompt：**  
怎麼讓這個模型方便給其他人互動使用？  

**過程：**  
- 使用 **Streamlit** 建立 Web App：  
  - 左側 Sidebar：調整 `a`、`n`、`noise`  
  - 右側主畫面：顯示圖表 + 模型結果  
- 部署選項：  
  - **本地端**：`streamlit run app.py`  
  - **雲端**：Streamlit Cloud / Heroku / Render / Vercel  

---

## 📦 安裝環境

```bash
pip install -r requirements.txt
