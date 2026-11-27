import os
import random
from data_loader import load_sms_data, save_sms_data

random.seed(11) # để đảm bảo kết quả ngẫu nhiên giống nhau mỗi lần chạy

data = load_sms_data("data/processed/sms_clean.tsv")

ham_data = []
spam_data = []
for label, text in data:
    if label == "ham":
        ham_data.append((label, text))
    else:
        spam_data.append((label, text))

random.shuffle(ham_data) # xáo trộn trước khi chia để chọn mẫu ngẫu nhiên, tránh lệch theo thứ tự gốc
random.shuffle(spam_data)

ham_split = int(len(ham_data) * 0.7)
spam_split = int(len(spam_data) * 0.7)

train_data = ham_data[:ham_split] + spam_data[:spam_split]
test_data = ham_data[ham_split:] + spam_data[spam_split:]

random.shuffle(train_data) # trộn đều Ham và Spam xen kẽ với nhau sau khi ghép
random.shuffle(test_data)

os.makedirs("data/train", exist_ok=True)
os.makedirs("data/test", exist_ok=True)

save_sms_data(train_data, "data/train/train.tsv")
save_sms_data(test_data, "data/test/test.tsv")

print(f"Tổng: {len(data)}")
print(f"Train: {len(train_data)} (Ham: {ham_split}, Spam: {spam_split})")
print(f"Test : {len(test_data)} (Ham: {len(ham_data) - ham_split}, Spam: {len(spam_data) - spam_split})")