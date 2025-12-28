def main():
    while True:
        print("\nQUẢN LÝ SÁCH")
        print("1. Xem danh sách sách")
        print("2. Thêm sách mới")
        print("3. Đánh dấu sách đã đọc")
        print("4. Xóa sách")
        print("5. Tìm sách theo tên")
        print("6. Thoát")

        choice = input("Chọn chức năng (1-6): ")

        if choice == "1":
            show_book()
        elif choice == "2":
            add_book()
        elif choice == "3":
            mark_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            search_book()
        elif choice == "6":
            print("Thoát chương trình 👋")
            break
        else:
            print("Lựa chọn không hợp lệ!")


def show_book():
    try:
        with open("book.txt", "r", encoding="utf-8") as file:
            books = file.readlines()
            if not books:
                print("📚 Danh sách sách trống")
                return
            print("📖 DANH SÁCH SÁCH:")
            for i, book in enumerate(books, 1):
                print(f"{i}. {book.strip()}")
    except:
        print("⚠️ Chưa có file book.txt")


def add_book():
    book = input("Nhập tên sách: ")
    with open("book.txt", "a", encoding="utf-8") as file:
        file.write(f"[]{book}\n")
    print("➕ Đã thêm sách")


def mark_book():
    show_book()
    try:
        num = int(input("Nhập số sách đã đọc: "))
        with open("book.txt", "r", encoding="utf-8") as file:
            books = file.readlines()

        if 1 <= num <= len(books):
            books[num - 1] = books[num - 1].replace("[]", "[x]")
            with open("book.txt", "w", encoding="utf-8") as file:
                file.writelines(books)
            print("✅ Đã đánh dấu đã đọc")
        else:
            print("❌ Số không hợp lệ")
    except ValueError:
        print("❌ Phải nhập số")


def delete_book():
    show_book()
    try:
        num = int(input("Nhập số sách cần xóa: "))
        with open("book.txt", "r", encoding="utf-8") as file:
            books = file.readlines()

        if 1 <= num <= len(books):
            del books[num - 1]
            with open("book.txt", "w", encoding="utf-8") as file:
                file.writelines(books)
            print("🗑️ Đã xóa sách")
        else:
            print("❌ Số không hợp lệ")
    except ValueError:
        print("❌ Phải nhập số")


def search_book():
    keyword = input("Nhập tên sách cần tìm: ").lower()
    try:
        with open("book.txt", "r", encoding="utf-8") as file:
            books = file.readlines()

        found = False
        for book in books:
            if keyword in book.lower():
                print(book.strip())
                found = True

        if not found:
            print("🔍 Không tìm thấy sách")
    except:
        print("⚠️ Chưa có file book.txt")


if __name__ == "__main__":
    main()
