# Ghi chú về các file mẫu

Đây là bộ script đã dùng cho tuần #0021 (Thử thách Flow 7 ngày). Chép sang `ket-qua/<số>/`, sửa nội dung rồi chạy từ thư mục đó.

- `render.py`: 10 banner. Đường dẫn ảnh dạng `img/...`: tạo liên kết `ln -s ../../bo-cong-cu/img img` trong thư mục làm việc.
- `sheets.py`: 7 phiếu PDF A4 một trang.
- `mkdocx.js`: đọc `posts.md` trong thư mục hiện tại, đọc ảnh JPG thu nhỏ trong `docjpg/`, xuất Word vào thư mục truyền vào. Chạy: `node mkdocx.js word`.
- `posts.md`: mẫu 9 bài đăng. Dòng `@img`, `@pdf`, `@cat` là thông tin đính kèm cho Word.
