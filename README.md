# 📊 Linear Regression Demo (CRISP-DM)

本專案是一個基於 **Streamlit + scikit-learn** 的線性迴歸互動式展示。  
使用者可以透過側邊欄調整參數，生成不同的模擬數據，並即時查看回歸結果與異常值 (Outliers)。  

## 🔍 功能特色
- 使用 **CRISP-DM 流程** 展示線性迴歸模型：
  1. **Business Understanding**：展示迴歸模型與資料特徵的關聯  
  2. **Data Understanding**：由使用者生成資料 (y = ax + b + noise)  
  3. **Data Preparation**：整理成 NumPy / Pandas 格式  
  4. **Modeling**：使用 `sklearn.linear_model.LinearRegression`  
  5. **Evaluation**：顯示係數、截距、殘差與 R²  
  6. **Deployment**：透過 **Streamlit** 提供互動式介面  
- 可調整參數：
  - 資料點數量 (n)  
  - 斜率 a  
  - 噪音變異數 (Noise Variance)  
- 自動繪製：
  - 散點圖 (data points)  
  - 回歸線 (regression line)  
  - 標記 Top 5 Outliers  
- 表格顯示 **前 5 筆離群值** (含 x, y, residuals)  

---

## 📦 安裝環境

請先安裝 Python 3.8+，再安裝所需套件：

```bash
pip install -r requirements.txt
