# 📚 Welcome to Bookbot
Hey, people !! FacerOfGod here :D 

This is a Python program that analyzes novels and prints a statistical report of the word and character usage found within (project idea comes from [Boot.dev](https://www.boot.dev/)). I want to develop this further with eventually fully functional GUI, but it is going to take some time because I am still improving my skills. I will show my goals steps by step hoping not to suffer too much.

---

## 🚀 1st Project Goals
- Configure a professional Python development environment on your local machine
- Practice building a full project from scratch
- Deploy a Python project to your personal GitHub account

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
python3 main.py cli books/mobydick.txt
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

## 🚀 2nd Project Goals
- Create a GUI where you can simply drag and drop files
- Have visual represation of the number of characters on a chart
- Deploy the program on a website

### How it went:

This part of the project has been quite challenging since I’ve never built a GUI in Python before. I chose to work with **PySide6** and **Matplotlib** to tackle it. Along the way, I realized that my initial file structure wasn’t well-designed — I had lumped the GUI logic, styles, and controllers all into a single `.py` file. This made the code hard to read and even harder to scale.

To fix this, I restructured the project by separating the GUI components, styling, and logic into distinct modules. I took inspiration from my past **Kotlin group project**, where we followed a similar structure, and applying that same pattern here has made the codebase much cleaner and easier to manage.
