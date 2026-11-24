import os

def load_sms_data(filepath):
    data = []
    with open(filepath, "r", encoding="utf-8") as f: # r là read, dùng utf-8 để đọc file text do raw data có ký tự đặc biệt £, ... 
        for line in f:
            line = line.strip()
            if line == "":
                continue
            label, text = line.split(sep="\t", maxsplit=1) # file raw là tsv -> dùng \t, raw gồm có 2 cột (k có header): label và text nên maxsplit = 1 chỉ tách lấy 2 phần đầu, phần còn lại là text
            data.append((label, text))
    return data

def save_sms_data(data, filepath):
    with open(filepath, "w", encoding="utf-8") as f: # dùng w là write để ghi dữ liệu SMS ra file tsv, mỗi dòng gồm label và text, dùng utf-8 để đảm bảo lưu các ký tự đặc biệt như £, ... 
        for label, text in data:
            f.write(f"{label}\t{text}\n")  # \t là tab, \n là xuống dòng

if __name__ == "__main__":
    data = load_sms_data("data/raw/SMSSpamCollection")
    print("Tổng số dòng:", len(data))
    print("3 dòng đầu:", data[:3])