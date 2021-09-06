import praw

reddit = praw.Reddit(client_id = "qrxqoodVR64iLK9kq9BCzQ",
    client_secret="ZhJ1Wgi-KdQ8WpHCBVxE9C2J1HJl1A",
    user_agent = "EthicalBrandBot",
    username = "EthicalBrandBot" ,
    password = "@hAXTC99h+LsjE_<", 
    

)
brands = [
   "Abercrombie","Adidas","Amazon","Calvin Klein","FILA""Gap", "Old Navy", "Banana Republic", "Athleta","H&M","L.L. Bean","Lacoste","Nike",
    "Polo", "Ralph Lauren","Puma","Skechers","Tommy Hilfiger","UNIQLO","Victoria's Secret","Zara","Zegna"
]
print(reddit.read_only)
reddit.read_only = True
subreddit = reddit.subreddit("frugalmalefashion")

for sumbission in subreddit.hot(limit=25):
    if sumbission.title in brands:
        sumbission.reply("BTW this brand uses Uyghur Slave Labor ")
        f = open("data.txt","a")
        f.write(sumbission.url)
        f.close()