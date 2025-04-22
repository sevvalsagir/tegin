import os

# Klasör ve dosya yapısı
folders = [
    "data",
    "notebooks",
    "models",
    "utils",
    "app"
]

files = {
    "README.md": """# TEGİN

Radar Görüntüleri ile Hedef Sınıflandırması - Derin Öğrenme Projesi

## 🚀 Proje Hakkında
TEGİN, radar benzeri görüntülerden askeri hedef sınıflandırması yapabilen bir CNN modeli geliştirmeyi amaçlayan bir projedir. Proje, ASELSAN ve HAVELSAN gibi savunma sanayii firmalarının çalışma alanlarına yönelik olarak radar görüntüsü üzerinden otomatik hedef tanıma teknolojilerini keşfetmektedir.

## 🔍 Kullanılan Teknolojiler
- Python 3.x
- PyTorch / TensorFlow (isteğe bağlı)
- NumPy, Pandas
- Matplotlib / OpenCV
- Jupyter Notebook
- (Opsiyonel) Streamlit

## 📁 Klasör Yapısı
- data/
- notebooks/
- models/
- utils/
- app/

## 📈 Proje Durumu
🟡 Başlangıç aşamasında. Veri seti ile ilk analiz yapılacak.

## 📜 Lisans
MIT License.
""",

    "requirements.txt": """numpy
pandas
matplotlib
opencv-python
torch
torchvision
notebook
scikit-learn
streamlit
""",

    ".gitignore": """__pycache__/
*.pyc
*.pth
.ipynb_checkpoints/
models/
.env
*.h5
*.pth
""",

    "LICENSE": """MIT License

Copyright (c) 2025 [Adın]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
"""
}

# Klasörleri oluştur
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "README.md"), "w") as f:
        f.write(f"# {folder.capitalize()} klasörü")

# Dosyaları oluştur
for filename, content in files.items():
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

print("📁 Proje yapısı başarıyla oluşturuldu!")
