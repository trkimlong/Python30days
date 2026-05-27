#Day 2: Git & GitHub
# Bài 1: Tạo repo đàu tiên
mkdir python-30-days
cd python-30-days
git init
touch README.md
echo "# Python 30 Days Learning" > README.md
git add README.md
git commit -m "init: tạo repo học Python"
git log --oneline
git config --global user.name "yourgithubusername" # để cấu hình github
git config --global user.email "youruseremail" # để cấu hình github

# Bài 2: Vòng lặp làm việc thực tế
# Tạo file day01.py, thêm code từ ngày 1, commit
touch day01.py
git commit -m "day01: biến, kiểu dữ liệu, f-string"
# Sửa file, commit lại
# Sửa code
git add day01.py
git commit -m "day01: thêm bài tập debug indentation"
# Xem sự khác biệt giữa 2 commit
git diff HEAD~1 HEAD

# Bài 3: Tạo .gitignore - Bỏ qua file không cần thiết, không commit rác
cat > .gitignore << 'EOF'
__pycache__/
*.pyc
.env
env/
venv/
*.log
.DS_Store
EOF
git add .gitignore
git commit -m "config: thêm .gitignore"

# Bài 4: Tạo tài khoản GitHub, tạo repo mới, push code lên
# Tạo thành công nhưng vấp lỗi master -> main do dùng git cũ tạo repo trên vscode và tạo trên github thì mặc định là main
git branch -m master main # để đổi tên branch master thành main
# Lỗi rejected khi mình tạo repo trên GitHub có README.md, nên mình phải pull về trước rồi mới push lên được

# Bài 5: Push lên GitHub
git remote add origin https://github.com/yourusername/python-30-days.git
git push -u origin main

# Thành công và đã add day01.py lên GitHub và đây là Day02