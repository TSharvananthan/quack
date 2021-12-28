# Pre Config
## Removing the exe (if it exists)
rm quack

# Creating Exe
pyinstaller --onefile quack.py
mv dist/quack .
chmod +x quack
rm -rf build dist
rm quack.spec