import os
import librosa
import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Paths
CSV_FILE = "dataset/esc50.csv"
AUDIO_DIR = "dataset/nature"
WOODCUT_DIR = "dataset/woodcutting"
MODEL_FILE = "woodcut_detector.pkl"

# Load ESC-50 data
df = pd.read_csv(CSV_FILE)[['filename', 'category']]

# Add woodcutting files
wood_files = [f for f in os.listdir(WOODCUT_DIR) if f.endswith(".wav")]
wood_df = pd.DataFrame({
    'filename': wood_files,
    'category': ['woodcutting'] * len(wood_files)
})
df = pd.concat([df, wood_df], ignore_index=True)

# Feature extraction
def extract_melspectrogram(file_path, n_mels=40, max_len=173):
    try:
        y, sr = librosa.load(file_path, sr=None)
        mel = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=n_mels)
        log_mel = librosa.power_to_db(mel, ref=np.max)

        # Fix length
        if log_mel.shape[1] < max_len:
            pad_width = max_len - log_mel.shape[1]
            log_mel = np.pad(log_mel, ((0,0),(0,pad_width)), mode='constant')
        else:
            log_mel = log_mel[:, :max_len]

        return log_mel.flatten()
    except Exception as e:
        print("Error:", file_path, e)
        return None

X, y = [], []
for _, row in df.iterrows():
    if row['category'] == 'woodcutting':
        file_path = os.path.join(WOODCUT_DIR, row['filename'])
    else:
        file_path = os.path.join(AUDIO_DIR, row['filename'])

    if os.path.exists(file_path):
        feat = extract_melspectrogram(file_path)
        if feat is not None:
            X.append(feat)
            y.append(row['category'])

X, y = np.array(X), np.array(y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train model
clf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
clf.fit(X_train, y_train)

# Evaluate
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

# Save trained model
with open(MODEL_FILE, "wb") as f:
    pickle.dump(clf, f)

print(f"✅ Model saved to {MODEL_FILE}")
