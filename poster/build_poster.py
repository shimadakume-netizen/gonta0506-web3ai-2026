# -*- coding: utf-8 -*-
# CHIBATECH PROTOTYPE 用 A4縦ポスター生成（画像・QRをbase64で埋め込み → 自己完結HTML）
import io, base64, os

D = os.path.dirname(os.path.abspath(__file__))
def b64(fn):
    with open(os.path.join(D, fn), 'rb') as f:
        return base64.b64encode(f.read()).decode('ascii')

SHOT_HOME    = b64('shot_hero.png')
SHOT_MISSION = b64('shot_mission.png')
QR_PRODUCT   = b64('qr_product.png')
QR_GITHUB    = b64('qr_github.png')

HTML = f'''<!DOCTYPE html>
<html lang="ja"><head><meta charset="UTF-8">
<title>余裕乗り換えナビ — CHIBATECH PROTOTYPE ポスター</title>
<style>
@page {{ size: A4 portrait; margin: 0; }}
*{{box-sizing:border-box;margin:0;padding:0;}}
:root{{
  --ink:#141726; --ink2:#3d4460; --muted:#6b7392;
  --indigo:#4f46e5; --indigo-l:#6366f1; --indigo-p:#eef0ff;
  --green:#10b981; --amber:#f59e0b; --red:#ef4444;
  --line:#dfe3f2; --bg:#ffffff;
}}
html,body{{width:210mm;height:297mm;overflow:hidden;}}
body{{
  font-family:"Yu Gothic UI","Yu Gothic","Hiragino Kaku Gothic ProN","Noto Sans JP","Meiryo",sans-serif;
  color:var(--ink); background:var(--bg);
  -webkit-print-color-adjust:exact; print-color-adjust:exact;
  display:flex; flex-direction:column;
}}
/* ── header ── */
.hd{{
  flex:0 0 auto;
  background:linear-gradient(115deg,#1e1b4b 0%,#4f46e5 55%,#6366f1 100%);
  color:#fff; padding:6mm 9mm 5mm; position:relative; overflow:hidden;
}}
.hd::after{{content:'🚃';position:absolute;right:-4mm;bottom:-8mm;font-size:34mm;opacity:.13;transform:rotate(-12deg);}}
.hd-top{{display:flex;align-items:center;gap:3mm;margin-bottom:1.5mm;}}
.badge{{background:rgba(255,255,255,.22);border:.4mm solid rgba(255,255,255,.5);border-radius:99px;
  font-size:2.9mm;font-weight:800;padding:.8mm 3mm;letter-spacing:.06em;}}
.cat{{font-size:2.9mm;font-weight:700;letter-spacing:.14em;opacity:.9;}}
.ttl{{font-size:11mm;font-weight:900;letter-spacing:-.01em;line-height:1.04;}}
.sub{{font-size:3.9mm;font-weight:700;margin-top:1.3mm;opacity:.96;}}
.who{{margin-top:1.9mm;font-size:2.8mm;opacity:.88;letter-spacing:.04em;}}
/* ── body grid ── */
.wrap{{flex:1 1 auto;min-height:0;padding:4mm 9mm 0;display:flex;flex-direction:column;gap:2.8mm;}}
.row{{display:grid;gap:3.4mm;}}
.r2{{grid-template-columns:1fr 1fr;}}
.rmain{{grid-template-columns:1.02fr .98fr;}}
.card{{border:.35mm solid var(--line);border-radius:2.4mm;padding:3mm 3.5mm;background:#fff;}}
.card.accent{{background:var(--indigo-p);border-color:#c9cffb;}}
.card.warn{{background:#fff8ec;border-color:#f6d9a6;}}
.h{{display:flex;align-items:center;gap:2mm;margin-bottom:2.2mm;}}
.no{{background:var(--indigo);color:#fff;font-size:2.7mm;font-weight:900;border-radius:1.2mm;
  padding:.7mm 1.8mm;letter-spacing:.06em;}}
.no.w{{background:var(--amber);}}
.no.g{{background:var(--green);}}
.ht{{font-size:4.1mm;font-weight:900;letter-spacing:.02em;}}
li{{list-style:none;font-size:3.02mm;line-height:1.55;color:var(--ink2);
  padding-left:4.2mm;position:relative;margin-bottom:1.1mm;}}
li::before{{content:'';position:absolute;left:.6mm;top:1.5mm;width:1.6mm;height:1.6mm;
  border-radius:50%;background:var(--indigo-l);}}
li b{{color:var(--ink);font-weight:800;}}
.quote{{font-size:3.0mm;line-height:1.5;color:var(--ink2);background:#fff;border-left:1mm solid var(--amber);
  padding:1.6mm 2.4mm;border-radius:0 1.4mm 1.4mm 0;margin-bottom:1.4mm;}}
.quote b{{color:var(--ink);}}
/* VPC */
.vpc{{display:grid;grid-template-columns:1fr 1fr;gap:2mm;margin-top:.6mm;}}
.vp{{border-radius:1.8mm;padding:2.2mm 2.6mm;}}
.vp.pain{{background:#fff1f1;border:.3mm solid #f7c9c9;}}
.vp.gain{{background:#eefaf4;border:.3mm solid #b9e6d1;}}
.vp-l{{font-size:2.5mm;font-weight:900;letter-spacing:.1em;margin-bottom:1mm;}}
.vp.pain .vp-l{{color:#d33;}} .vp.gain .vp-l{{color:#0a8a5f;}}
.vp p{{font-size:2.95mm;line-height:1.5;color:var(--ink2);}}
/* product */
.shot{{width:100%;border-radius:2mm;border:.35mm solid var(--line);display:block;}}
.shot.hero{{max-height:84mm;object-fit:cover;object-position:top;}}
.shot.mini{{max-height:33mm;object-fit:cover;object-position:top;}}
.feat{{display:flex;flex-direction:column;gap:1.4mm;margin-top:1.6mm;}}
.f{{display:flex;gap:2mm;align-items:flex-start;background:#fafbff;border:.3mm solid #e6e9f8;
  border-radius:1.8mm;padding:1.5mm 2.1mm;}}
.f-i{{font-size:4.4mm;line-height:1;flex-shrink:0;}}
.f-t{{font-size:3.1mm;font-weight:900;margin-bottom:.5mm;}}
.f-d{{font-size:2.75mm;line-height:1.45;color:var(--muted);}}
.evo{{display:flex;align-items:center;gap:1.4mm;margin-top:2mm;flex-wrap:wrap;}}
.ev{{font-size:2.5mm;font-weight:800;color:var(--muted);background:#f2f4fd;border-radius:99px;padding:.7mm 2mm;}}
.ev.on{{background:var(--indigo);color:#fff;}}
.arrow{{font-size:2.6mm;color:#b9c0dd;}}
/* footer */
.ft{{flex:0 0 auto;margin-top:auto;background:#141726;color:#fff;padding:3.6mm 9mm;display:flex;align-items:center;gap:5mm;}}
.qr{{display:flex;align-items:center;gap:2.4mm;}}
.qr img{{width:19mm;height:19mm;background:#fff;padding:.9mm;border-radius:1.4mm;display:block;}}
.qr-t{{font-size:2.7mm;font-weight:900;letter-spacing:.05em;margin-bottom:.7mm;}}
.qr-u{{font-size:2.35mm;color:#a8b0d0;word-break:break-all;line-height:1.35;max-width:44mm;}}
.ft-msg{{margin-left:auto;text-align:right;}}
.ft-msg .m1{{font-size:3.9mm;font-weight:900;line-height:1.35;}}
.ft-msg .m2{{font-size:2.7mm;color:#a8b0d0;margin-top:1mm;}}
</style></head>
<body>

<div class="hd">
  <div class="hd-top">
    <span class="badge">v6</span>
    <span class="cat">A-1 プロダクト系 ／ CHIBATECH PROTOTYPE</span>
  </div>
  <div class="ttl">余裕乗り換えナビ</div>
  <div class="sub">ギリギリ乗り換えを、もうやめよう。— 通学2時間を「座れて・使える」時間に</div>
  <div class="who">Discord: gonta0506 ／ GitHub: shimadakume-netizen ／ 静的Webアプリ（インストール不要・スマホ完結）</div>
</div>

<div class="wrap">

  <div class="row r2">
    <div class="card">
      <div class="h"><span class="no">01</span><span class="ht">現場で実際に困ったこと</span></div>
      <ul>
        <li>乗り換えの接続時間が短すぎて、ホームまで<b>毎回走る</b>（バグ#2）</li>
        <li>朝、<b>何時に起きれば間に合うか</b>を毎日あたまで計算するのが面倒（バグ#18）</li>
        <li>往復2時間の通学が、混雑で<b>ただ消えていく</b>（バグ#3・#5）</li>
      </ul>
    </div>
    <div class="card accent">
      <div class="h"><span class="no">02</span><span class="ht">誰の、何を解決するか</span></div>
      <ul><li>顧客：<b>毎日電車で通学する大学生</b>（片道1時間・乗換あり）</li></ul>
      <div class="vpc">
        <div class="vp pain"><div class="vp-l">★ PAIN</div><p>乗り換えダッシュ。毎回ギリギリで、着いた時点で消耗している。</p></div>
        <div class="vp gain"><div class="vp-l">★ GAIN</div><p>座って余裕を持って移動し、その時間を勉強や仮眠に使いたい。</p></div>
      </div>
    </div>
  </div>

  <div class="row rmain">
    <div class="card">
      <div class="h"><span class="no">03</span><span class="ht">プロダクト v6</span></div>
      <img class="shot hero" src="data:image/png;base64,{SHOT_HOME}" alt="余裕乗り換えナビ v6 画面">
      <div class="evo">
        <span class="ev">v1 ルート比較</span><span class="arrow">▶</span>
        <span class="ev">v3 いま出発</span><span class="arrow">▶</span>
        <span class="ev">v4 マイ通学</span><span class="arrow">▶</span>
        <span class="ev">v5 マイ精度</span><span class="arrow">▶</span>
        <span class="ev on">v6 逆算＋ミッション</span>
      </div>
    </div>
    <div class="card">
      <div class="h"><span class="no g">04</span><span class="ht">v6 の中身</span></div>
      <div class="feat">
        <div class="f"><span class="f-i">🌅</span><div><div class="f-t">出発逆算プラン</div>
          <div class="f-d">徒歩・準備時間を登録すると「起きる→家を出る→乗る電車」を自動計算。家を出るまでを秒でカウントダウン。</div></div></div>
        <div class="f"><span class="f-i">🔴</span><div><div class="f-t">いま出発モード</div>
          <div class="f-d">今の時刻から、座れる可能性が高い電車をライブ判定。走らずに乗れる一本を優先。</div></div></div>
        <div class="f"><span class="f-i">🎒</span><div><div class="f-t">座れた30分ミッション</div>
          <div class="f-d">座れたら何をするかを先に決める（英単語・読書・課題・仮眠）。通学時間を"使える時間"に。</div></div></div>
        <div class="f"><span class="f-i">🎯</span><div><div class="f-t">マイ精度</div>
          <div class="f-d">自分の「座れた記録」で座席確保率を±8%補正。補正の根拠も画面に明示。</div></div></div>
      </div>
      <img class="shot mini" style="margin-top:1.6mm;" src="data:image/png;base64,{SHOT_MISSION}" alt="ミッションと記録">
    </div>
  </div>

  <div class="row r2">
    <div class="card">
      <div class="h"><span class="no">05</span><span class="ht">検証してわかったこと</span></div>
      <div class="quote">「便利そう。でも<b>記録は続かない</b>と思う」</div>
      <div class="quote">「％の<b>根拠が分からない</b>と、信じ切れない」</div>
      <ul>
        <li>→ v5：<b>あとから記録できる</b>リマインドを追加（忘れても回収）</li>
        <li>→ v5：座席確保率に<b>「記録n件から±N%補正」</b>と根拠を明示</li>
      </ul>
    </div>
    <div class="card warn">
      <div class="h"><span class="no w">06</span><span class="ht">失敗と、そこからの学び</span></div>
      <ul>
        <li><b>通用しなかったこと：</b>v4で「毎日その日に座れたか記録する」機能を作ったが、<b>作った自分が3日で記録を忘れた</b>。「記録させる」設計は続かなかった。</li>
        <li><b>学び：</b>習慣は<b>増やすより「思い出させる」</b>。v5では“あとから記録できる／忘れても精度に反映される”に作り替えた。</li>
        <li><b>次の課題：</b>混雑データは現状モデル値。実データ接続が信頼性の鍵。</li>
      </ul>
    </div>
  </div>

</div>

<div class="ft">
  <div class="qr">
    <img src="data:image/png;base64,{QR_PRODUCT}" alt="プロダクトQR">
    <div><div class="qr-t">▶ その場で使えます</div>
      <div class="qr-u">prototype-pi-six.vercel.app</div></div>
  </div>
  <div class="qr">
    <img src="data:image/png;base64,{QR_GITHUB}" alt="GitHub QR">
    <div><div class="qr-t">&lt;/&gt; ソースコード</div>
      <div class="qr-u">github.com/shimadakume-netizen/<br>gonta0506-web3ai-2026</div></div>
  </div>
  <div class="ft-msg">
    <div class="m1">走らなくていい朝を、<br>ぜんぶの通学生に。</div>
    <div class="m2">次：混雑オープンデータ接続 ／ ルート自動学習</div>
  </div>
</div>

</body></html>'''

out = os.path.join(D, 'poster.html')
io.open(out, 'w', encoding='utf-8').write(HTML)
print('poster.html written:', len(HTML), 'chars')
