def login():
    u = input("Enter username: ")
    p = input("Enter password: ")

    if u == "admin" and p == "123":
        print("Login Successful")
        return True
    else:
        print("Invalid Login")
        return False


def create_post():
    title = input("Enter Title: ")
    desc = input("Enter Description: ")
    date = input("Enter Date: ")

    post = {"author": "admin", "title": title, "desc": desc, "date": date}
    return post


def view_post(posts):
    for i in posts:
        print("Author:", i["author"])
        print("Title:", i["title"])
        print("Date:", i["date"])
        print("Description:", i["desc"])
        print("----------------")


posts = []
login_status = False

while True:
    print("1.Login")
    print("2.Create Post")
    print("3.View Post")
    print("4.Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        login_status = login()

    elif ch == "2":
        if login_status:
            p = create_post()
            posts.append(p)
        else:
            print("Login First")

    elif ch == "3":
        view_post(posts)

    elif ch == "4":
        break