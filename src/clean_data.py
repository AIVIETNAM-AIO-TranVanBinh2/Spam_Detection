import os
from data_loader import load_sms_data, save_sms_data

raw_data = load_sms_data("data/raw/SMSSpamCollection")
clean_data = []
seen = set() # dùng set để lưu các tin nhắn đã gặp thay vì list để không phải duyệt toàn bộ danh sách mỗi lần kiểm tra trùng lặp
dup_ham = 0 
dup_spam = 0

for label, text in raw_data:
    if text in seen:
        if label == "ham":
            dup_ham += 1
        else:
            dup_spam += 1
    else:
        seen.add(text)
        clean_data.append((label, text))

os.makedirs("data/processed", exist_ok=True)
save_sms_data(clean_data, "data/processed/sms_clean.tsv")

print("Số dòng ban đầu:", len(raw_data))
print("Trùng lặp (Ham):", dup_ham)
print("Trùng lặp (Spam):", dup_spam)
print("Số dòng sạch còn lại:", len(clean_data))

