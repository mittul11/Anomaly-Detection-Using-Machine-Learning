# Anomaly-Detection-Using-Machine-Learning

The experiments were conducted in Google Collab, a cloud‐based Python environment to ensure reproducibility, scalability, and ease of sharing. The collab was configured using the T4 GPU runtime to accelerate computationally intensive deep learning tasks. 

The workflow followed the following steps:
Data Preprocessing: Raw sensor data from the eight Iot devices was transformed locally using a Python script (preprocessing.py. 
 Key steps included:
•	Timestamp conversion: Unix‐epoch values → UTC datetime.
•	Device selection: Retained only Device D, which exhibited the fewest missing intervals.
•	Missing‐value imputation: Applied forward‐fill (ffill) and backward fill (bfill)

The processed data frame in python was saved as final_data.parquet (Parquet format chosen for its efficiency in storing time-series data) and uploaded to a GitHub repository (link in appendix) for cloud access.

Collab Runtime Setup: 
Upon opening mittul_finalyearproj.ipynb in Google Colab, users should:

•	Select Runtime → Change runtime type
•	Choose T4 GPU under Hardware accelerator
•	Run the initial cells to install required Python packages and fetch final_data.parquet directly from GitHub

Core Software Stack 
•	pandas, numpy – for data manipulation
•	scikit-learn – for implementing Isolation Forest, One-Class SVM, and preprocessing
•	TensorFlow/Keras – for LSTM Autoencoder
•	Matplotlib, Seaborn, Plotly – for visualization
•	Nixtla’s TimeGPT API – for LLM-based time series modelling
•	Software:
– Python 3.11
– TensorFlow 2.8, scikitlearn 1.0, Pandas 1.3, NumPy 1.21
– JupyterLab for interactive experimentation
Version Control: Git was used for version control of code 
![image](https://github.com/user-attachments/assets/f502cc22-222b-40a5-a7ee-2af1b3bb75e5)
