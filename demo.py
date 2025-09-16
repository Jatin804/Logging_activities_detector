import os
import pickle
import librosa
import numpy as np

# Load saved model
with open("woodcut_detector.pkl", "rb") as f:
    clf = pickle.load(f)

# Feature extractor (same as training)
def extract_melspectrogram(file_path, n_mels=40, max_len=173):
    try:
        y, sr = librosa.load(file_path, sr=None)
        mel = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=n_mels)
        log_mel = librosa.power_to_db(mel, ref=np.max)

        if log_mel.shape[1] < max_len:
            pad_width = max_len - log_mel.shape[1]
            log_mel = np.pad(log_mel, ((0,0),(0,pad_width)), mode='constant')
        else:
            log_mel = log_mel[:, :max_len]

        return log_mel.flatten()
    except Exception as e:
        print("Error:", file_path, e)
        return None

# Prediction function
def predict_audio(file_path):
    feat = extract_melspectrogram(file_path)
    if feat is not None:
        feat = feat.reshape(1, -1)
        return clf.predict(feat)[0]
    return None

# Example usage
test_file = "/home/jatin/Documents/PyCharm/Logging_activities_detector/dataset/nature/1-7456-A-13.wav"  # change to your test file
if os.path.exists(test_file):
    print("Prediction:", predict_audio(test_file))
else:
    print("❌ Test file not found:", test_file)
