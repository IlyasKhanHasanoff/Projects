import tkinter as tk
import webbrowser

class Browser:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Simple Browser")
        self.window.geometry("800x600")
        
        # Create an Entry widget for entering URLs
        self.url_entry = tk.Entry(self.window)
        self.url_entry.pack(side=tk.TOP, fill=tk.X)
        self.url_entry.bind("<Return>", self.load_url)
        
        # Create a Text widget for displaying web content
        self.content_text = tk.Text(self.window)
        self.content_text.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        self.window.mainloop()
        
    def load_url(self, event):
        url = self.url_entry.get()
        try:
            # Open the URL in the default web browser
            webbrowser.open(url)
        except:
            self.content_text.insert(tk.END, "Error loading URL")

if __name__ == "__main__":
    browser = Browser()
