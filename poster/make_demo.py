# -*- coding: utf-8 -*-
# 余裕乗り換えナビ v6 デモ動画（字幕つきスライド）用フレーム生成
from PIL import Image, ImageDraw, ImageFont
import os

D = r'C:\Users\seiya\OneDrive\Desktop\WEB3課題\gonta0506-web3ai-2026\poster'
OUT = os.path.join(D, 'frames')
os.makedirs(OUT, exist_ok=True)

W, H = 1080, 1350          # 縦型（Discord/SNS向け）
BG = (15, 15, 26)
INDIGO = (129, 140, 248)
WHITE = (255, 255, 255)
GRAY = (148, 163, 184)

def font(sz, bold=True):
    for p in [r'C:\Windows\Fonts\YuGothB.ttc', r'C:\Windows\Fonts\meiryob.ttc',
              r'C:\Windows\Fonts\YuGothM.ttc', r'C:\Windows\Fonts\meiryo.ttc',
              r'C:\Windows\Fonts\msgothic.ttc']:
        if os.path.exists(p):
            try: return ImageFont.truetype(p, sz)
            except Exception: pass
    return ImageFont.load_default()

F_T   = font(52)
F_S   = font(30)
F_TAG = font(26)

SCENES = [
    ('sc_plan.png',   '① 毎朝の「何時に起きる？」を自動で',
                      '徒歩・準備時間を登録 → 起きる/家を出る/乗る電車を逆算', 4.0),
    ('sc_reco.png',   '② いま出発モード：座れる一本をライブ判定',
                      '走らずに乗れる電車と、発車までのカウントダウン', 3.6),
    ('sc_record.png', '③ マイ精度：自分の記録で確保率を補正',
                      '「記録4件から+4%補正済み」と根拠まで表示', 3.6),
    ('sc_mission.png','④ 座れた30分を、使える時間に',
                      '座れたら何をするかを先に決める30分ミッション', 3.2),
]

def build(src, title, sub, idx):
    canvas = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(canvas)
    # header bar
    d.rectangle([0, 0, W, 190], fill=(26, 26, 46))
    d.text((60, 42), title, font=F_T, fill=WHITE)
    d.text((60, 118), sub, font=F_S, fill=GRAY)
    # screenshot
    im = Image.open(os.path.join(D, src)).convert('RGB')
    maxw, maxh = W - 120, H - 300
    r = min(maxw / im.width, maxh / im.height)
    im = im.resize((int(im.width * r), int(im.height * r)), Image.LANCZOS)
    x = (W - im.width) // 2
    y = 190 + (H - 190 - 70 - im.height) // 2
    # border
    d.rectangle([x - 4, y - 4, x + im.width + 4, y + im.height + 4], outline=(60, 64, 110), width=3)
    canvas.paste(im, (x, y))
    # footer
    d.text((60, H - 58), '余裕乗り換えナビ v6  /  prototype-pi-six.vercel.app', font=F_TAG, fill=INDIGO)
    return canvas

FPS = 30
n = 0
for i, (src, t, s, dur) in enumerate(SCENES):
    fr = build(src, t, s, i)
    for _ in range(int(dur * FPS)):
        fr.save(os.path.join(OUT, f'f_{n:05d}.png')); n += 1

# 最後: まとめカード
end = Image.new('RGB', (W, H), BG)
d = ImageDraw.Draw(end)
d.text((60, 300), '余裕乗り換えナビ v6', font=font(64), fill=WHITE)
d.text((60, 400), 'ギリギリ乗り換えを、もうやめよう。', font=F_T, fill=INDIGO)
for j, line in enumerate([
    '・原体験：乗り換えダッシュ／毎朝の起床計算',
    '・顧客：毎日電車で通学する大学生',
    '・v1 → v6：逆算プラン＋30分ミッションまで',
    '・失敗：作った自分が3日で記録を忘れた',
    '　→「記録させる」より「思い出させる」へ',
]):
    d.text((60, 540 + j * 62), line, font=F_S, fill=GRAY)
d.text((60, 900), 'その場で使えます', font=F_S, fill=WHITE)
d.text((60, 950), 'https://prototype-pi-six.vercel.app/', font=font(34), fill=INDIGO)
d.text((60, 1030), 'github.com/shimadakume-netizen/gonta0506-web3ai-2026', font=F_TAG, fill=GRAY)
for _ in range(int(4.0 * FPS)):
    end.save(os.path.join(OUT, f'f_{n:05d}.png')); n += 1

print('frames:', n, '/ fps', FPS, '/ duration', round(n / FPS, 1), 's')
