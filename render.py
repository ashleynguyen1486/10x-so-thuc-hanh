import asyncio, os
from playwright.async_api import async_playwright

D = os.path.dirname(os.path.abspath(__file__))
W, H = 1920, 1080
K = '#862222'      # 10X Excellence Hub red (from PDF series)
CR = '#FBF3F2'     # cream / light pink
GR = '#F1E4E2'
INK = '#231F20'
NB = ' '

def nb(s):
    for p in ['THỜI GIAN', 'THÓI QUEN', '7 NGÀY', '45 PHÚT', 'BAO NHIÊU', 'LÀM VIỆC', 'MỖI TUẦN', 'CỐ ĐỊNH', 'NHANH HƠN', 'THỬ THÁCH', 'BẮT ĐẦU', 'ĐẦU TIÊN', 'HOÀN THÀNH', 'GẦN NHẤT', 'THAY ĐỔI', 'PHIÊN FLOW', 'VÙNG FLOW', 'NGÀY FLOW', 'PHÚT FLOW', 'LỊCH FLOW', 'THỨ HAI', 'VÀO NHỊP']:
        s = s.replace(p, p.replace(' ', NB))
    return s

def img(name):
    return f'img/p_{name}.jpg'

BASE = f"""
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:{W}px;height:{H}px;overflow:hidden;font-family:'Be Vietnam Pro',sans-serif;color:{INK};background:{CR}}}
.kick{{font-size:30px;font-weight:700;letter-spacing:.2em;text-transform:uppercase}}
.ttl{{font-weight:800;line-height:1.24;letter-spacing:-0.012em;text-transform:uppercase}}
.body{{font-size:36px;line-height:1.5}}
.rule{{width:120px;height:4px;background:#fff}} .rule.dk{{background:{K}}}
.fill{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
.mark{{font-size:24px;font-weight:700;letter-spacing:.18em}}
</style>
<script>
function fit(el,maxLines){{
  const box=el.parentElement; const maxW=el.clientWidth*0.93;
  let start=parseFloat(getComputedStyle(el).fontSize); const min=start*0.52;
  const ls=parseFloat(getComputedStyle(el).letterSpacing)/start||0;
  const p=document.createElement('span'); p.style.cssText='position:absolute;visibility:hidden;white-space:nowrap;font-weight:800;text-transform:uppercase';
  p.style.fontFamily=getComputedStyle(el).fontFamily; document.body.appendChild(p);
  const txt=el.dataset.text; const words=txt.split(' ');
  const wOf=(s,sz)=>{{p.style.fontSize=sz+'px';p.style.letterSpacing=(ls*sz)+'px';p.textContent=s;return p.getBoundingClientRect().width}};
  for(let lines=1;lines<=maxLines;lines++){{
    for(let sz=start;sz>=min;sz-=Math.max(2,Math.round(start*0.035))){{
      // greedy balanced: try all splits for 2/3 lines
      let best=null;
      const n=words.length;
      const cand=[];
      if(lines===1) cand.push([words.join(' ')]);
      if(lines===2) for(let i=1;i<n;i++) cand.push([words.slice(0,i).join(' '),words.slice(i).join(' ')]);
      if(lines===3) for(let i=1;i<n-1;i++) for(let j=i+1;j<n;j++) cand.push([words.slice(0,i).join(' '),words.slice(i,j).join(' '),words.slice(j).join(' ')]);
      for(const c of cand){{
        const ws=c.map(s=>wOf(s,sz)); if(Math.max(...ws)>maxW) continue;
        if(c.some(s=>s.split(' ').length===1 && wOf(s,sz)<maxW*0.55 && c.length>1)) continue;
        const cost=ws.reduce((a,b,k)=>a+((maxW-b)/maxW)**2*(k===ws.length-1?18:130),0);
        if(!best||cost<best.cost) best={{c,cost}};
      }}
      if(best){{el.style.fontSize=sz+'px';el.style.letterSpacing=(ls*sz)+'px';el.innerHTML=best.c.join('<br>');p.remove();return;}}
    }}
  }}
  el.textContent=txt; p.remove();
}}
window.addEventListener('load',()=>document.fonts.ready.then(()=>{{document.querySelectorAll('[data-text]').forEach(e=>fit(e,+e.dataset.lines||3));document.body.dataset.ready=1}}));
</script>
"""

def T(text, size, color, lines=3, extra=''):
    return f'<div class="ttl" data-lines="{lines}" data-text="{nb(text)}" style="font-size:{size}px;color:{color};width:100%;{extra}">{nb(text)}</div>'

L = {}

# 0 Announcement: red block left 58%, photo right
L[0] = lambda: f"""
<div style="position:absolute;left:0;top:0;width:58%;height:100%;background:{K};padding:130px 120px;display:flex;flex-direction:column;justify-content:center;gap:44px;color:#fff">
  <div class="kick" style="color:#fff;opacity:.85">CÔNG THỨC #0021</div>
  {T('THỬ THÁCH FLOW 7 NGÀY BẮT ĐẦU',112,'#fff',3)}
  <div class="rule"></div>
  <div class="body" style="color:#fff;font-size:38px">Mỗi ngày một việc, 10 đến 45 phút.<br>Bắt đầu thứ Hai, check-in ngay trên 10X&nbsp;Excellence&nbsp;Hub.</div>
</div>
<div style="position:absolute;right:0;top:0;width:42%;height:100%;overflow:hidden"><img class="fill" src="{img('1497215728101-856f4ea42174')}"></div>
<img src="img/logo_w_crop.png" style="position:absolute;left:120px;bottom:60px;height:120px">
"""

# 1 Day 1: full-bleed photo, red gradient bottom
L[1] = lambda: f"""
<img class="fill" src="{img('1431540015161-0bf868a2d407')}">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(134,34,34,0) 25%,rgba(134,34,34,.88) 62%,{K} 100%)"></div>
<div style="position:absolute;left:150px;right:150px;bottom:110px;display:flex;flex-direction:column;gap:30px;color:#fff">
  <div class="kick">NGÀY 1 / 7 · NHẬN DIỆN FLOW</div>
  {T('LẦN GẦN NHẤT BẠN QUÊN THỜI GIAN',128,'#fff',2)}
  <div class="body" style="color:#fff">Nhớ lại một lần làm việc mà quên nhìn đồng hồ. Điều gì giúp bạn tập trung như vậy?</div>
</div>
<img src="img/logo_w_crop.png" style="position:absolute;left:150px;top:60px;height:120px">
"""

# 2 Day 2: cream, title left, 2x2 matrix right
def cell(lbl, sub, bg, fg, border=''):
    return f'<div style="background:{bg};color:{fg};border-radius:18px;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:12px;padding:0 24px;text-align:center;{border}"><div style="font-size:50px;font-weight:800;letter-spacing:.04em">{lbl}</div><div style="font-size:28px;line-height:1.35;opacity:.88">{sub}</div></div>'
L[2] = lambda: f"""
<div style="position:absolute;left:130px;top:0;bottom:0;width:760px;display:flex;flex-direction:column;justify-content:center;gap:40px">
  <div class="kick" style="color:{K}">NGÀY 2 / 7 · BẢN ĐỒ CÔNG VIỆC</div>
  {T('VIỆC NÀO ĐANG Ở VÙNG FLOW?',104,INK,3)}
  <div class="rule dk"></div>
  <div class="body">Đặt 5 việc chiếm nhiều thời gian nhất của bạn vào ma trận Thử thách và Kỹ năng.</div>
  <img src="img/logo_c_crop.png" style="align-self:flex-start;margin-top:10px;height:120px">
</div>
<div style="position:absolute;right:130px;top:120px;bottom:120px;width:800px;display:flex;gap:24px">
  <div style="writing-mode:vertical-rl;transform:rotate(180deg);font-size:26px;font-weight:700;letter-spacing:.2em;color:{K};text-align:center">THỬ THÁCH →</div>
  <div style="flex:1;display:flex;flex-direction:column;gap:24px">
    <div style="flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:24px">
      {cell('LO ÂU','Thử&nbsp;thách&nbsp;cao, kỹ&nbsp;năng&nbsp;thấp','#E4D6D4',INK)}
      {cell('FLOW','Thử&nbsp;thách&nbsp;cao, kỹ&nbsp;năng&nbsp;cao',K,'#fff')}
      {cell('VÔ CẢM','Thử&nbsp;thách&nbsp;thấp, kỹ&nbsp;năng&nbsp;thấp','#EDE3E1',INK)}
      {cell('CHÁN','Thử&nbsp;thách&nbsp;thấp, kỹ&nbsp;năng&nbsp;cao','#fff',K,f'border:4px solid {K}')}
    </div>
    <div style="font-size:26px;font-weight:700;letter-spacing:.2em;color:{K};text-align:center">KỸ NĂNG →</div>
  </div>
</div>
"""

# 3 Day 3: big timer ring left, title right
L[3] = lambda: f"""
<div style="position:absolute;left:150px;top:0;bottom:0;width:640px;display:flex;align-items:center;justify-content:center">
  <div style="width:620px;height:620px;border-radius:50%;background:conic-gradient({K} 0 75%, {GR} 75% 100%);display:flex;align-items:center;justify-content:center">
    <div style="width:500px;height:500px;border-radius:50%;background:{CR};display:flex;flex-direction:column;align-items:center;justify-content:center">
      <div style="font-size:260px;font-weight:800;color:{K};line-height:1">45</div>
      <div style="font-size:44px;font-weight:700;letter-spacing:.2em;color:{K}">PHÚT</div>
    </div>
  </div>
</div>
<div style="position:absolute;left:900px;right:140px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center;gap:38px">
  <div class="kick" style="color:{K}">NGÀY 3 / 7 · PHIÊN FLOW #1</div>
  {T('PHIÊN FLOW ĐẦU TIÊN: 45 PHÚT',104,INK,3)}
  <div class="rule dk"></div>
  <div class="body">Tắt thông báo. Viết một mục tiêu cụ thể. Tự kiểm tra kết quả ngay trong lúc làm.</div>
  <img src="img/logo_c_crop.png" style="align-self:flex-start;height:120px">
</div>
"""

# 4 Day 4: solid red, Q&A
def qa(q):
    return f'<div style="display:flex;gap:26px;align-items:flex-start"><div style="width:60px;height:4px;background:#fff;margin-top:26px;flex:0 0 auto"></div><div style="font-size:38px;line-height:1.4;color:#fff">{q}</div></div>'
L[4] = lambda: f"""
<div style="position:absolute;inset:0;background:{K};padding:110px 150px;display:flex;flex-direction:column;justify-content:center;gap:40px;color:#fff">
  <div class="kick">NGÀY 4 / 7 · HỎI VÀ ĐÁP</div>
  {T('PHIÊN THỨ HAI VÀO NHỊP NHANH HƠN',116,'#fff',2)}
  <div style="display:flex;flex-direction:column;gap:26px;margin-top:10px">
    {qa('Phiên đầu chưa vào được Flow: hoàn toàn bình thường.')}
    {qa('Bị gián đoạn: ghi lại nguồn, đổi sang khung giờ yên tĩnh hơn.')}
    {qa('Giữ việc cũ để so tiến bộ, hoặc đổi việc để thử nghiệm.')}
  </div>
  <img src="img/logo_w_crop.png" style="align-self:flex-start;height:110px">
</div>
"""

# 5 Day 5: title top, 5 cards bottom
def card(n, t, s, shade):
    return f'<div style="flex:1;background:{shade};border-radius:20px;padding:40px 32px;display:flex;flex-direction:column;justify-content:space-between;color:#fff"><div style="font-size:84px;font-weight:800;line-height:1">0{n}</div><div style="display:flex;flex-direction:column;gap:16px"><div style="font-size:38px;font-weight:700;line-height:1.25">{t}</div><div style="width:60px;height:3px;background:#fff"></div><div style="font-size:30px;line-height:1.4;opacity:.95">{s}</div></div></div>'
L[5] = lambda: f"""
<div style="position:absolute;inset:0;padding:100px 130px;display:flex;flex-direction:column;gap:48px">
  <div style="display:flex;justify-content:space-between;align-items:center"><div class="kick" style="color:{K}">NGÀY 5 / 7 · CHỌN MỘT ĐIỀU CHỈNH</div><img src="img/logo_c_crop.png" style="height:100px"></div>
  {T('MỘT THAY ĐỔI CHO GÓC LÀM VIỆC',110,INK,2)}
  <div style="flex:1;display:flex;gap:24px;min-height:44%">
    {card(1,'Thông báo điện&nbsp;thoại','Bật chế độ tập&nbsp;trung','#B4545A')}
    {card(2,'Nhiều việc cùng&nbsp;lúc','Chỉ mở một tab','#A0434A')}
    {card(3,'Mục tiêu mơ&nbsp;hồ','Viết mục tiêu cụ&nbsp;thể','#8F343A')}
    {card(4,'Việc quá&nbsp;quen','Rút ngắn thời&nbsp;hạn','#86292F')}
    {card(5,'Việc quá lớn','Chia thành bước&nbsp;nhỏ',K)}
  </div>
</div>
"""

# 6 Day 6: photo left 40%, cream right with questions
L[6] = lambda: f"""
<div style="position:absolute;left:0;top:0;width:40%;height:100%;overflow:hidden"><img class="fill" src="{img('1486406146926-c627a92ad1ab')}"><div style="position:absolute;inset:0;background:rgba(134,34,34,.35)"></div></div>
<div style="position:absolute;left:40%;right:0;top:0;bottom:0;padding:100px 130px;display:flex;flex-direction:column;justify-content:center;gap:36px">
  <div class="kick" style="color:{K}">NGÀY 6 / 7 · ĐO LẠI TUẦN</div>
  {T('TUẦN NÀY BẠN CÓ BAO NHIÊU PHÚT FLOW',98,INK,3)}
  <div class="rule dk"></div>
  <div style="display:flex;flex-direction:column;gap:20px;font-size:34px;line-height:1.4">
    <div><b style="color:{K}">01</b>&nbsp;&nbsp;Điều kiện nào bạn làm tốt nhất?</div>
    <div><b style="color:{K}">02</b>&nbsp;&nbsp;Gián đoạn đến từ bên ngoài hay bên trong?</div>
    <div><b style="color:{K}">03</b>&nbsp;&nbsp;Việc nào đã chuyển vùng?</div>
  </div>
  <img src="img/logo_c_crop.png" style="align-self:flex-start;height:110px">
</div>
"""

# 7 Day 7: weekly calendar grid
def day(lbl, on):
    blk = f'<div style="height:120px;border-radius:14px;background:{K};color:#fff;display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:700">FLOW</div>' if on else f'<div style="height:120px;border-radius:14px;border:3px dashed #D9C3C0"></div>'
    return f'<div style="flex:1;display:flex;flex-direction:column;gap:18px"><div style="text-align:center;font-size:30px;font-weight:700;color:{K};letter-spacing:.08em">{lbl}</div>{blk}<div style="height:70px;border-radius:14px;background:{GR}"></div><div style="height:70px;border-radius:14px;background:{GR}"></div></div>'
L[7] = lambda: f"""
<div style="position:absolute;inset:0;padding:100px 130px;display:flex;flex-direction:column;gap:46px">
  <div class="kick" style="color:{K}">NGÀY 7 / 7 · GIỮ NHỊP LÂU DÀI</div>
  {T('ĐẶT LỊCH FLOW CỐ ĐỊNH MỖI TUẦN',112,INK,2)}
  <div style="flex:1;display:flex;gap:22px;align-items:center;min-height:42%">
    {day('T2',True)}{day('T3',False)}{day('T4',True)}{day('T5',False)}{day('T6',True)}{day('T7',False)}{day('CN',False)}
  </div>
  <div style="display:flex;justify-content:space-between;align-items:center"><div class="body" style="font-size:32px">Ba khung giờ 45 đến 60 phút, đặt như một cuộc hẹn lặp lại hằng tuần.</div><img src="img/logo_c_crop.png" style="height:100px"></div>
</div>
"""

# 8 Recap: 7 checked circles timeline + skyline strip
def dot(n):
    return f'<div style="display:flex;flex-direction:column;align-items:center;gap:16px;z-index:1"><div style="width:130px;height:130px;border-radius:50%;background:{K};color:#fff;display:flex;align-items:center;justify-content:center;font-size:56px;font-weight:800;border:8px solid {CR}">{n}</div><div style="font-size:26px;font-weight:700;color:{K};letter-spacing:.1em">NGÀY {n}</div></div>'
L[8] = lambda: f"""
<div style="position:absolute;left:0;right:0;top:0;height:34%;overflow:hidden"><img class="fill" src="{img('1477959858617-67f85cf4f1df')}"><div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(134,34,34,.85),rgba(134,34,34,.25))"></div>
<div class="kick" style="position:absolute;left:130px;top:70px;color:#fff">TỔNG KẾT THỬ THÁCH · CÔNG THỨC #0021</div>
<img src="img/logo_w_crop.png" style="position:absolute;right:130px;top:50px;height:120px"></div>
<div style="position:absolute;left:130px;right:130px;top:34%;bottom:0;display:flex;flex-direction:column;justify-content:center;gap:60px">
  {T('7 NGÀY FLOW: GIỮ LẠI THÓI QUEN NÀO',108,INK,2)}
  <div style="position:relative;display:flex;justify-content:space-between">
    <div style="position:absolute;left:65px;right:65px;top:61px;height:8px;background:#D9C3C0"></div>
    {''.join(dot(i) for i in range(1,8))}
  </div>
</div>
"""

# 9 Badge
L[9] = lambda: f"""
<div style="position:absolute;inset:50px;border:6px solid {K};border-radius:28px"></div>
<div style="position:absolute;inset:74px;border:2px solid #D9C3C0;border-radius:20px"></div>
<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;gap:110px;padding:0 180px">
  <div style="flex:0 0 auto;width:440px;height:440px;border-radius:50%;background:{K};display:flex;flex-direction:column;align-items:center;justify-content:center;color:#fff;box-shadow:0 0 0 14px {CR},0 0 0 20px {K}">
    <div style="font-size:200px;font-weight:800;line-height:1">7</div>
    <div style="font-size:44px;font-weight:700;letter-spacing:.24em">NGÀY</div>
    <div style="font-size:30px;font-weight:600;letter-spacing:.3em;margin-top:8px;opacity:.9">FLOW</div>
  </div>
  <div style="flex:1;display:flex;flex-direction:column;gap:34px">
    <div class="kick" style="color:{K}">THẺ THÀNH TÍCH · CÔNG THỨC #0021</div>
    {T('HOÀN THÀNH THỬ THÁCH FLOW 7 NGÀY',104,INK,3)}
    <div class="rule dk"></div>
    <div class="body" style="font-size:34px">Ghi nhận thành viên đã check-in đủ 7 ngày luyện tập trạng thái Dòng chảy.</div>
    <img src="img/logo_c_crop.png" style="align-self:flex-start;height:110px">
  </div>
</div>
"""

NAMES = ['0_thong-bao', '1_ngay-1', '2_ngay-2', '3_ngay-3', '4_ngay-4', '5_ngay-5', '6_ngay-6', '7_ngay-7', '8_tong-ket', '9_the-thanh-tich']

CHECK = """
(()=>{const out=[];document.querySelectorAll('[data-text]').forEach(el=>{
 const r=document.createRange();r.selectNodeContents(el);
 const rects=[...r.getClientRects()].filter(q=>q.height>2&&q.width>1);
 const tops=[];rects.forEach(q=>{if(!tops.some(t=>Math.abs(t-q.top)<4))tops.push(q.top)});
 const b=el.getBoundingClientRect();const over=rects.some(q=>q.right>b.right+2||q.left<b.left-2);
 out.push({lines:tops.length,over,html:el.innerHTML,size:el.style.fontSize});});
 const docOver=document.documentElement.scrollHeight>window.innerHeight+2||document.documentElement.scrollWidth>window.innerWidth+2;
 return {titles:out,docOver};})()
"""

async def main():
    os.makedirs(os.path.join(D, 'out'), exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': W, 'height': H}, device_scale_factor=2)
        for i, n in enumerate(NAMES):
            html = f'<!doctype html><html><head><meta charset="utf-8">{BASE}</head><body>{L[i]()}</body></html>'
            f = os.path.join(D, f'{n}.html')
            open(f, 'w').write(html)
            await pg.goto('file://' + f)
            await pg.wait_for_selector('body[data-ready="1"]', timeout=20000)
            await pg.wait_for_timeout(300)
            res = await pg.evaluate(CHECK)
            print(n, res)
            await pg.screenshot(path=os.path.join(D, 'out', f'10XHub_Flow7Ngay_{n}.png'))
        await b.close()

asyncio.run(main())
