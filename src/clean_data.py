import os
from data_loader import load_sms_data, save_sms_data

replacements = {
    "\x91": "'",
    "\x92": "'",
    "\x93": '"',
    "\x94": '"',
    "\x96": "-",
    "‘": "'",
    "’": "'",
    "“": '"',
    "”": '"',
    "–": "-",
    "—": "-",
    "…": "...",
}

junk_symbols = ["»", "¡", "鈥", "┾", "〨"]

raw_data = load_sms_data("data/raw/SMSSpamCollection")
clean_data = []
seen = set() # dùng set để lưu các tin nhắn đã gặp thay vì list để không phải duyệt toàn bộ danh sách mỗi lần kiểm tra trùng lặp
dup_ham = 0 
dup_spam = 0
normalized_count = 0

def normalize_text(text):
    for old, new in replacements.items():
        text = text.replace(old, new)
    for sym in junk_symbols:
        text = text.replace(sym, "")
    return text.strip()

for label, text in raw_data:
    norm_text = normalize_text(text)
    if norm_text != text:
        normalized_count += 1

    if norm_text in seen:
        if label == "ham":
            dup_ham += 1
        else:
            dup_spam += 1
    else:
        seen.add(norm_text)
        clean_data.append((label, norm_text))

os.makedirs("data/processed", exist_ok=True)
save_sms_data(clean_data, "data/processed/sms_clean.tsv")

print("Số dòng ban đầu:", len(raw_data))
print("Số dòng được chuẩn hóa:", normalized_count)
print("Trùng lặp (Ham):", dup_ham)
print("Trùng lặp (Spam):", dup_spam)
print("Số dòng sạch còn lại:", len(clean_data))


