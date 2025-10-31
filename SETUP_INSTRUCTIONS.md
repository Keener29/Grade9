# 🚀 Setup Instructions for Students

### Step 1: Get the code
1. Go to: [GitHub repository link] (instructor will provide)
2. Click the green **"Code"** button
3. Click **"Download ZIP"**
4. Extract the ZIP file to your Desktop

### Step 2: Edit the code (use ANY text editor - no fancy IDE needed!)
- **Windows**: Right-click `puzzle1.py` → "Open with" → **Notepad** (or Notepad++)
- **Mac**: Right-click `puzzle1.py` → "Open with" → **TextEdit** 
- **Linux**: Right-click → Open with **Text Editor** (gedit)
- **Or use a code editor if you have one**: VS Code, PyCharm, Sublime Text, etc.

**You don't need to install anything special!** The built-in text editors work perfectly fine.

### Step 3: Run the game
```bash
python escape_room.py
```
(or `python3 escape_room.py` if that doesn't work)


## 📥 Installing Python 3

**First, check if Python is already installed:**

1. Open Terminal (Mac/Linux) or Command Prompt (Windows)
   - **Windows**: Press `Windows key + R`, type `cmd`, press Enter
   - **Mac**: Press `Cmd + Space`, type "Terminal", press Enter
   - **Linux**: Press `Ctrl + Alt + T`

2. Run this command:
   ```bash
   python --version
   ```
   or
   ```bash
   python3 --version
   ```

3. If you see something like `Python 3.9.0` or higher → **You're done!** Skip to "Quick Test" below.

4. If you see "Python is not recognized" or "command not found" → Follow the installation steps below.

---

### 🪟 Installing Python on Windows

1. **Download Python:**
   - Go to [python.org/downloads](https://www.python.org/downloads/)
   - Click the big yellow "Download Python 3.x.x" button
   - The download will start automatically

2. **Run the installer:**
   - Double-click the downloaded file (usually in your Downloads folder)
   - **IMPORTANT:** Check the box that says **"Add Python to PATH"** at the bottom!
   - Click "Install Now"
   - Wait for installation to complete

3. **Verify installation:**
   - Close and reopen Command Prompt
   - Run: `python --version`
   - You should see: `Python 3.x.x`

4. **If `python --version` doesn't work:**
   - Open "Edit environment variables" (search in Windows Start menu)
   - Under "System variables", find "Path" and click "Edit"
   - Click "New" and add: `C:\Users\YourName\AppData\Local\Programs\Python\Python3xx` (replace YourName and xx with your version)
   - Or just reinstall Python and make sure to check "Add Python to PATH" this time!

---

### 🍎 Installing Python on Mac

**Option 1: Using the official installer (Recommended)**

1. **Download Python:**
   - Go to [python.org/downloads](https://www.python.org/downloads/)
   - Click "Download Python 3.x.x"
   - Download the `.pkg` file

2. **Install:**
   - Double-click the downloaded `.pkg` file
   - Follow the installation wizard (click "Continue", "Install", etc.)
   - Enter your password when prompted

3. **Verify installation:**
   - Open Terminal
   - Run: `python3 --version`
   - You should see: `Python 3.x.x`

---

## 📝 What You Need

- **Python 3** ✅ (install using instructions above)
- **A text editor** (already on your computer!):
  - **Windows**: Notepad (built-in) - Just right-click the file and "Open with Notepad"
  - **Mac**: TextEdit (built-in) - Just right-click the file and "Open with TextEdit"
---

## ✅ Quick Test

**Step 1: Test Python installation**

1. Open Terminal (Mac/Linux) or Command Prompt (Windows)
2. Run:
   ```bash
   python --version
   ```
   or
   ```bash
   python3 --version
   ```
3. You should see: `Python 3.x.x` (any version 3.6 or higher is fine)
4. If this works, Python is installed and in your PATH! ✅

**Step 2: Test the escape room**

1. Navigate to your project folder:
   ```bash
   cd ~/Desktop/Grade9  # Mac/Linux
   cd Desktop\Grade9    # Windows
   ```
   (Or wherever you extracted the files)

2. Run the game:
   ```bash
   python escape_room.py
   ```
   or
   ```bash
   python3 escape_room.py
   ```

3. You should see the escape room game start! 🎮

**If you get an error:**
- "Python is not recognized" → Python isn't in your PATH (see Windows installation steps above)
- "No such file or directory" → Make sure you're in the right folder (where `escape_room.py` is located)
- "Permission denied" → On Mac/Linux, you might need to use `python3` instead of `python`

