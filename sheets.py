import asyncio, os
from playwright.async_api import async_playwright
D = os.path.dirname(os.path.abspath(__file__))
K = '#862222'; CR = '#FBF3F2'; GR = '#F1E4E2'; INK = '#231F20'; LN = '#D9C3C0'

CSS = f"""
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
@page {{ size: A4; margin: 0 }}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:210mm;height:297mm;font-family:'Be Vietnam Pro',sans-serif;color:{INK};background:#fff;font-size:10.5pt}}
.page{{width:210mm;height:297mm;display:flex;flex-direction:column}}
.hd{{background:{K};color:#fff;padding:9mm 14mm 8mm;display:flex;justify-content:space-between;align-items:flex-end;gap:8mm}}
.hd .k{{font-size:8.5pt;font-weight:700;letter-spacing:.18em;opacity:.9}}
.hd h1{{font-size:21pt;font-weight:800;line-height:1.24;text-transform:uppercase;margin-top:2mm}}
.hd img{{height:19mm}}
.ct{{flex:1;padding:8mm 14mm 0;display:flex;flex-direction:column;gap:5mm}}
.lead{{font-size:10.5pt;line-height:1.55}}
.sec{{font-size:9pt;font-weight:800;letter-spacing:.14em;color:{K};text-transform:uppercase;margin-bottom:2mm}}
.box{{border:1.4pt solid {K};border-radius:3mm;padding:4mm 5mm}}
.soft{{background:{CR};border-radius:3mm;padding:4mm 5mm}}
.line{{border-bottom:0.8pt solid {LN};height:8.5mm}}
.q{{font-weight:600;margin-top:2.5mm}}
.chk{{display:flex;gap:3mm;align-items:center;margin:1.6mm 0}}
.cb{{width:4.2mm;height:4.2mm;border:1.2pt solid {K};border-radius:1mm;flex:0 0 auto}}
table{{width:100%;border-collapse:collapse}}
th{{background:{K};color:#fff;font-size:9pt;font-weight:700;text-align:left;padding:2.2mm 3mm}}
td{{border-bottom:0.8pt solid {LN};padding:0 3mm;height:12mm;vertical-align:middle}}
.ci{{margin-top:auto;background:{K};color:#fff;border-radius:3mm 3mm 0 0;padding:5mm 6mm}}
.ci b{{letter-spacing:.12em;font-size:8.5pt}}
.ci .s{{font-size:11pt;margin-top:1.5mm;line-height:1.5}}
.ft{{background:{K};color:#fff;font-size:7.5pt;letter-spacing:.12em;padding:0 14mm 5mm;display:flex;justify-content:space-between;opacity:1}}
.grid2{{display:grid;grid-template-columns:1fr 1fr;gap:4mm}}
</style>"""

def L(n): return ''.join('<div class="line"></div>' for _ in range(n))
def C(t): return f'<div class="chk"><div class="cb"></div><div>{t}</div></div>'

def page(day, kick, title, body, checkin):
    return f"""<!doctype html><html><head><meta charset="utf-8">{CSS}</head><body><div class="page">
<div class="hd"><div><div class="k">THỬ THÁCH FLOW 7 NGÀY · NGÀY {day}/7 · {kick}</div><h1>{title}</h1></div><img src="img/logo_w_crop.png"></div>
<div class="ct">{body}
<div class="ci"><b>CHECK-IN TRÊN 10X EXCELLENCE HUB</b><div class="s">{checkin}</div></div></div>
<div class="ft"><span>CÔNG THỨC #0021 · TRẠNG THÁI DÒNG CHẢY</span><span>Họ tên: ................................ Ngày: ....../....../......</span></div>
</div></body></html>"""

S = {}
S[1] = page(1, 'NHẬN DIỆN', 'Lần gần nhất bạn quên thời gian', f"""
<div class="lead">Flow là trạng thái hoà toàn vào việc đang làm, quên thời gian và quên việc tự đánh giá bản thân. Trang này giúp bạn nhận ra lúc nào mình đã từng ở trạng thái đó. Thời lượng: khoảng 10 phút.</div>
<div class="box"><div class="sec">Nhớ lại một lần gần đây</div>
<div class="q">Khi đó tôi đang làm việc gì?</div>{L(2)}
<div class="q">Ở đâu, vào khoảng thời gian nào trong ngày?</div>{L(2)}
<div class="q">Điều gì giúp tôi tập trung được như vậy?</div>{L(3)}</div>
<div class="soft"><div class="sec">Ba điều kiện cốt lõi lúc đó có mặt không?</div>
{C('Mục tiêu rõ ràng: tôi biết chính xác thế nào là xong')}
{C('Phản hồi ngay: tôi biết mình làm đúng hay chưa ngay trong lúc làm')}
{C('Độ khó vừa sức: đủ để phải cố gắng nhưng chưa quá tải')}</div>
<div><div class="sec">Một điều tôi muốn tạo lại trong tuần này</div>{L(2)}</div>
""", '"Lần gần nhất tôi quên thời gian là khi ..."')

def cell(t, sub, bg, fg):
    return f'<div style="background:{bg};color:{fg};border-radius:3mm;padding:3mm 4mm;min-height:36mm"><div style="font-weight:800;letter-spacing:.06em">{t}</div><div style="font-size:8pt;opacity:.85;margin-bottom:2mm">{sub}</div><div style="border-bottom:0.8pt solid {fg if fg!="#fff" else "rgba(255,255,255,.55)"};height:7mm;opacity:.5"></div><div style="border-bottom:0.8pt solid {fg if fg!="#fff" else "rgba(255,255,255,.55)"};height:7mm;opacity:.5"></div><div style="border-bottom:0.8pt solid {fg if fg!="#fff" else "rgba(255,255,255,.55)"};height:7mm;opacity:.5"></div></div>'
S[2] = page(2, 'BẢN ĐỒ CÔNG VIỆC', 'Việc nào đang ở vùng Flow?', f"""
<div class="lead">Liệt kê 5 việc chiếm nhiều thời gian nhất trong tuần, đặt từng việc vào một trong bốn vùng, rồi khoanh tròn việc gần vùng Flow nhất để dùng cho phiên Flow ngày mai. Thời lượng: khoảng 15 phút.</div>
<table><tr><th style="width:8%">#</th><th>Việc chiếm nhiều thời gian nhất</th><th style="width:30%">Thuộc vùng</th></tr>
{''.join(f'<tr><td>{i}</td><td></td><td></td></tr>' for i in range(1,6))}</table>
<div style="display:flex;gap:3mm"><div style="writing-mode:vertical-rl;transform:rotate(180deg);font-size:8pt;font-weight:700;letter-spacing:.16em;color:{K};text-align:center">THỬ THÁCH CAO →</div>
<div style="flex:1"><div class="grid2">
{cell('LO ÂU','Thử thách cao, kỹ năng thấp: chia nhỏ thành bước vừa sức',GR,INK)}
{cell('FLOW','Thử thách cao, kỹ năng cao: vùng cần tăng thêm',K,'#fff')}
{cell('VÔ CẢM','Thử thách thấp, kỹ năng thấp: cân nhắc giảm bớt','#F7EFEE',INK)}
{cell('CHÁN','Thử thách thấp, kỹ năng cao: nâng độ khó',CR,K)}
</div><div style="text-align:center;font-size:8pt;font-weight:700;letter-spacing:.16em;color:{K};margin-top:2mm">KỸ NĂNG CAO →</div></div></div>
<div class="soft"><div class="sec">Việc tôi chọn cho phiên Flow ngày mai</div>{L(1)}</div>
""", 'Bình luận việc bạn đã khoanh, hoặc chụp ảnh trang này sau khi điền và đăng lên bài Ngày 2.')

def log(n):
    return f"""<table><tr><th style="width:42%">Nhật ký phiên {n}</th><th>Ghi chép</th></tr>
<tr><td>Thời gian bắt đầu và kết thúc</td><td></td></tr>
<tr><td>Tổng số phút tập trung</td><td></td></tr>
<tr><td>Đã vào Flow chưa?</td><td><span class="cb" style="display:inline-block;vertical-align:middle"></span> Có &nbsp;&nbsp; <span class="cb" style="display:inline-block;vertical-align:middle"></span> Gần Flow &nbsp;&nbsp; <span class="cb" style="display:inline-block;vertical-align:middle"></span> Chưa</td></tr>
<tr><td>Số lần gián đoạn và nguồn gián đoạn</td><td></td></tr>
<tr><td>Lần sau tôi muốn điều chỉnh</td><td></td></tr></table>"""
S[3] = page(3, 'PHIÊN FLOW #1', 'Phiên Flow đầu tiên: 45 phút', f"""
<div class="lead">Dành 30 đến 45 phút cho việc đã khoanh hôm qua. Mười đến mười lăm phút đầu thường khó tập trung nhất, cứ tiếp tục và không kiểm tra điện thoại.</div>
<div class="box"><div class="sec">Chuẩn bị trước khi bắt đầu</div>
{C('Tắt thông báo điện thoại, đóng các tab không liên quan')}
{C('Báo đồng nghiệp hoặc gia đình: tôi cần 45 phút không bị gọi')}
{C('Chọn cách tự kiểm tra trong lúc làm (đọc lại, đối chiếu số liệu)')}
<div class="q">Trong 45 phút, tôi sẽ hoàn thành:</div>{L(2)}
<div style="font-size:8.5pt;color:#6b5b5a;margin-top:1.5mm">Ví dụ mục tiêu rõ: "viết xong phần phân tích chi phí của báo cáo", thay vì "làm báo cáo".</div></div>
{log(1)}
<div class="soft"><div class="sec">Ghi chú nhanh trong lúc làm (ý chợt đến, việc cần làm sau)</div>{L(4)}</div>
""", '"Phiên 1: ... phút, gián đoạn ... lần, cảm nhận: ..."')

S[4] = page(4, 'PHIÊN FLOW #2', 'Phiên thứ hai vào nhịp nhanh hơn', f"""
<div class="lead">Mở lại nhật ký phiên 1, chọn đúng một điều để điều chỉnh, rồi làm phiên thứ hai trong 30 đến 45 phút.</div>
<div class="soft"><div class="sec">Điều tôi điều chỉnh hôm nay (chọn một)</div>
<div class="grid2">{C('Đổi sang khung giờ yên tĩnh hơn')}{C('Viết mục tiêu cụ thể hơn')}{C('Cất điện thoại ra khỏi tầm nhìn')}{C('Đổi sang việc khác để thử')}</div>
{C('Khác: ..................................................................')}</div>
<div class="box"><div class="sec">Mục tiêu phiên 2</div>{L(2)}</div>
{log(2)}
<table><tr><th style="width:42%">So sánh</th><th>Phiên 1</th><th>Phiên 2</th></tr>
<tr><td>Số phút tập trung</td><td></td><td></td></tr><tr><td>Số lần gián đoạn</td><td></td><td></td></tr></table>
""", '"Hôm nay tôi điều chỉnh ..., kết quả ..."')

S[5] = page(5, 'CHỌN MỘT ĐIỀU CHỈNH', 'Một thay đổi cho góc làm việc', f"""
<div class="lead">Chấm mức ảnh hưởng của từng yếu tố trong hai phiên vừa qua (1: ít, 5: nhiều), rồi chọn đúng một yếu tố để thay đổi ngay hôm nay. Thời lượng: khoảng 15 phút.</div>
<table><tr><th style="width:6%">#</th><th style="width:30%">Yếu tố</th><th>Cách điều chỉnh gợi ý</th><th style="width:17%">Mức 1 đến 5</th></tr>
<tr><td>1</td><td>Thông báo điện thoại</td><td>Bật chế độ tập trung trong khung giờ làm việc sâu</td><td></td></tr>
<tr><td>2</td><td>Làm nhiều việc cùng lúc</td><td>Chỉ mở một ứng dụng hoặc một tab</td><td></td></tr>
<tr><td>3</td><td>Mục tiêu mơ hồ</td><td>Viết mục tiêu cụ thể trước khi bắt đầu</td><td></td></tr>
<tr><td>4</td><td>Việc quá quen</td><td>Thêm thử thách, ví dụ rút ngắn thời hạn</td><td></td></tr>
<tr><td>5</td><td>Việc quá lớn</td><td>Chia thành các bước nhỏ</td><td></td></tr></table>
<div class="box"><div class="sec">Yếu tố tôi chọn: số ......</div>
<div class="q">Tôi sẽ điều chỉnh bằng cách:</div>{L(2)}
<div class="q">Áp dụng bắt đầu từ (ngày, giờ):</div>{L(1)}</div>
<div class="soft"><div class="sec">Ghi chú sau khi áp dụng</div>{L(2)}</div>
""", 'Bình luận số thứ tự yếu tố bạn chọn (từ 1 đến 5) và cách bạn điều chỉnh.')

S[6] = page(6, 'ĐO LẠI TUẦN', 'Tuần này bạn có bao&nbsp;nhiêu phút&nbsp;Flow', f"""
<div class="lead">Nhìn lại tuần bằng con số, không chỉ bằng cảm nhận. Con số lớn hay nhỏ không quan trọng bằng việc bạn đã đo được. Thời lượng: khoảng 20 phút.</div>
<table><tr><th style="width:40%">Phiên</th><th>Số phút tập trung</th><th>Số lần gián đoạn</th></tr>
<tr><td>Phiên 1 (Ngày 3)</td><td></td><td></td></tr><tr><td>Phiên 2 (Ngày 4)</td><td></td><td></td></tr>
<tr><td><b>Tổng</b></td><td></td><td></td></tr></table>
<div class="box"><div class="q" style="margin-top:0">1. Trong ba điều kiện cốt lõi, điều kiện nào tôi làm tốt nhất, điều kiện nào còn thiếu?</div>{L(2)}
<div class="q">2. Gián đoạn chủ yếu đến từ bên ngoài hay từ bên trong?</div>{L(2)}
<div class="q">3. Việc nào trong bản đồ Ngày 2 đã chuyển vùng?</div>{L(2)}</div>
<div class="soft"><div class="sec">Một điều tôi nhận ra về cách mình làm việc</div>{L(2)}</div>
""", '"Tổng phút Flow tuần này: ...", kèm một điều bạn nhận ra về cách mình làm việc.')

days = ['T2','T3','T4','T5','T6','T7','CN']
slots = ['Sáng sớm','Buổi sáng','Đầu giờ chiều','Buổi chiều','Buổi tối']
grid = '<table><tr><th style="width:18%">Khung giờ</th>' + ''.join(f'<th style="text-align:center">{d}</th>' for d in days) + '</tr>' + ''.join(f'<tr><td style="font-size:9pt">{s}</td>' + ''.join('<td style="border-left:0.8pt solid #D9C3C0;height:12.5mm"></td>' for _ in days) + '</tr>' for s in slots) + '</table>'
S[7] = page(7, 'GIỮ NHỊP LÂU DÀI', 'Đặt lịch Flow cố định mỗi tuần', f"""
<div class="lead">Đánh dấu 3 khung giờ mỗi tuần, mỗi khung 45 đến 60 phút, vào lúc ít bị gián đoạn nhất. Sau đó đưa ba khung giờ này vào lịch làm việc như một cuộc hẹn lặp lại hằng tuần.</div>
{grid}
<table><tr><th style="width:12%">#</th><th>Ngày và giờ</th><th>Việc dự kiến cho khung giờ này</th></tr>
<tr><td>1</td><td></td><td></td></tr><tr><td>2</td><td></td><td></td></tr><tr><td>3</td><td></td><td></td></tr></table>
<div class="soft"><div class="sec">Nhìn lại 15 phút mỗi tối Chủ Nhật</div>
{C('Cộng số phút Flow của tuần vừa qua')}{C('Chọn việc cho ba khung giờ tuần tới')}{C('Điều chỉnh một yếu tố gây gián đoạn nếu cần')}</div>
<div><div class="sec">Điều tôi muốn giữ lại sau thử thách</div>{L(2)}</div>
""", '"Lịch Flow của tôi: ...". Đây là check-in cuối cùng của thử thách.')

NAMES = {1:'ngay-1',2:'ngay-2',3:'ngay-3',4:'ngay-4',5:'ngay-5',6:'ngay-6',7:'ngay-7'}
async def main():
    os.makedirs(os.path.join(D,'pdf'), exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page()
        for d,h in S.items():
            f = os.path.join(D, f'sheet_{d}.html'); open(f,'w').write(h)
            await pg.goto('file://'+f); await pg.wait_for_load_state('networkidle'); await pg.evaluate('document.fonts.ready')
            await pg.pdf(path=os.path.join(D,'pdf',f'10XHub_Flow7Ngay_PhieuNgay{d}_{NAMES[d]}.pdf'), format='A4', print_background=True, prefer_css_page_size=True)
        await b.close()
asyncio.run(main())
