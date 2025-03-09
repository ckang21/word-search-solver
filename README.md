# word-search-solver
Side project just to solve word search problems on a whim. It goes through each row and column looking for the first character of the word we want then it searches each direction looking for the rest of the word.

## 🔍 How It Works
- The grid is a list of lists (like a 2D array).
- The program loops through every letter in the grid.
- If the first letter of the word matches, it checks all directions to see if the whole word fits.
- If found, it returns the start and end coordinates of the word.

## 🖥️ Example Run

### **Input:**
Grid: C | A | T | D B | G | O | G I | R | D | X N | A | T | S

Word: "CAT"

### **Output:**
Word 'CAT' found from (0, 0) to (0, 2)

## 🚀 How to Run It
1. Make sure you have Python installed.
2. Clone the repo: 
git clone https://github.com/ckang21/word-search-solver.git cd word-search-solver
3. Install dependencies: pip install numpy
4. Run the program: python3 solver.py

## 🔧 Next Steps (Planned Improvements)
Some possible improvements:
- Allow searching for **multiple words** at once.
- Read the grid from a **text file** instead of hardcoding it.
- Make a simple **command-line interface** to let users input words.

## 📜 License
This project is licensed under the **MIT License** – free to use and modify.

### 🎯 Notes:
If you run into issues or have ideas for improvements, feel free to submit an **issue** or **pull request**. Always happy to improve the solver!

