# Vehicle-Insurance-Domain-Project



## 🚗 Vehicle Project Setup Guide

Follow this step-by-step guide to set up your Python project environment, connect to MongoDB Atlas, and prepare your data pipeline.

---

## ✅ Step 1: Initialize Project Structure

- Run `template.py` to create the initial folder structure for your project.

---

## ✅ Step 2: Configure Local Package Import

- Create and update `setup.py` and `pyproject.toml` to support local imports.
- Refer to `crashcourse.txt` for more details.

---

## ✅ Step 3: Create and Activate Virtual Environment

```bash
conda create --name vehicle_proj python=3.12 -y
conda activate vehicle_proj
```

---

## ✅ Step 4: Add and Install Requirements

1. Add required packages to `requirements.txt`.
2. Install all packages:
```bash
pip install -r requirements.txt
```
3. Verify installations:
```bash
pip list
```

---

## ✅ Step 5: Setup MongoDB Atlas Account

1. Sign up at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).
2. Create a new project (just provide a name and proceed).

---

## ✅ Step 6: Create a Free Cluster

1. Click **Create Cluster**.
2. Select **M0 (Free Tier)**.
3. Keep default settings and click **Create Deployment**.

---

## ✅ Step 7: Setup Database User

- Create a **DB user** with a **username** and **password**.
- Save these credentials securely.

---

## ✅ Step 8: Configure Network Access

- Go to **Network Access**.
- Add IP address `0.0.0.0/0` to allow access from anywhere.

---

## ✅ Step 9: Get MongoDB Connection String

1. Go to **Database** → **Connect** → **Drivers**.
2. Choose:
   - **Driver:** Python
   - **Version:** 3.6 or later
3. Copy and save the connection string.
4. Replace `<password>` with your actual password.

---

## ✅ Step 10: Create Notebook Folder and Push Dataset

1. Create a folder named `notebook`.
2. Add your dataset files inside.
3. Create a notebook `mongoDB_demo.ipynb`.
4. Set kernel: `Python Kernel → vehicle_proj`.

---

## ✅ Step 11: Upload Data to MongoDB

- Write Python code in your notebook to insert data into MongoDB.
- Use the connection string from Step 9.

---

## ✅ Step 12: Verify Data in MongoDB Atlas

- Go to **Database** → **Browse Collections**.
- Check your uploaded data in key-value format.

---

## ✅ Step 13: Setup Logging

- Create a logger module.
- Test logging using `demo.py`.

---

## ✅ Step 14: Setup Exception Handling

- Create an exception module.
- Test exception handling in `demo.py`.

---

## ✅ Step 15: Add EDA and Feature Engineering

- Add relevant notebooks in the `notebook/` folder.

---

## ✅ Step 16: Data Ingestion Setup

1. Add constants to `constants/__init__.py`.
2. Define MongoDB connection in `configuration/mongo_db_connections.py`.

---

## ✅ Step 17: Database Access Layer

1. In `data_access/proj1_data.py`, fetch and convert DB data to pandas DataFrame.
2. Use connection logic from `mongo_db_connections.py`.

---

## ✅ Step 18: Define Entities

- In `entity/config_entity.py`: Create `DataIngestionConfig` class.
- In `entity/artifact_entity.py`: Create `DataIngestionArtifact` class.

---

## ✅ Step 19: Create Data Ingestion Component

- Write the ingestion logic in `components/data_ingestion.py`.

---

## ✅ Step 20: Add Training Pipeline

- Call data ingestion logic from the pipeline.
- Run using `demo.py`.

---

## ✅ Step 21: Set MongoDB URL as Environment Variable

### For Bash (Linux/macOS):

```bash
export MONGODB_URL="mongodb+srv://<username>:<password>@cluster.mongodb.net/myDatabase"
echo $MONGODB_URL
```

### For PowerShell (Windows):

```powershell
$env:MONGODB_URL = "mongodb+srv://<username>:<password>@cluster.mongodb.net/myDatabase"
echo $env:MONGODB_URL
```

### For Windows GUI:

- Go to **System Properties → Environment Variables**.
- Add a new user variable:
  - Name: `MONGODB_URL`
  - Value: your MongoDB connection string

---

## ✅ Step 22: Git Ignore Settings

- Add `artifact/` directory to `.gitignore`.

---

🎉 **Done!** You’re now ready to build and run your vehicle data pipeline project!

