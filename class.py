class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(self.name)
        print(self.username)

you = Member('이수연 매니저님','진용님','원욱')
you1 = Member('이수연 매니저님1','진용님1','원욱1')
you2 = Member('이수연 매니저님2','진용님2','원욱2')

you.display()
you1.display()
you2.display()

asd_list = []
asd_list.append(you)
asd_list.append(you1)
asd_list.append(you2)

for Member in asd_list:
    print(Member.name)
    print(Member.username)
class Post:
    def __init__(self,title,content,author):
        self.title = title
        self.content = content
        self.author = author

me1 = Post('황1','원1','욱1')
me2 = Post('황2','원2','욱2')
me3 = Post('황3','원3','욱3')
me4 = Post('황4','원4','욱4')
me5 = Post('황5','원5','욱5')
me6 = Post('황6','원6','욱6')
me7 = Post('황7','원7','욱7')
me8 = Post('황8','원8','욱8')
me9 = Post('황9','원9','욱9')

posts = []
for post in posts:
    if post.author == '진용님':
        print(post.title)





