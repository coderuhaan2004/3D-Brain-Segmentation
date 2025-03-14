# FastSurferCNN Processing & Visualization with InVesalius  

This repository provides a streamlined workflow for **running FastSurferCNN** for brain MRI segmentation and **visualizing the results in InVesalius**.

## 📌 **Overview**  

- **FastSurferCNN**: A deep-learning-based tool for fast whole-brain segmentation of MRI scans.  
- **InVesalius**: A free, open-source software for 3D reconstruction of medical imaging data (DICOM/NIfTI).  

This guide walks through:  
👉 Running **FastSurferCNN** on an MRI scan  
👉 Converting the output into a **visualizable format**  
👉 Loading and analyzing the results in **InVesalius**  

## 🚀 **Installation**  

### **1️⃣ Clone this repository**  
```sh
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### **2️⃣ Install FastSurferCNN**  
```sh
git clone https://github.com/Deep-MI/FastSurfer.git
cd FastSurfer
pip install -r requirements.txt  # Install dependencies
```

### **3️⃣ Install InVesalius**  
Download and install InVesalius from:  
👉 [https://invesalius.github.io/download/](https://invesalius.github.io/download/)  

## 🏃 **Running FastSurferCNN on MRI Data**  

Make sure your input MRI scan is in **NIfTI format (.nii or .nii.gz)**.  

```sh
python FastSurferCNN.py --i input.nii.gz --o output_dir
```

### **Output Files (in `output_dir/`):**  
- `aseg.auto.mgz` → Segmentation mask  
- `mri_orig.mgz` → Processed input image  

💡 **Convert `.mgz` to `.nii.gz` for InVesalius compatibility:**  
```sh
mri_convert output_dir/aseg.auto.mgz output_dir/aseg.nii.gz
```

## 🔦 **Visualizing in InVesalius**  

1️⃣ Open **InVesalius**  
2️⃣ Click **"File" → "Import Medical Images"**  
3️⃣ Select **`aseg.nii.gz`**  
4️⃣ Adjust **opacity & color settings** for better visualization  

🟢 **Optional:** Overlay segmentation on original MRI  
- Load `mri_orig.nii.gz`  
- Set segmentation mask transparency  

## 🛠 **Troubleshooting**  

🛠 **FastSurferCNN not detecting GPU?**  
Try running on CPU:  
```sh
python FastSurferCNN.py --i input.nii.gz --o output_dir --no_cuda
```

🛠 **InVesalius not displaying segmentation?**  
- Ensure you converted `.mgz` to `.nii.gz`  
- Adjust **contrast & opacity** settings  

## 📜 **References**  

- [FastSurfer GitHub](https://github.com/Deep-MI/FastSurfer)  
- [InVesalius Official Website](https://invesalius.github.io/)  

## ✨ **Contributions & Issues**  

Feel free to **fork**, **submit PRs**, or report issues. 🚀  

