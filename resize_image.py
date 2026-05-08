import os
import cv2

# Dataset path
base_path = r"C:\Users\Anchal\OneDrive\Desktop\hog_SVM_project\dataset"

folders = ["human", "non_human"]

for folder in folders:

    folder_path = os.path.join(base_path, folder)

    print(f"\nProcessing Folder: {folder}")

    for file in os.listdir(folder_path):

        img_path = os.path.join(folder_path, file)

        img = cv2.imread(img_path)

        if img is None:
            print("Skipped:", file)
            continue

        resized = cv2.resize(img, (64, 128))

        cv2.imwrite(img_path, resized)

    print(f"✅ Finished resizing {folder}")

print("\n🎉 All images resized successfully!")