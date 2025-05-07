# 📚 Welcome to Bookbot
Hey, people !! _FacerOfGod_ here :D 

This is a Python program that analyzes novels and prints a statistical report of the word and character usage found within (project idea comes from [Boot.dev](https://www.boot.dev/)). I want to develop this further with eventually fully functional GUI, but it is going to take some time because I am still improving my skills. I will show my goals steps by step hoping not to suffer too much.

---

## 🚀 1st Project Goals
- [X] Configure a professional Python development environment on your local machine
- [X] Practice building a full project from scratch
- [X] Deploy a Python project to your personal GitHub account

### How it went:
This part was relatively straightforward. I only ran into some minor issues with using Git again and a few problems setting up my Python environment, but overall, it went smoothly. I am so motivated to start this small project !

---
## Quick Demo

Run the program on a sample book:

```bash
python3 main.py books/mobydick.txt
```
**⚠ UPDATED:** due to a few changes caused by the project expansion you must use the key word `cli`

```bash
python3 main.py cli -f books/mobydick.txt
```
Example output:

```
============ BOOKBOT ============
Analyzing book found at books/mobydick.txt...

----------- Word Count ----------
Found 215838 total words

----------- Character Count ----------
e: 119351
t: 89874
a: 79226
o: 70809
n: 66782
i: 66675
s: 65138
h: 63769
r: 53593
l: 43351
d: 38840
u: 27205
m: 23626
c: 23319
w: 22557
g: 21287
f: 21252
p: 17873
y: 17244
b: 17203
v: 8725
k: 8228
q: 1581
j: 1178
x: 1064
z: 636
æ: 23
œ: 5
é: 5
è: 3
ϰ: 1
η: 1
τ: 1
ο: 1
ς: 1
â: 1

============= END ===============
```
---
## 🚀 2nd Project Goals
- [X] Create a GUI where you can simply drag and drop files
- [X] Have visual represation of the number of characters on a chart
- [ ] Allow analyse of various documents other than .txt
- [ ] Ideally handle all times of errors
- [ ] User flow test

### How it went:

- #### Project Structure
This part of the project has been quite challenging since I’ve never built a GUI in Python before. I chose to work with **PySide6** and **Matplotlib** to tackle it. Along the way, I realized that my initial file structure wasn’t well-designed — I had lumped the GUI logic, styles, and controllers all into a single `.py` file. This made the code hard to read and even harder to scale.

To fix this, I restructured the project by separating the GUI components, styling, and logic into distinct modules. I took inspiration from my past **Kotlin group project**, where we followed a similar structure, and applying that same pattern here has made the codebase much cleaner and easier to manage.

- #### GUI
Building the GUI was fun... until it came to placing the buttons. Lining things up the way I wanted—especially the Delete button—was trickier than expected. It took way more tweaking than it probably should’ve to get it looking right. Layout managers can be a bit of a headache, but after some trial and error (and maybe a few frustrated sighs), everything ended up more or less where it should be. Still room to improve, but it works!

- #### Support of various documents
Supporting file types beyond .txt turned out to be more complicated than I expected. Each format has its own quirks—whether it's encoding, hidden characters, or just how the data is structured. I started looking into handling .pdf and .docx, but quickly realized that parsing them properly would need extra libraries and a lot more logic to handle edge cases. I will come back to this

- #### Testing
Testing went pretty well. I used **pytest** for some basic unit tests and ran through a few user flows to make sure things like insert a file works, cli works well, and chart updates worked as expected. Most of it held up nicely. Error handling still needs more work, especially with weird or unsupported files, but overall it’s in a good spot for now.

---
## 🚀 3th Project Goals
- [X] Allow user to input text throught GUI
- [X] Scrap off Wikipedia what the user wants to text
- [X] Build a `.exe` file to run
- [X] Keep all the previous goals functional

### How it went:

- #### Scraping
I thought scraping **Wikipedia** would be a simple task—just fetch the HTML and grab the content. Fetching the URL was easy using **DuckDuckGo**, but actually extracting the text turned out to be trickier. I quickly realized that Wikipedia's structure is more complex than I expected. 

I tried using **BeautifulSoup** for parsing the HTML, which helped a lot in isolating the main content from the sidebars and ads. But, even with that, I ran into issues like stray links or images mixed in with the text. It’s not perfect yet, but it works for now. I’ll need to clean up the output and handle some edge cases, but I’m on the right track!

- #### Building `.exe`
Building the `.exe` was a bit of a headache. It wasn’t the big stuff, but rather all the little annoying problems—like the icons and logo not showing up, or the window opening behind everything else. These tiny issues took way more time to fix than I expected, but after some trial and error, I got everything working. Still, it’s a process that could’ve gone smoother!

---
## Quick Demo
If you want to build the project use the following:

```bash
pyinstaller Bookbot.spec
```
This should build a folder `dist` with the following:

![image](https://github.com/user-attachments/assets/1f402a9e-a7c3-428b-8a38-afb1f6e07b95)

The following GUI should look like this:

<img src="https://github.com/user-attachments/assets/a5ccaf35-1bb3-4636-93af-c89eea71f5c1" width="300" height="300"/>
<br>
<img src="https://github.com/user-attachments/assets/edc56fc6-be09-49f1-817f-32cfc8d492b4" width="300" height="300"/>

---
