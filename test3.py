from datetime import date
def main():
    while True:
        print("QUẢN LÝ CHI TIÊU")
        print("1. Xem danh sách chi tiêu")
        print("2. Thêm khoản chi mới")
        print("3. Tính tổng tiền")
        print("4. Tìm chi tiêu theo ngày")
        print("5. Thoát")

        choice = input("Chọn chức năng (1-5): ")
        if choice == "1":
            show_expense()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            find_expense()
        elif choice == "5":
            print("Kết thúc chương trình")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng lại")    

def show_expense():
        try:
            with open("expense.txt", "r", encoding="utf-8") as file:
                expenses = file.readlines()
                if not expenses:
                    print("📚 Danh sách chi tiêu trống")
                    return
                print("📖 DANH SÁCH CHI TIÊU:")
                for i, e in enumerate(expenses, 1):
                    print(f"{i}. {e.strip()}")
        except:
            print("⚠️ Chưa có file expense.txt")
def add_expense():
    today = date.today() #lấy ngày 
    name = input("Nhập tên khoản chi: ")
    money = input("Nhập số tiền: ")

    with open("expense.txt", "a", encoding = "utf-8") as f:
        f.write(f'{today} | {name} | {money}')
    print("Đã thêm chi tiêu cho hôm nay")


def total_expense():
    total = 0
    with open("expense.txt", "r", encoding = "utf-8") as f:
        expenses = f.readlines()

        for i in expenses:
            if i.strip() == "":
                continue  #bỏ qua dòng trống

            parts = i.strip().split("|")#phân tách và bỏ khoảng cách
            money = parts[2].strip()
            total += int(money)
        print(f"Tổng chi tiêu: {total} VND")
            
def find_expense():
    date1 = input('nhập ngày (dd/mm/yyyy): ')
    with open("expense.txt", "r", encoding = "utf-8") as f:
        expenses = f.readlines()

        for i in expenses:
            if i.strip() == "":
                continue  #bỏ qua dòng trống

            parts = i.strip().split("|")#phân tách và bỏ khoảng cách
            print(parts)
            date2 = parts[0].strip()
            print(date2)
            if date1 == date2:
                print(i)

if __name__ == '__main__':
    main()