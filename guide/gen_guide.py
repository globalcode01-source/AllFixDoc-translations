"""
AllFixDoc kullanım kılavuzu (guide.html) üreticisi. Metinler texts/<dil>.py dosyalarında (G sözlüğü); arayüz adları
{anahtar} biçiminde yazılır ve uygulamanın o dildeki metniyle doldurulur (tools/i18n), böylece kılavuz ile uygulama
aynı adları kullanır. Biçim: **kalın**, [metin](adres). Çalıştırma:

    python3 -I tools/guide/gen_guide.py <çıktı klasörü> [<çıktı klasörü> ...]
"""
import html
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
I18N = os.path.join(HERE, "..", "i18n")

# (sayfadaki kimlik, çeviri dosyası adı, dilin kendi adı)
LANGS = [
    ("tr", "tr", "Türkçe"), ("en", "en", "English"), ("az", "az", "Azərbaycan dili"), ("de", "de", "Deutsch"),
    ("es", "es", "Español"), ("fr", "fr", "Français"), ("id", "id", "Bahasa Indonesia"), ("it", "it", "Italiano"),
    ("pt-BR", "pt_BR", "Português (Brasil)"), ("ru", "ru", "Русский"), ("ar", "ar", "العربية"), ("hi", "hi", "हिन्दी"),
    ("ja", "ja", "日本語"), ("zh-CN", "zh_CN", "简体中文"),
]


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def ui_strings():
    """Uygulama metinleri: dil → {anahtar: metin}; eksikler İngilizce."""
    gen = load(os.path.join(I18N, "gen_strings.py"), "gen_strings")
    english = {k: v[0] for k, v in gen.S.items()}
    result = {"en": english, "tr": {**english, **{k: v[1] for k, v in gen.S.items()}}}
    for _, name, _ in LANGS:
        if name in result:
            continue
        table = load(os.path.join(I18N, "translations", name + ".py"), "t_" + name).T
        result[name] = {**english, **table}
    return result


def render(text, ui):
    def fill(m):
        key = m.group(1)
        if key not in ui:
            raise SystemExit(f"bilinmeyen arayüz anahtarı: {key}")
        return "\x00" + ui[key] + "\x01"  # yer tutucu; kaçışlamadan sonra açılır

    text = re.sub(r"\{([a-z0-9_]+)\}", fill, text)
    out = html.escape(text, quote=False)
    out = out.replace("\x00", "").replace("\x01", "")
    out = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", out)
    out = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", lambda m: f'<a href="{html.escape(m.group(2))}">{m.group(1)}</a>', out)
    return out


CSS = """
  :root { --bg: #f4eef0; --surface: #fffafb; --text: #221a1d; --muted: #6c5f64; --primary: #9b1f47; --tertiary: #2f63c0;
          --border: #ead9df; --chip: #f6e6ec; }
  @media (prefers-color-scheme: dark) {
    :root { --bg: #191315; --surface: #241c1f; --text: #f3e9ec; --muted: #c4b3b9; --primary: #ffb1c3; --tertiary: #a9c7ff;
            --border: #3a2d32; --chip: #33262b; }
  }
  * { box-sizing: border-box; }
  body { margin: 0; background: var(--bg); color: var(--text); font: 16px/1.6 system-ui, -apple-system, "Segoe UI", Roboto, sans-serif; }
  main { max-width: 760px; margin: 0 auto; padding: 28px 16px 64px; }
  .brand { font-size: 34px; font-weight: 700; letter-spacing: .5px; margin: 0;
           background: linear-gradient(90deg, var(--primary), var(--tertiary)); -webkit-background-clip: text; background-clip: text;
           color: transparent; text-shadow: 0 3px 8px color-mix(in srgb, var(--primary) 25%, transparent); }
  .tagline { margin: 0 0 16px; font-weight: 600; font-size: 14px;
             background: linear-gradient(90deg, var(--primary), var(--tertiary)); -webkit-background-clip: text; background-clip: text; color: transparent; }
  nav { display: flex; flex-wrap: wrap; gap: 6px; margin: 8px 0 4px; }
  nav a { font-size: 13px; padding: 4px 10px; border-radius: 999px; background: var(--chip); color: var(--text); text-decoration: none; }
  nav a.on { background: linear-gradient(90deg, var(--primary), var(--tertiary)); color: #fff; }
  h1 { font-size: 26px; line-height: 1.25; margin: 18px 0 6px; }
  .intro { color: var(--muted); margin: 0 0 8px; }
  .card { background: var(--surface); border: 1px solid var(--border); border-radius: 18px; padding: 16px 18px; margin-top: 14px;
          box-shadow: 0 2px 10px color-mix(in srgb, var(--primary) 8%, transparent); }
  h2 { font-size: 19px; margin: 0 0 6px; color: var(--primary); }
  ul { margin: 0; padding-inline-start: 22px; }
  li { margin: 4px 0; overflow-wrap: anywhere; }
  dt { font-weight: 600; margin-top: 10px; }
  dd { margin: 2px 0 0; color: var(--muted); overflow-wrap: anywhere; }
  a { color: var(--tertiary); }
  b { color: var(--text); }
  footer { color: var(--muted); font-size: 14px; margin-top: 28px; }
"""

SCRIPT = """
const LANGS = %s;
function pick() {
  const h = decodeURIComponent(location.hash.slice(1));
  if (LANGS.includes(h)) return h;
  for (const l of (navigator.languages || [navigator.language || "en"])) {
    const exact = LANGS.find(x => x.toLowerCase() === l.toLowerCase());
    if (exact) return exact;
    const base = LANGS.find(x => x.split("-")[0] === l.split("-")[0].toLowerCase());
    if (base) return base;
  }
  return "en";
}
function show(l) {
  for (const s of document.querySelectorAll("section.lang")) s.hidden = s.id !== l;
  for (const a of document.querySelectorAll("nav a")) a.classList.toggle("on", a.getAttribute("href") === "#" + l);
  document.documentElement.lang = l;
  const s = document.getElementById(l);
  if (s) document.title = s.dataset.title;
}
window.addEventListener("hashchange", () => { show(pick()); window.scrollTo(0, 0); });
show(pick());
// Dil etiketi (#tr) tarayıcıyı bölüme kaydırır; başlık ve dil seçici görünsün diye en üstten başla
window.addEventListener("load", () => window.scrollTo(0, 0));
"""


def build():
    ui = ui_strings()
    parts = []
    for page_id, name, _ in LANGS:
        g = load(os.path.join(HERE, "texts", name + ".py"), "g_" + name).G
        u = ui[name]
        rtl = ' dir="rtl"' if page_id == "ar" else ""
        p = [f'<section class="lang" id="{page_id}" lang="{page_id}"{rtl} data-title="{html.escape(g["title"])}">']
        p.append(f"<h1>{render(g['title'], u)}</h1>")
        p.append(f'<p class="intro">{render(g["intro"], u)}</p>')
        for title, items in g["sections"]:
            p.append('<div class="card">')
            p.append(f"<h2>{render(title, u)}</h2>")
            p.append("<ul>" + "".join(f"<li>{render(i, u)}</li>" for i in items) + "</ul>")
            p.append("</div>")
        p.append('<div class="card">')
        p.append(f"<h2>{render(g['faq_title'], u)}</h2><dl>")
        for q, a in g["faq"]:
            p.append(f"<dt>{render(q, u)}</dt><dd>{render(a, u)}</dd>")
        p.append("</dl></div>")
        p.append("</section>")
        parts.append("\n".join(p))
    nav = " ".join(f'<a href="#{pid}">{html.escape(label)}</a>' for pid, _, label in LANGS)
    ids = [pid for pid, _, _ in LANGS]
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AllFixDoc · Guide</title>
<link rel="icon" href="icon.png">
<meta name="description" content="AllFixDoc user guide: reading, notes, tools, voice notes, AI assistant, cloud and settings.">
<style>{CSS}</style>
</head>
<body>
<main>
<p class="brand">AllFixDoc</p>
<p class="tagline">PDF · Office · Scan · Notes</p>
<nav>{nav}</nav>
{chr(10).join(parts)}
<footer><a href="./">AllFixDoc</a> · <a href="privacy.html">Privacy policy</a></footer>
</main>
<script>{SCRIPT % ids}</script>
</body>
</html>
"""


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("kullanım: gen_guide.py <çıktı klasörü> [...]")
    page = build()
    for out in sys.argv[1:]:
        with open(os.path.join(out, "guide.html"), "w", encoding="utf-8") as f:
            f.write(page)
        print("yazıldı:", os.path.join(out, "guide.html"))
