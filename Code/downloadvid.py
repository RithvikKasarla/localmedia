import pytube

link = input("What is the link")
dire = input("What is the directory")

video = pytube.Youtube(link)

videos = video.get_videos

num = 1

for types in videos:
    print("{s} . {s}").format(num,types)
    num+=1

n = int(input("What format?")) -1

choice = videos[n]

choice.download('C:\Users\\' + dire + '\Desktop')

print("done")
