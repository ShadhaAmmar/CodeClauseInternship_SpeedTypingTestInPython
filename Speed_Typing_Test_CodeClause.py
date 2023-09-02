import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random
import time

class SpeedTypingTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Code Clause Speed Typing Test")
        self.root.geometry("750x700")
        self.root.config(bg="white")
        
        # Load images
        self.code_clause_img = Image.open("codeclause.png")
        self.code_clause_img = self.code_clause_img.resize((100, 100), Image.ANTIALIAS)
        self.code_clause_img = ImageTk.PhotoImage(self.code_clause_img)
        
        self.timer_img = Image.open("timer.png")
        self.timer_img = self.timer_img.resize((100, 100), Image.ANTIALIAS)
        self.timer_img = ImageTk.PhotoImage(self.timer_img)
        
        # Typography settings
        self.font = ("Arial", 14)
        self.black_color = "black"
        self.turquoise_color = "#00CED1"
        
        # Randomly select a word from the list
        self.text = ["apple", "banana", "cherry", "grape", "kiwi", "mango", "orange", "pear", "strawberry","elephant", "giraffe", 
                    "kangaroo", "lion", "penguin", "rhinoceros", "tiger", "zebra","cryptography","juxtaposition", "labyrinthine", 
                    "quizzaciously", "unbelievable", "zygomatic","code","clause","Code Clause","code clause","{Code Clause};"
                    "This is a sample sentence.","Coding is fun.","The quick brown fox jumps over the lazy dog.","Today is a beautiful day.",
                    "Python programming is versatile and powerful.","I enjoy learning new things every day.","The sun sets in the west.",
                    "A journey of a thousand miles begins with a single step.","Reading books broadens your horizons.","Life is full of surprises.",
                    "Happiness is a state of mind.","In the midst of winter, I found there was, within me, an invincible summer.",
                    "The best way to predict the future is to create it.","Every problem is an opportunity in disguise.",
                    "CodeClause's internships are enriching experiences.","Positive work environment fosters creativity.",
                    "Team collaboration at CodeClause is inspiring.","Coding challenges at CodeClause are exciting.",
                    "Innovation is key to success at CodeClause.","CodeClause promotes a culture of continuous learning.",
                    "CodeClause's values align with personal growth.","CodeClause's work environment is supportive and inclusive.",
                    "Problem-solving is a daily adventure at CodeClause.","CodeClause encourages exploring new technologies.",
                    "Dedicated mentors guide interns at CodeClause.",]

        self.current_word = random.choice(self.text)
        
        self.start_time = 0
        self.end_time = 0
        self.typing_text = tk.StringVar()
        self.typing_text.set(self.current_word)
        
        self.code_clause_label = tk.Label(root, image=self.code_clause_img, bg="white")
        self.code_clause_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.app_label = tk.Label(root, text="Code Clause Speed Typing Test", font=("Arial", 20), fg=self.turquoise_color, bg="white")
        self.app_label.grid(row=0, column=1, padx=10, pady=10, sticky="w")
         
        self.input_text_label = tk.Label(root, text="Type the following:", font=("Arial", 14), bg="white", fg=self.black_color)
        self.input_text_label.grid(row=1, column=0, columnspan=3, pady=10)

        self.random_word_label = tk.Label(root, textvariable=self.typing_text, font=self.font, bg="white")
        self.random_word_label.grid(row=2, column=0, columnspan=3, pady=(20, 10))       
        
        self.input_text = tk.Entry(root, font=self.font)
        self.input_text.grid(row=3, column=0, columnspan=3, pady=(0, 10), padx=10, sticky="n")

        self.clear_button = ttk.Button(root, text="Clear", style="Turquoise.TButton", command=self.clear_text)
        self.clear_button.grid(row=4, column=0, columnspan=1, pady=10, padx=10, sticky="n")
        
        self.submit_button = ttk.Button(root, text="Submit", style="Turquoise.TButton", command=self.submit_text)
        self.submit_button.grid(row=4, column=1, columnspan=1, pady=10, padx=10, sticky="n")        
        
        self.update_button = ttk.Button(root, text="Update", style="Turquoise.TButton", command=self.update_text)
        self.update_button.grid(row=4, column=2, columnspan=1, pady=10, padx=10, sticky="n")

        
        self.timer_label = tk.Label(root, image=self.timer_img, bg="white")
        self.timer_label.grid(row=5, column=0, columnspan=3, pady=10)
        
        self.timer_display = tk.Label(root, text="00:00", font=("Arial", 24), bg="white", fg=self.black_color)
        self.timer_display.grid(row=6, column=0, columnspan=3, pady=10)
        
        self.statistics_label = tk.Label(root, text="", font=("Arial", 14), bg="white", fg=self.black_color)
        self.statistics_label.grid(row=7, column=0, columnspan=3, pady=10)
        
        style = ttk.Style()
        style.configure("Turquoise.TButton", background=self.turquoise_color, font=self.font, padding=10)
        
        self.input_text.bind("<KeyPress>", self.start_typing)

        
    def start_typing(self, event):
        if self.start_time == 0:
            self.start_time = time.time()
            self.update_timer()
        
    def clear_text(self):
        self.input_text.delete(0, tk.END)
        self.stop_timer()
        
    def update_text(self):
        self.current_word = random.choice(self.text)
        self.typing_text.set(self.current_word)
        self.input_text.delete(0, tk.END)
        self.start_time = 0
        self.end_time = 0
        self.update_timer()
        
    def update_timer(self):
        if self.start_time > 0:
            elapsed_time = time.time() - self.start_time
            formatted_time = time.strftime("%M:%S", time.gmtime(elapsed_time))
            self.timer_display.config(text=formatted_time)
            self.root.after(1000, self.update_timer)
    
    def stop_timer(self):
        self.start_time = 0
        self.end_time = 0
        self.timer_display.config(text="00:00")
        self.root.after_cancel(self.update_timer)
    
    def submit_text(self):
        entered_text = self.input_text.get()
        if entered_text == self.current_word:
            self.update_statistics()
        else:
            self.statistics_label.config(text="Incorrect. Try again.")

    def update_statistics(self):
        self.end_time = time.time()
        if self.start_time > 0:
            elapsed_time = self.end_time - self.start_time
            characters_typed = len(self.input_text.get())
            cps = characters_typed / elapsed_time
            cpm = cps * 60
            words_typed = len(self.input_text.get().split())
            wps = words_typed / elapsed_time
            wpm = wps * 60
            
            formatted_time = time.strftime("%M:%S", time.gmtime(elapsed_time))
            
            result_message = f"Time: {formatted_time}\nCPS: {cps:.2f}\nCPM: {cpm:.2f}\nWPS: {wps:.2f}\nWPM: {wpm:.2f}"
            
            self.statistics_label.config(text=result_message)
        
        self.current_word = random.choice(self.text)
        self.typing_text.set(self.current_word)
        self.input_text.delete(0, tk.END)
        self.stop_timer()
        self.update_statistics()

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeedTypingTestApp(root)
    root.mainloop()
