# Quy trình soạn tuần mới: Sổ thực hành 10X Excellence Hub

Tài liệu này dành cho phiên Claude chạy tự động mỗi tuần. Đọc hết trước khi làm.

## 1. Bối cảnh

- 10X Excellence Hub là cộng đồng Skool của John&Partners, dành cho người muốn nâng cao năng lực và xây thói quen để thành công. Gói trả phí 29 USD/tháng.
- Mỗi tuần có một "Công thức thành công" (file PDF, đánh số #0021, #0022...). Từ công thức đó, cộng đồng chạy một **thử thách 7 ngày**:
  - Chủ Nhật: Bài 0 thông báo, đính kèm PDF công thức đầy đủ.
  - Thứ Hai đến Chủ Nhật tuần sau: 7 bài, mỗi ngày một việc từ 10 đến 45 phút, kèm banner, phiếu PDF một trang và câu check-in một dòng.
  - Thứ Hai kế tiếp: bài tổng kết, kèm thẻ thành tích.
- Thành viên làm bài trên trang https://10xexcellence.co/so-thuc-hanh. Trang đọc file trong kho này ở nhánh `main`:
  - `sth.js`: phần khung, KHÔNG sửa.
  - `weeks.json`: danh sách tuần.
  - `<số công thức>.json`: nội dung 7 ngày của từng tuần, ví dụ `0021.json`.

## 2. Luật nội dung, bắt buộc

1. 100% tiếng Việt. Ngôn ngữ business chuyên nghiệp, không dùng từ Hán Việt hoa mỹ, không dùng văn nói (dùng "điều", "việc", "yếu tố" thay cho "thứ").
2. Không hứa hẹn, không cam kết kết quả (không viết "chắc chắn", "đảm bảo", "sẽ giúp bạn tăng gấp..."). Không bịa câu chuyện, số liệu hay lời kể của người thật; dùng "Hãy hình dung..." khi cần tình huống minh hoạ.
3. Không dùng dấu gạch ngang dài (em dash, en dash). Thay bằng dấu phẩy hoặc dấu hai chấm.
4. Các bài trong tuần phải khác nhau về cách viết: xoay vòng kể tình huống, hỏi đáp, danh sách, đối chiếu, giải nghĩa, câu hỏi mở. Bài đủ dài, không cụt.
5. Mỗi ngày đúng một việc, nêu rõ thời gian (10 đến 45 phút), có câu check-in mẫu một dòng.
6. Nội dung bám sát PDF công thức của tuần. Không thêm ý không có trong PDF.

## 3. Luật thiết kế, bắt buộc

1. Chỉ dùng đen, trắng và đỏ thương hiệu `#862222` (đổi độ đậm nhạt để phân lớp). Tuyệt đối không dùng màu vàng ở bất kỳ đâu, kể cả đường kẻ trang trí. Không dùng nền đen.
2. Mọi hình có logo 10X Excellence Hub: `img/logo_w_crop.png` trên nền đỏ hoặc ảnh tối, `img/logo_c_crop.png` trên nền sáng.
3. Banner 1920x1080, chụp với `device_scale_factor=2`, ra file PNG 3840x2160.
4. Tiêu đề trên hình viết IN HOA, dài 25 đến 35 ký tự, nằm một dòng khi đủ chỗ; không tách một cụm từ ra hai dòng (dùng hàm `nb()` và `fit()` trong `mau/render.py`).
5. 10 hình trong tuần (thông báo, 7 ngày, tổng kết, thẻ thành tích) không trùng bố cục. `mau/render.py` có 10 bố cục mẫu: dùng lại khung, thay nội dung, và đổi thứ tự hoặc biến thể so với tuần trước để các tuần không giống hệt nhau.
6. Ảnh nền: ưu tiên ảnh chung chung (toà nhà, văn phòng, thành phố), dùng ảnh trong `img/`. Không dùng ảnh khách hàng thật.
7. Phiếu PDF: khổ A4, đúng 1 trang (kiểm tra số trang sau khi xuất).

## 4. Các bước mỗi lần chạy

1. **Tìm công thức mới.** Dùng kết nối Google Drive (chỉ đọc, không tạo hay sửa gì trên Drive).
   - Thư mục gốc "Công thức thành công của tuần" có ID `1RyX_S_2Mod1rmk41fqNqZuINCHJQRpOl`. Bên trong là các thư mục tuần, tên dạng `2026_Tháng 10_Tuần 1`, `2026_Tháng 10_Tuần 2`...
   - Sắp các thư mục tuần theo năm, tháng, số tuần. Lần lượt mở từng thư mục, tìm file PDF tên dạng `10XHub_CongThuc_<số>_..._VN.pdf`. Lấy số công thức từ tên file (ví dụ `0022`).
   - Chọn thư mục tuần đầu tiên có PDF mà số công thức chưa có trong `weeks.json`. Đó là tuần cần soạn.
   - Nếu không có: dừng, báo "Chưa có công thức mới trong thư mục Drive", không sửa gì.
   - Tải file PDF về bằng công cụ tải nội dung file của kết nối Google Drive.
2. **Đọc PDF** và tóm tắt: khái niệm chính, các điều kiện hay bước, công cụ, câu hỏi tự đánh giá.
3. **Xác định lịch.** Bài 0 đăng Chủ Nhật gần nhất sau ngày chạy. Ngày 1 đến Ngày 7 là Thứ Hai đến Chủ Nhật kế tiếp. Bài tổng kết là Thứ Hai sau đó. Ghi ngày cụ thể dạng "Thứ Hai 19/10".
4. **Soạn file tuần** `<số>.json` theo đúng cấu trúc của `0021.json` (xem mục 5). Mỗi ngày phải có câu check-in tự sinh từ các ô điền.
5. **Cập nhật `weeks.json`:** thêm một mục `{"id":"<số>","label":"Tuần <n>","file":"<số>.json","show":"<ngày Bài 0, dạng YYYY-MM-DD>"}` vào cuối mảng `weeks`. Giữ nguyên các mục cũ. `n` là số thứ tự tuần (tuần đầu là Tuần 1 = 0021).
6. **Kiểm tra file tuần chạy được:** viết trang test như sau, mở bằng Playwright (Chromium có sẵn) qua `python3 -m http.server`, bỏ trường `show` hoặc đặt ngày trong quá khứ trong một bản `weeks.json` tạm để thấy tuần mới. Duyệt đủ 7 ngày, điền thử, xác nhận câu check-in hiện ra và không có lỗi JavaScript.
   ```html
   <div id="flow7-root"></div><script>window.STH_BASE="/";</script><script src="/sth.js"></script>
   ```
7. **Soạn 9 bài đăng** vào `ket-qua/<số>/posts.md` theo định dạng của `mau/posts.md` (Bài 0, Bài 1 đến 7, Tổng kết). Mỗi bài Ngày n có đường link `https://10xexcellence.co/so-thuc-hanh#<số>-ngay-n`. Bài 0 nhắc PDF công thức đầy đủ đính kèm.
8. **Dựng 10 banner** bằng cách chép `mau/render.py` sang `ket-qua/<số>/render.py`, thay nội dung và chỉnh bố cục, rồi chạy. Kiểm tra kết quả `CHECK` in ra: không có tiêu đề tràn (`over: false`), không vượt khung (`docOver: false`). Xem lại từng ảnh.
9. **Dựng 7 phiếu PDF** một trang từ `mau/sheets.py`, theo nội dung từng ngày. Kiểm tra mỗi file đúng 1 trang.
10. **Dựng 9 file Word** từ `mau/mkdocx.js` (cài `npm install docx` nếu thiếu). Đổi tên chuỗi "Thử thách Flow 7 ngày" và tiền tố tên file theo chủ đề tuần. Ảnh trong Word dùng bản JPG thu nhỏ của banner.
11. **Đóng gói** banner, phiếu PDF, Word và posts.md vào `ket-qua/10XHub_Tuan_<số>.zip`. Không đưa file tạm (html, render.py) vào zip.
12. **Commit và push thẳng lên `main`**: `<số>.json`, `weeks.json`, thư mục `ket-qua/<số>/` (chỉ posts.md và các script) và file zip. Không tạo nhánh phụ, không tạo pull request. Không sửa `sth.js`, `0021.json` hay các tuần cũ.
13. **Xác nhận** sau khi push: tải `https://raw.githubusercontent.com/ashleynguyen1486/10x-so-thuc-hanh/main/weeks.json` thấy có tuần mới.
14. **Báo cáo cuối phiên**, ngắn gọn bằng tiếng Việt: số công thức, chủ đề, ngày Bài 0, ngày tuần mới tự hiện trên trang, đường link tải zip (`https://github.com/ashleynguyen1486/10x-so-thuc-hanh/raw/main/ket-qua/10XHub_Tuan_<số>.zip`), và bất kỳ điểm nào cần Admin xem lại.

## 5. Cấu trúc file tuần

Xem `0021.json` ở gốc kho làm mẫu đầy đủ. Các trường:

- `id`, `name` (tên ngắn trên tab tuần), `storeKey` (`"sth-<số>"`), `kicker` (`"Công thức #<số>"`), `title`, `sub`.
- `days`: đúng 7 phần tử. Mỗi ngày: `label` (Thứ Hai...), `kick`, `title`, `time`, `cards`, `checkin`, `hint`.
- Mỗi `card`: `h` (tiêu đề thẻ) và `items`. Các loại item (`f`):
  - `ta` ô nhiều dòng, `tx` ô một dòng: `k`, `q`, `ph`.
  - `cb` ô tích: `k`, `label`.
  - `seg` chọn một: `k`, `q`, `opts` (mảng chữ), tuỳ chọn `hints` cùng độ dài để hiện gợi ý.
  - `note`: `text`. `show`: `text` có `{khoá}`, `need` (chỉ hiện khi các khoá đã có giá trị).
  - `rows`: danh sách việc có nút chọn vùng: `kp`, `n`, `ph`, `zk`, `zones` ([[giá trị, nhãn]]).
  - `matrix`: ma trận 2x2 từ `rows`: `kp`, `n`, `zk`, `top`, `bottom`, `zones` ([[giá trị, nhãn, mô tả, 1 nếu tô đỏ]]).
  - `pick`: chọn một trong các việc đã điền: `k`, `kp`, `n`, `empty`.
  - `nums`: các ô số: `items` [{k, q}].
  - `timer`: đồng hồ: `k` (khoá lưu số phút), `dk`, `opts`, `def`, `note`.
  - `compare`: bảng so sánh chỉ đọc: `cols`, `rows` [{label, keys}].
  - `sum`: bảng cộng có ô nhập: `head`, `rows` [{label, keys}].
  - `rate`: bảng chấm điểm: `kp`, `scale`, `head`, `rows` [[tên, gợi ý]].
  - `cal`: lịch tuần bấm chọn ô: `k`, `mark`, `max`, `cols`, `rows`.
- `checkin`: mảng phần câu `{tpl, need}`. `tpl` dùng `{khoá}`, `{khoá|mặc định}`, `{sum:k1,k2}`, `{cal:khoá}`. Một phần chỉ xuất hiện khi mọi khoá trong `need` có giá trị. Các phần nối liền nhau thành câu check-in.
- Khoá (`k`) đặt riêng cho từng tuần, không trùng trong cùng một tuần.

## 6. Khi gặp lỗi

- Không push được: báo nguyên văn lỗi, không thử cách khác làm thay đổi cài đặt kho.
- PDF không đọc được: dừng và báo.
- Không chắc nội dung có đúng ý PDF: vẫn soạn, nhưng ghi rõ điểm cần Admin xem lại trong báo cáo.
