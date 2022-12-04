import os
print('Welcome to Python Console Blog!')
blog = input('if you want to write blog then you press "w" and either you want to search blog then press "a": ')

if blog == "w":
    title = input("Enter Your Blog Tilte: ")
    desc = input("Enter Your Blog Description: ")
    add_blog = open(f"blog/{title}.txt", "w")
    add_blog.write(f"Title: {title}. Description: {desc}.")
    add_blog.close()
elif blog == "a":
    all_blog_list = []
    for root, dirs, files in os.walk('blog'):
        print("List of All Blogs is: ")
        for file in files:
            if file.endswith(f'.txt'):
                with open(os.path.join(root, file), 'r') as f:
                    text = f.read()
                    all_blog_list.append(text)
    print(all_blog_list)