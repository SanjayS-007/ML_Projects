# 🚀 How to Start Jupyter Lab

**Easy Methods to Launch Jupyter Lab**

---

## ⚡ EASIEST METHOD - Double-Click!

**Just double-click this file:**
```
START_JUPYTER.bat
```

✅ Jupyter Lab will:
- Activate the virtual environment
- Start on port 8888
- **Automatically open in your browser**
- Show the file browser ready to use!

---

## 🔧 METHOD 2 - PowerShell Script

In PowerShell terminal:
```powershell
cd D:\ML_Projects
.\start_jupyter.ps1
```

---

## 📝 METHOD 3 - Manual (If you want control)

```powershell
# 1. Navigate to project
cd D:\ML_Projects

# 2. Activate environment  
.\ml_env\Scripts\Activate.ps1

# 3. Start Jupyter Lab (will auto-open browser)
jupyter lab
```

**What if the browser shows a file error?**
- Just look in the terminal for `http://localhost:8888/lab?token=...`
- Copy that URL and paste it in your browser

---

## 🛑 How to Stop Jupyter Lab

Press **Ctrl + C** in the terminal (twice if needed)

---

## 💡 Tips

**Bookmark the URL:**
Once Jupyter opens, bookmark the page for quick access!

**Check what's running:**
```powershell
jupyter lab list
```

**Stop all Jupyter servers:**
```powershell
jupyter lab stop
```

**Change port if needed:**
```powershell
jupyter lab --port=9000
```

---

## 🎯 What You'll See

When Jupyter Lab opens:
1. **Left sidebar** → File browser
2. Navigate to: `notebooks/experiments/01_house_price_prediction/`
3. Double-click: `house_price_prediction.ipynb`
4. Select kernel: **"Python (ML-GPU)"**
5. Run cells with **Shift + Enter**

---

## ⚠️ Troubleshooting

**"Port already in use":**
```powershell
# Find what's using the port
netstat -ano | findstr :8888

# Kill the process (use PID from above)
taskkill /PID <number> /F

# Or use a different port
jupyter lab --port=9000
```

**Browser doesn't open:**
- Look for the `http://localhost:8888/lab?token=...` URL in terminal
- Copy and paste it in your browser manually

**"Command not found":**
- Make sure virtual environment is activated
- You should see `(ml_env)` at the start of your prompt

---

**Updated:** December 5, 2025
