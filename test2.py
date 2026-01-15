import webbrowser
import tkinter as tk
from tkinter import ttk
import json
import os

LINKS_FILE = "links.json"

def load_links():
    if os.path.exists(LINKS_FILE):
        with open(LINKS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {
        "url_to_open": "https://www.tiktok.com/@genshi076/video/7591475044719594773?is_from_webapp=1&sender_device=pc",
        "url_open": "https://www.tiktok.com/@2jz.exp/video/7561744014039469330?is_from_webapp=1&sender_device=pc",
        "link": "https://www.tiktok.com/@fwzakkuu/video/7566299797443890453",
        "idk": "https://www.tiktok.com/@kkallelout/video/7549555580386446610",
        "dark_triad": "https://www.tiktok.com/@.switch.1337/video/7554627596537875732",
        "my_demons": "https://www.tiktok.com/@natsuyaxq/video/7430111748738288902",
        "faded": "https://www.tiktok.com/@garikblond/video/7496934177011535120",
        "za_warudo": "https://www.tiktok.com/@pregnanthippo308/video/7552193233556753686",
        "smokeitoff": "https://www.tiktok.com/@eddyog.ae/video/7458706544859958571",
        "sugarcrush": "https://www.tiktok.com/@_rillzzz_/video/7511712033042189573",
        "betterthanyou": "https://www.tiktok.com/@matti_mip/video/7398145053635497248",
        "coe": "https://www.tiktok.com/@1kaisen_0/video/7522450102850424069",
        "courtesycall": "https://www.tiktok.com/@tenko38/video/7514062650263964984",
        "reinhard": "https://www.tiktok.com/@toxicghoul228/video/7527708894404021509",
        "mamasboy": "https://www.tiktok.com/@sabersongs.2/video/7378115411792989473",
        "hackerroblox": "https://www.tiktok.com/@aan27coco07/video/7394332506415238401",
        "unkwnsng": "https://www.tiktok.com/@fearlessgamerpro000/video/7364482259413503248",
        "rezerogmfu": "https://www.tiktok.com/@ev1l_ae/video/7269844190094265633",
        "mistymemory": "https://www.tiktok.com/@reffmc/video/7285238491309526278",
        "scpfoundation": "https://www.tiktok.com/@modestoring/video/7275104649579891974",
        "hysteria": "https://www.tiktok.com/@dash_cool2131/video/7247743238046616837",
        "boomboomboom": "https://www.tiktok.com/@ukrainemaper0/video/7247091154582392070",
        "ifyoulovemetemein": "https://www.tiktok.com/@quatravfx/video/7236741137371860229",
        "onetruth": "https://www.tiktok.com/@excelfaithfully/video/7211957327728069931",
        "bankomat": "https://www.tiktok.com/@skyexqbeats/video/7498734670671138070",
        "discordics": "https://www.tiktok.com/@edut_17/video/7521254472270597394",
    }

links = load_links()

def save_links():
    with open(LINKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(links, f, ensure_ascii=False, indent=2)

class LinkOpener:
    def __init__(self, root):
        self.root = root
        self.root.title("link test")
        self.root.geometry("500x600")
        
        title = tk.Label(root, text="Выберите ссылки для открытия", font=("Arial", 12, "bold"))
        title.pack(pady=10)
        
        add_frame = ttk.Frame(root)
        add_frame.pack(pady=10, padx=10, fill=tk.X)
        
        tk.Label(add_frame, text="Название:").pack(side=tk.LEFT, padx=5)
        self.name_entry = tk.Entry(add_frame, width=15)
        self.name_entry.pack(side=tk.LEFT, padx=5)
        
        tk.Label(add_frame, text="Ссылка:").pack(side=tk.LEFT, padx=5)
        self.url_entry = tk.Entry(add_frame, width=25)
        self.url_entry.pack(side=tk.LEFT, padx=5)
        
        add_btn = tk.Button(add_frame, text="Добавить", command=self.add_link, bg="#2196F3", fg="white")
        add_btn.pack(side=tk.LEFT, padx=5)
        
        frame = ttk.Frame(root)
        frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        canvas = tk.Canvas(frame)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        self.checkboxes = {}
        for name, url in links.items():
            var = tk.BooleanVar()
            checkbox = tk.Checkbutton(self.scrollable_frame, text=name, variable=var)
            checkbox.pack(anchor="w", padx=10, pady=5)
            self.checkboxes[name] = var
        
        canvas.pack(side="left", fill=tk.BOTH, expand=True)
        scrollbar.pack(side="right", fill="y")
        
        button = tk.Button(root, text="Открыть в браузере", command=self.open_links, 
                          bg="#4CAF50", fg="white", font=("Arial", 11, "bold"))
        button.pack(pady=10)
    
    def add_link(self):
        name = self.name_entry.get().strip()
        url = self.url_entry.get().strip()
        
        if name and url:
            links[name] = url
            save_links()
            
            var = tk.BooleanVar()
            checkbox = tk.Checkbutton(self.scrollable_frame, text=name, variable=var)
            checkbox.pack(anchor="w", padx=10, pady=5)
            self.checkboxes[name] = var
            
            self.name_entry.delete(0, tk.END)
            self.url_entry.delete(0, tk.END)
    
    def open_links(self):
        for name, var in self.checkboxes.items():
            if var.get():
                webbrowser.open(links[name])

if __name__ == "__main__":
    root = tk.Tk()
    app = LinkOpener(root)
    root.mainloop()