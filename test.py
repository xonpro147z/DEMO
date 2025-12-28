    
def main():
    while True:
        print("TO DO LIST")
        print("1. Xem danh sách")
        print("2. Thêm công việc mới")
        print("3. Đánh dấu hoàn thành")
        print("4. Xóa công việc")
        print("5. Thoát")

        choice = input("Chọn chức năng (1-5): ")
        if choice == "1":
            show_task()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Kết thúc chương trình")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng lại")    

def show_task():
    try:
        with open('task.txt', "r", encoding ='utf-8') as file:
            tasks = file.readlines()
            if not tasks:
                print("DANH SÁCH CÔNG VIỆC TRỐNG")
                return
            print("DANH SÁCH CÔNG VIỆC:")
            for i, tasks in enumerate(tasks, 1):
                print(f"{i}.{tasks.strip()}")
    except:
        print("không tìm thấy file task")
    

def add_task():
    task = input("Nhập công việc mới...")
    with open("task.txt", "a", encoding = "utf-8") as file:
        file.write(f"[]{task}\n")
        print("đã thêm công việc")
def mark_task():
    show_task()
    try:
        task_num = int(input("Nhập số thứ tự công việc: "))
        with open("task.txt", "r", encoding ="utf-8")as file:
            tasks = file.readlines()
        if 1 <= task_num <= len(tasks):
            tasks[task_num -1] = tasks[task_num -1].replace("[]", "[x]")
            with open("task.txt", "w", encoding ="utf-8")as file: 
                file.writelines(tasks)
                print("đã đánh dấu hoàn thành")
        else:
            print("số thứ tự không hợp lệ")
    except ValueError:
        print("Yêu cầu nhập số")
        
def delete_task():    
    show_task()
    try:
        task_num = int(input("Nhập số thứ tự công việc cần xóa: "))
        with open("task.txt", "r", encoding ="utf-8")as file:
            tasks = file.readlines()

        if 1 <= task_num <= len(tasks):
            del tasks[task_num-1]
            with open("task.txt", "w", encoding ="utf-8")as file: 
                file.writelines(tasks)
                print("Đã xóa công việc")
        else:
            print("số thứ tự không hợp lệ")
    except ValueError:
        print("Yêu cầu nhập số")
if __name__ == "__main__":
    main()