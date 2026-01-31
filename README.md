# PPM to ASCII Art Converter 🎨➡️📄

A Python project that converts **P3 (ASCII) PPM images** into **ASCII art** by transforming RGB pixels into grayscale and mapping pixel intensity to text characters.

---

## 📌 Features
- Supports **P3 ASCII PPM** image format
- Ignores comments and blank lines in PPM files
- Converts RGB pixels to grayscale
- Maps pixel brightness to ASCII characters
- Saves output as a `.txt` file
- Beginner-friendly and well-structured code

---

## 🛠️ Technologies Used
- Python 3
- File Handling
- Basic Image Processing
- ASCII Art Generation

---

## 📂 Project Structure
```bash
ppm-to-ascii-art/
│
├── face.ppm            # Input PPM image
├── ascii_output.txt    # Generated ASCII art
├── main.py             # Python source code
└── README.md           # Project documentation

```

---

## ▶️ How to Run the Project

1. **Clone the repository**
```bash
git clone https://github.com/your-username/ppm-to-ascii-art.git
````

2. **Navigate to the project folder**

```bash
cd ppm-to-ascii-art
```

3. **Run the Python script**

```bash
python main.py
```

4. **Output**

* ASCII art will be saved in `ascii_output.txt`

---

## 🧠 How It Works

1. Reads a P3 PPM image file
2. Extracts width, height, and RGB pixel values
3. Converts RGB pixels to grayscale using average method
4. Maps grayscale values to ASCII characters
5. Writes ASCII art to a text file

---

## 🧪 Sample ASCII Characters Used

```
@%#*+=-:. 
```

---

## 📸 Example

```
@@##**++
**++==--
--::..  
```

---

## 🎓 Use Cases

* Learning basic image processing
* Understanding file parsing in Python
* College mini-project
* ASCII art generation
* GitHub portfolio project

---

## 🚀 Future Enhancements

* Support for P6 (binary) PPM files
* Image resizing for better ASCII output
* Colored ASCII art
* Command-line arguments for input/output files

---

## 👤 Author

**Gudimetla Tharun kumar Reddy**

---
