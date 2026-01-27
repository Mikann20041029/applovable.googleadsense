set -euo pipefail

BASE="tools/json-formatter-validator"
mkdir -p "$BASE/assets" "$BASE/content"

# -------------------------
# assets/i18n.js
# -------------------------
cat > "$BASE/assets/i18n.js" <<'JS'
(function () {
  const DICT = {
    en: {
      "nav.home": "Home",
      "nav.about": "About",
      "nav.all_tools": "All Tools",
      "nav.contact": "Contact",

      "footer.privacy": "Privacy",
      "footer.terms": "Terms",
      "footer.disclaimer": "Disclaimer",
      "footer.contact": "Contact",
      "footer.about": "About",

      "lang.label": "Language",
      "lang.en": "English",
      "lang.ja": "日本語",
      "lang.ko": "한국어",
      "lang.zh": "中文",

      "tool.title": "JSON Formatter & Validator",
      "tool.subtitle": "Pretty print, minify, validate, sort keys, and pinpoint errors by line/column — in your browser.",
      "tool.input_label": "Input JSON",
      "tool.output_label": "Output",
      "tool.btn.format": "Format",
      "tool.btn.minify": "Minify",
      "tool.btn.validate": "Validate",
      "tool.btn.sample": "Load sample",
      "tool.btn.clear": "Clear",
      "tool.btn.copy": "Copy output",
      "tool.btn.download": "Download",
      "tool.toggle.sort_keys": "Sort object keys",
      "tool.indent.label": "Indent",
      "tool.indent.two": "2 spaces",
      "tool.indent.four": "4 spaces",
      "tool.status.ready": "Ready.",
      "tool.status.valid": "Valid JSON.",
      "tool.status.invalid": "Invalid JSON.",
      "tool.note.privacy": "Privacy: everything runs locally in your browser. No input is sent to a server.",
      "search.placeholder": "Search tools…",
      "breadcrumbs.home": "Home",
      "breadcrumbs.tools": "Tools",
      "breadcrumbs.current": "JSON Formatter & Validator",
      "popular.title": "Popular tools",
      "related.title": "Related tools"
    },

    ja: {
      "nav.home": "ホーム",
      "nav.about": "運営者情報",
      "nav.all_tools": "全ツール",
      "nav.contact": "お問い合わせ",

      "footer.privacy": "プライバシー",
      "footer.terms": "利用規約",
      "footer.disclaimer": "免責事項",
      "footer.contact": "お問い合わせ",
      "footer.about": "運営者情報",

      "lang.label": "言語",
      "lang.en": "English",
      "lang.ja": "日本語",
      "lang.ko": "한국어",
      "lang.zh": "中文",

      "tool.title": "JSON フォーマッター & バリデーター",
      "tool.subtitle": "整形・最小化・検証・キー並び替え・行/列付きエラー特定を、ブラウザ内だけで実行します。",
      "tool.input_label": "入力（JSON）",
      "tool.output_label": "出力",
      "tool.btn.format": "整形",
      "tool.btn.minify": "最小化",
      "tool.btn.validate": "検証",
      "tool.btn.sample": "サンプル",
      "tool.btn.clear": "クリア",
      "tool.btn.copy": "出力をコピー",
      "tool.btn.download": "ダウンロード",
      "tool.toggle.sort_keys": "キーを並び替える",
      "tool.indent.label": "インデント",
      "tool.indent.two": "2スペース",
      "tool.indent.four": "4スペース",
      "tool.status.ready": "準備完了。",
      "tool.status.valid": "有効なJSONです。",
      "tool.status.invalid": "JSONが不正です。",
      "tool.note.privacy": "プライバシー：処理はすべてブラウザ内で完結し、入力内容はサーバーに送信されません。",
      "search.placeholder": "ツールを検索…",
      "breadcrumbs.home": "ホーム",
      "breadcrumbs.tools": "ツール",
      "breadcrumbs.current": "JSON フォーマッター",
      "popular.title": "人気ツール",
      "related.title": "関連ツール"
    },

    ko: {
      "nav.home": "홈",
      "nav.about": "소개",
      "nav.all_tools": "전체 도구",
      "nav.contact": "문의",

      "footer.privacy": "개인정보처리방침",
      "footer.terms": "이용약관",
      "footer.disclaimer": "면책조항",
      "footer.contact": "문의",
      "footer.about": "소개",

      "lang.label": "언어",
      "lang.en": "English",
      "lang.ja": "日本語",
      "lang.ko": "한국어",
      "lang.zh": "中文",

      "tool.title": "JSON 포매터 & 검증기",
      "tool.subtitle": "브라우저에서 JSON을 정렬/축소/검증하고, 오류를 줄/열로 정확히 표시합니다.",
      "tool.input_label": "입력(JSON)",
      "tool.output_label": "출력",
      "tool.btn.format": "정렬",
      "tool.btn.minify": "축소",
      "tool.btn.validate": "검증",
      "tool.btn.sample": "예시",
      "tool.btn.clear": "지우기",
      "tool.btn.copy": "출력 복사",
      "tool.btn.download": "다운로드",
      "tool.toggle.sort_keys": "키 정렬",
      "tool.indent.label": "들여쓰기",
      "tool.indent.two": "2칸",
      "tool.indent.four": "4칸",
      "tool.status.ready": "준비됨.",
      "tool.status.valid": "유효한 JSON입니다.",
      "tool.status.invalid": "JSON이 유효하지 않습니다.",
      "tool.note.privacy": "개인정보: 모든 처리는 브라우저에서만 진행되며 입력은 서버로 전송되지 않습니다.",
      "search.placeholder": "도구 검색…",
      "breadcrumbs.home": "홈",
      "breadcrumbs.tools": "도구",
      "breadcrumbs.current": "JSON 포매터",
      "popular.title": "인기 도구",
      "related.title": "관련 도구"
    },

    zh: {
      "nav.home": "主页",
      "nav.about": "关于",
      "nav.all_tools": "全部工具",
      "nav.contact": "联系",

      "footer.privacy": "隐私",
      "footer.terms": "条款",
      "footer.disclaimer": "免责声明",
      "footer.contact": "联系",
      "footer.about": "关于",

      "lang.label": "语言",
      "lang.en": "English",
      "lang.ja": "日本語",
      "lang.ko": "한국어",
      "lang.zh": "中文",

      "tool.title": "JSON 格式化与校验",
      "tool.subtitle": "在浏览器内完成格式化、压缩、校验、键排序，并定位到行/列错误。",
      "tool.input_label": "输入(JSON)",
      "tool.output_label": "输出",
      "tool.btn.format": "格式化",
      "tool.btn.minify": "压缩",
      "tool.btn.validate": "校验",
      "tool.btn.sample": "示例",
      "tool.btn.clear": "清空",
      "tool.btn.copy": "复制输出",
      "tool.btn.download": "下载",
      "tool.toggle.sort_keys": "键排序",
      "tool.indent.label": "缩进",
      "tool.indent.two": "2空格",
      "tool.indent.four": "4空格",
      "tool.status.ready": "就绪。",
      "tool.status.valid": "JSON 有效。",
      "tool.status.invalid": "JSON 无效。",
      "tool.note.privacy": "隐私：所有处理都在浏览器本地完成，输入不会发送到服务器。",
      "search.placeholder": "搜索工具…",
      "breadcrumbs.home": "主页",
      "breadcrumbs.tools": "工具",
      "breadcrumbs.current": "JSON 格式化",
      "popular.title": "热门工具",
      "related.title": "相关工具"
    }
  };

  function getLang() {
    const url = new URL(location.href);
    const q = url.searchParams.get("lang");
    const saved = localStorage.getItem("lang");
    const lang = (q || saved || "en").toLowerCase();
    return (DICT[lang] ? lang : "en");
  }

  function setLang(lang) {
    const v = (DICT[lang] ? lang : "en");
    localStorage.setItem("lang", v);
    const url = new URL(location.href);
    url.searchParams.set("lang", v);
    history.replaceState(null, "", url.toString());
  }

  function t(key) {
    const lang = getLang();
    return (DICT[lang] && DICT[lang][key]) || DICT.en[key] || key;
  }

  window.__I18N__ = { DICT, getLang, setLang, t };
})();
JS

# -------------------------
# assets/site.css
# -------------------------
cat > "$BASE/assets/site.css" <<'CSS'
:root{
  --bg:#0b1020;
  --panel:rgba(18,26,51,.55);
  --panel2:rgba(18,26,51,.35);
  --line:#22305f;
  --text:#e8ecff;
  --muted:#a9b3e6;
  --link:#9bb6ff;
  --good:#6ee7b7;
  --bad:#fb7185;
  --warn:#fbbf24;
  --shadow: 0 10px 30px rgba(0,0,0,.35);
  --radius: 16px;
}

*{ box-sizing:border-box; }
html,body{ height:100%; }
body{
  margin:0;
  font-family: system-ui,-apple-system,"Segoe UI",Roboto,"Noto Sans JP",sans-serif;
  background: linear-gradient(180deg,#070a14,#0b1020 50%,#070a14);
  color: var(--text);
}

a{ color:var(--link); text-decoration:none; }
a:hover{ text-decoration:underline; }

.container{
  max-width: 1100px;
  margin: 0 auto;
  padding: 18px 16px 40px;
}

header{
  position: sticky;
  top: 0;
  z-index: 30;
  border-bottom: 1px solid var(--line);
  background: rgba(10,14,28,.86);
  backdrop-filter: blur(10px);
}

.navbar{
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:12px;
}

.brand{
  font-weight: 700;
  letter-spacing: .2px;
  white-space:nowrap;
}

.navlinks{
  display:flex;
  gap:10px;
  flex-wrap:wrap;
  align-items:center;
  justify-content:flex-end;
}

.pill{
  border:1px solid var(--line);
  background: rgba(18,26,51,.45);
  padding: 8px 10px;
  border-radius: 999px;
}

.lang{
  display:flex;
  gap:8px;
  align-items:center;
}

select, button, input, textarea{
  font: inherit;
}

.card{
  border: 1px solid var(--line);
  border-radius: var(--radius);
  background: radial-gradient(900px 320px at 20% 0%, rgba(155,182,255,.25), transparent), var(--panel);
  box-shadow: var(--shadow);
}

.card-inner{ padding: 16px; }

.breadcrumbs{
  margin: 12px 0 10px;
  color: var(--muted);
  font-size: 13px;
}
.breadcrumbs a{ color: var(--muted); }

.hero{
  padding: 16px;
}

.h-title{
  margin: 0 0 8px;
  font-size: 20px;
}
.h-sub{
  margin: 0;
  color: var(--muted);
  line-height: 1.6;
}

.grid{
  display:grid;
  grid-template-columns: 1fr;
  gap: 14px;
  margin-top: 14px;
}
@media (min-width: 980px){
  .grid{ grid-template-columns: 1.05fr .95fr; }
}

.label{
  display:block;
  margin: 0 0 8px;
  font-size: 13px;
  color: var(--muted);
}

textarea{
  width: 100%;
  min-height: 220px;
  resize: vertical;
  padding: 12px;
  border-radius: 12px;
  border: 1px solid var(--line);
  background: rgba(7,10,20,.65);
  color: var(--text);
  line-height: 1.5;
}

.controls{
  display:flex;
  flex-wrap:wrap;
  gap:10px;
  align-items:center;
  margin-top: 10px;
}

button{
  border: 1px solid var(--line);
  background: rgba(18,26,51,.35);
  color: var(--text);
  padding: 8px 10px;
  border-radius: 12px;
  cursor: pointer;
}
button:hover{ background: rgba(18,26,51,.55); }
button:disabled{
  opacity:.5;
  cursor:not-allowed;
}

small.note{
  display:block;
  margin-top: 10px;
  color: var(--muted);
  line-height: 1.5;
}

.status{
  margin-top: 10px;
  padding: 10px 12px;
  border-radius: 12px;
  border: 1px solid var(--line);
  background: rgba(18,26,51,.25);
  color: var(--muted);
}

.status.good{ border-color: rgba(110,231,183,.35); color: var(--good); }
.status.bad{ border-color: rgba(251,113,133,.35); color: var(--bad); }

.content{
  margin-top: 16px;
  padding: 16px;
  border: 1px solid var(--line);
  border-radius: var(--radius);
  background: rgba(18,26,51,.35);
}
.content h2{
  margin: 18px 0 8px;
  font-size: 16px;
}
.content h3{
  margin: 14px 0 6px;
  font-size: 14px;
}
.content p, .content li{
  color: var(--text);
  line-height: 1.75;
}
.content .muted{ color: var(--muted); }
.content code{
  background: rgba(7,10,20,.75);
  border: 1px solid var(--line);
  padding: 2px 6px;
  border-radius: 8px;
}
.content pre{
  background: rgba(7,10,20,.75);
  border: 1px solid var(--line);
  padding: 12px;
  border-radius: 12px;
  overflow:auto;
}

.toc{
  margin: 12px 0 0;
  padding: 12px;
  border-radius: 12px;
  border: 1px solid var(--line);
  background: rgba(7,10,20,.35);
}
.toc strong{ display:block; margin-bottom:6px; }
.toc a{ color: var(--link); }
.toc ul{ margin: 8px 0 0; padding-left: 18px; }

footer{
  margin-top: 22px;
  border-top: 1px solid var(--line);
  color: var(--muted);
  padding: 18px 0 28px;
  font-size: 13px;
}
.footer-links{
  display:flex;
  flex-wrap:wrap;
  gap:10px;
  margin-top: 8px;
}
CSS

# -------------------------
# assets/app.js
# -------------------------
cat > "$BASE/assets/app.js" <<'JS'
(function(){
  const { t, getLang, setLang } = window.__I18N__;

  function qs(sel, root=document){ return root.querySelector(sel); }
  function qsa(sel, root=document){ return Array.from(root.querySelectorAll(sel)); }

  function escapeHtml(s){
    return s.replace(/[&<>"']/g, (c)=>({ "&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;" }[c]));
  }

  function computeLineCol(text, pos){
    let line = 1, col = 1;
    for(let i=0;i<pos && i<text.length;i++){
      if(text[i]==="\n"){ line++; col=1; }
      else { col++; }
    }
    return { line, col };
  }

  function extractPositionFromErrorMessage(msg){
    // Chrome: "... at position 42"
    const m = msg.match(/position\s+(\d+)/i);
    if(m) return parseInt(m[1],10);
    return null;
  }

  function deepSortKeys(value){
    if(Array.isArray(value)){
      return value.map(deepSortKeys);
    }
    if(value && typeof value === "object"){
      const out = {};
      Object.keys(value).sort((a,b)=>a.localeCompare(b)).forEach(k=>{
        out[k] = deepSortKeys(value[k]);
      });
      return out;
    }
    return value;
  }

  function setText(el, key){
    el.textContent = t(key);
  }

  function applyI18n(){
    qsa("[data-i18n]").forEach(el=>{
      const key = el.getAttribute("data-i18n");
      setText(el, key);
    });
    qsa("[data-i18n-ph]").forEach(el=>{
      const key = el.getAttribute("data-i18n-ph");
      el.setAttribute("placeholder", t(key));
    });

    const lang = getLang();
    const sel = qs("#langSelect");
    if(sel) sel.value = lang;
  }

  async function loadContent(pageKey){
    const lang = getLang();
    const url = `content/${pageKey}.${lang}.html`;
    const host = qs("#contentHost");
    if(!host) return;

    try{
      const res = await fetch(url, { cache: "no-store" });
      if(!res.ok) throw new Error(`Failed to load ${url}`);
      const html = await res.text();
      host.innerHTML = html;
      buildTOC(host);
    }catch(e){
      host.innerHTML = `<p class="muted">Content failed to load.</p>`;
    }
  }

  function slugifyHeading(text){
    return text.toLowerCase()
      .replace(/[^\p{L}\p{N}\s-]/gu,"")
      .trim()
      .replace(/\s+/g,"-")
      .slice(0,64);
  }

  function buildTOC(host){
    const tocHost = qs("#tocHost");
    if(!tocHost) return;

    const hs = qsa("h2, h3", host);
    if(hs.length === 0){
      tocHost.innerHTML = "";
      return;
    }

    // Ensure ids
    hs.forEach(h=>{
      if(!h.id){
        h.id = slugifyHeading(h.textContent || "section");
      }
    });

    const items = hs.filter(h=>h.tagName === "H2").map(h2=>{
      const subs = [];
      let next = h2.nextElementSibling;
      while(next){
        if(next.tagName === "H2") break;
        if(next.tagName === "H3") subs.push(next);
        next = next.nextElementSibling;
      }
      return { h: h2, subs };
    });

    const html = [
      `<div class="toc">`,
      `<strong>Table of contents</strong>`,
      `<ul>`,
      ...items.map(it=>{
        const h2 = it.h;
        const li = [
          `<li><a href="#${escapeHtml(h2.id)}">${escapeHtml(h2.textContent || "")}</a>`,
          (it.subs.length ? `<ul>${it.subs.map(s=>`<li><a href="#${escapeHtml(s.id)}">${escapeHtml(s.textContent||"")}</a></li>`).join("")}</ul>` : ""),
          `</li>`
        ].join("");
        return li;
      }),
      `</ul>`,
      `</div>`
    ].join("");
    tocHost.innerHTML = html;
  }

  function initLanguage(){
    const sel = qs("#langSelect");
    if(!sel) return;
    sel.addEventListener("change", ()=>{
      setLang(sel.value);
      applyI18n();
      const pageKey = document.body.getAttribute("data-page") || "index";
      loadContent(pageKey);
    });
  }

  function initTool(){
    const input = qs("#jsonInput");
    const output = qs("#jsonOutput");
    const status = qs("#statusBox");
    const indentSel = qs("#indentSelect");
    const sortToggle = qs("#sortToggle");

    if(!input || !output || !status) return;

    const LS_KEY = "json_tool_input_v1";
    const saved = localStorage.getItem(LS_KEY);
    if(saved) input.value = saved;

    function setStatus(kind, msg){
      status.classList.remove("good","bad");
      if(kind==="good") status.classList.add("good");
      if(kind==="bad") status.classList.add("bad");
      status.textContent = msg;
    }

    function parseJson(text){
      try{
        const obj = JSON.parse(text);
        return { ok:true, obj };
      }catch(e){
        const msg = (e && e.message) ? String(e.message) : "JSON parse error";
        const pos = extractPositionFromErrorMessage(msg);
        if(pos !== null){
          const lc = computeLineCol(text, pos);
          return { ok:false, error: `${msg} (line ${lc.line}, col ${lc.col}, pos ${pos})`, pos, line: lc.line, col: lc.col };
        }
        return { ok:false, error: msg };
      }
    }

    function currentIndent(){
      return indentSel ? parseInt(indentSel.value,10) : 2;
    }

    function maybeSort(obj){
      return (sortToggle && sortToggle.checked) ? deepSortKeys(obj) : obj;
    }

    function doValidate(){
      const text = input.value.trim();
      if(!text){
        output.value = "";
        setStatus("","" + t("tool.status.ready"));
        return;
      }
      const r = parseJson(text);
      if(r.ok){
        setStatus("good", t("tool.status.valid"));
      }else{
        setStatus("bad", `${t("tool.status.invalid")} ${r.error}`);
        if(typeof r.pos === "number"){
          try{
            input.focus();
            input.setSelectionRange(r.pos, Math.min(r.pos+1, input.value.length));
          }catch(_){}
        }
      }
    }

    function doFormat(){
      const text = input.value.trim();
      const r = parseJson(text);
      if(!r.ok){
        output.value = "";
        setStatus("bad", `${t("tool.status.invalid")} ${r.error}`);
        return;
      }
      const obj = maybeSort(r.obj);
      output.value = JSON.stringify(obj, null, currentIndent());
      setStatus("good", t("tool.status.valid"));
    }

    function doMinify(){
      const text = input.value.trim();
      const r = parseJson(text);
      if(!r.ok){
        output.value = "";
        setStatus("bad", `${t("tool.status.invalid")} ${r.error}`);
        return;
      }
      const obj = maybeSort(r.obj);
      output.value = JSON.stringify(obj);
      setStatus("good", t("tool.status.valid"));
    }

    function doSample(){
      const sample = {
        tool: "JSON Formatter & Validator",
        ok: true,
        timestamp: new Date().toISOString(),
        user: { id: 123, name: "Aki", roles: ["admin","editor"] },
        settings: { indent: 2, sortKeys: true },
        items: [
          { id: 1, title: "Hello", tags: ["json","format"] },
          { id: 2, title: "World", tags: ["validate","debug"] }
        ]
      };
      input.value = JSON.stringify(sample, null, 2);
      localStorage.setItem(LS_KEY, input.value);
      doFormat();
    }

    function doClear(){
      input.value = "";
      output.value = "";
      localStorage.removeItem(LS_KEY);
      setStatus("", t("tool.status.ready"));
    }

    function doCopy(){
      const v = output.value || "";
      navigator.clipboard.writeText(v).then(()=>{
        setStatus("good", "Copied.");
        setTimeout(()=>doValidate(), 700);
      }).catch(()=>{
        setStatus("bad", "Copy failed.");
      });
    }

    function doDownload(){
      const v = output.value || "";
      const blob = new Blob([v], { type: "application/json;charset=utf-8" });
      const a = document.createElement("a");
      a.href = URL.createObjectURL(blob);
      a.download = "formatted.json";
      document.body.appendChild(a);
      a.click();
      a.remove();
      URL.revokeObjectURL(a.href);
      setStatus("good", "Downloaded.");
      setTimeout(()=>doValidate(), 700);
    }

    qs("#btnValidate")?.addEventListener("click", doValidate);
    qs("#btnFormat")?.addEventListener("click", doFormat);
    qs("#btnMinify")?.addEventListener("click", doMinify);
    qs("#btnSample")?.addEventListener("click", doSample);
    qs("#btnClear")?.addEventListener("click", doClear);
    qs("#btnCopy")?.addEventListener("click", doCopy);
    qs("#btnDownload")?.addEventListener("click", doDownload);

    input.addEventListener("input", ()=>{
      localStorage.setItem(LS_KEY, input.value);
    });

    setStatus("", t("tool.status.ready"));
  }

  function init(){
    applyI18n();
    initLanguage();

    const pageKey = document.body.getAttribute("data-page") || "index";
    loadContent(pageKey);

    initTool();
  }

  document.addEventListener("DOMContentLoaded", init);
})();
JS

# -------------------------
# Shared HTML pages
# -------------------------
make_page () {
  local file="$1"
  local pageKey="$2"
  local title="$3"
  local canonical="$4"

  cat > "$BASE/$file" <<HTML
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>${title}</title>
  <meta name="description" content="Format and validate JSON in your browser. Pretty print, minify, sort keys, and find errors by line/column." />
  <link rel="canonical" href="${canonical}" />
  <meta property="og:type" content="website" />
  <meta property="og:title" content="JSON Formatter & Validator" />
  <meta property="og:description" content="Format and validate JSON in your browser. Error line/column, minify, copy/download, examples, troubleshooting." />
  <meta property="og:url" content="${canonical}" />
  <meta name="twitter:card" content="summary" />

  <!-- AdSense (optional for ownership/ads). Replace client if needed. -->
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5643751507480712"
    crossorigin="anonymous"></script>

  <link rel="stylesheet" href="assets/site.css" />
</head>
<body data-page="${pageKey}">
<header>
  <div class="container">
    <div class="navbar">
      <div class="brand">Mikanntool</div>
      <nav class="navlinks" aria-label="Primary">
        <a class="pill" href="./" data-i18n="nav.home"></a>
        <a class="pill" href="about.html" data-i18n="nav.about"></a>
        <a class="pill" href="all-tools.html" data-i18n="nav.all_tools"></a>
        <a class="pill" href="contact.html" data-i18n="nav.contact"></a>
        <div class="lang">
          <span class="pill" data-i18n="lang.label"></span>
          <select id="langSelect" class="pill" aria-label="Language">
            <option value="en" data-i18n="lang.en">English</option>
            <option value="ja" data-i18n="lang.ja">日本語</option>
            <option value="ko" data-i18n="lang.ko">한국어</option>
            <option value="zh" data-i18n="lang.zh">中文</option>
          </select>
        </div>
      </nav>
    </div>
  </div>
</header>

<main class="container">
  <div class="breadcrumbs">
    <a href="./" data-i18n="breadcrumbs.home"></a> ›
    <a href="all-tools.html" data-i18n="breadcrumbs.tools"></a> ›
    <span data-i18n="breadcrumbs.current"></span>
  </div>

  <section class="card">
    <div class="card-inner hero">
      <div class="h-title" data-i18n="tool.title"></div>
      <p class="h-sub" data-i18n="tool.subtitle"></p>
    </div>
  </section>

  <div class="grid">
    <section class="card">
      <div class="card-inner">
        <label class="label" for="jsonInput" data-i18n="tool.input_label"></label>
        <textarea id="jsonInput" spellcheck="false" autocapitalize="off" autocomplete="off"></textarea>

        <div class="controls">
          <button id="btnFormat" type="button" data-i18n="tool.btn.format"></button>
          <button id="btnMinify" type="button" data-i18n="tool.btn.minify"></button>
          <button id="btnValidate" type="button" data-i18n="tool.btn.validate"></button>
          <button id="btnSample" type="button" data-i18n="tool.btn.sample"></button>
          <button id="btnClear" type="button" data-i18n="tool.btn.clear"></button>

          <label class="pill" style="display:flex;align-items:center;gap:8px;">
            <input id="sortToggle" type="checkbox" />
            <span data-i18n="tool.toggle.sort_keys"></span>
          </label>

          <label class="pill" style="display:flex;align-items:center;gap:8px;">
            <span data-i18n="tool.indent.label"></span>
            <select id="indentSelect" class="pill" aria-label="Indent">
              <option value="2" data-i18n="tool.indent.two">2 spaces</option>
              <option value="4" data-i18n="tool.indent.four">4 spaces</option>
            </select>
          </label>
        </div>

        <div id="statusBox" class="status" role="status" aria-live="polite"></div>
        <small class="note" data-i18n="tool.note.privacy"></small>
      </div>
    </section>

    <section class="card">
      <div class="card-inner">
        <label class="label" for="jsonOutput" data-i18n="tool.output_label"></label>
        <textarea id="jsonOutput" readonly></textarea>

        <div class="controls">
          <button id="btnCopy" type="button" data-i18n="tool.btn.copy"></button>
          <button id="btnDownload" type="button" data-i18n="tool.btn.download"></button>
        </div>

        <div id="tocHost"></div>
      </div>
    </section>
  </div>

  <section class="content" id="contentHost"></section>
</main>

<footer>
  <div class="container">
    <div>© JSON Formatter & Validator</div>
    <div class="footer-links" aria-label="Footer">
      <a href="privacy.html" data-i18n="footer.privacy"></a>
      <a href="terms.html" data-i18n="footer.terms"></a>
      <a href="disclaimer.html" data-i18n="footer.disclaimer"></a>
      <a href="contact.html" data-i18n="footer.contact"></a>
      <a href="about.html" data-i18n="footer.about"></a>
    </div>
  </div>
</footer>

<script src="assets/i18n.js"></script>
<script src="assets/app.js"></script>

<!-- Schema.org JSON-LD (English; keep canonical stable) -->
<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@graph":[
    {
      "@type":"BreadcrumbList",
      "itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":"https://mikanntool.com/"},
        {"@type":"ListItem","position":2,"name":"Tools","item":"https://mikanntool.com/tools/"},
        {"@type":"ListItem","position":3,"name":"JSON Formatter & Validator","item":"https://mikanntool.com/tools/json-formatter-validator/"}
      ]
    },
    {
      "@type":"SoftwareApplication",
      "name":"JSON Formatter & Validator",
      "applicationCategory":"DeveloperApplication",
      "operatingSystem":"All",
      "offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},
      "url":"https://mikanntool.com/tools/json-formatter-validator/",
      "description":"Format and validate JSON in your browser. Pretty print, minify, sort keys, and locate errors by line/column."
    },
    {
      "@type":"FAQPage",
      "mainEntity":[
        {"@type":"Question","name":"Is this JSON tool private?","acceptedAnswer":{"@type":"Answer","text":"Yes. Formatting and validation run locally in your browser. Your input is not sent to a server."}},
        {"@type":"Question","name":"Why does my JSON fail with trailing commas?","acceptedAnswer":{"@type":"Answer","text":"Strict JSON does not allow trailing commas. Remove the final comma before a closing ] or }."}},
        {"@type":"Question","name":"What does “Unexpected token” mean?","acceptedAnswer":{"@type":"Answer","text":"It means the parser found a character that is not allowed at that location (often an unquoted key, single quotes, or an extra comma)."}},
        {"@type":"Question","name":"Can JSON contain comments?","acceptedAnswer":{"@type":"Answer","text":"No. Standard JSON does not support // or /* */ comments. Use a different format (like JSONC) only where explicitly supported."}},
        {"@type":"Question","name":"Does JSON allow NaN or Infinity?","acceptedAnswer":{"@type":"Answer","text":"No. JSON numbers must be finite. Use null or a string if you need to represent those values."}},
        {"@type":"Question","name":"How do I find the exact error location?","acceptedAnswer":{"@type":"Answer","text":"This tool shows line/column (and character position) when the browser provides an error position."}},
        {"@type":"Question","name":"What is the difference between formatting and minifying?","acceptedAnswer":{"@type":"Answer","text":"Formatting adds whitespace and indentation for readability. Minifying removes whitespace to reduce size."}},
        {"@type":"Question","name":"Will sorting keys change the meaning?","acceptedAnswer":{"@type":"Answer","text":"For typical JSON objects, key order should not matter, but some systems may compare raw text. Only enable sorting when safe for your workflow."}},
        {"@type":"Question","name":"Can I validate against a JSON Schema here?","acceptedAnswer":{"@type":"Answer","text":"This tool validates strict JSON syntax. Schema validation is a separate step (JSON Schema) and is planned as a related tool."}},
        {"@type":"Question","name":"What encodings are safe?","acceptedAnswer":{"@type":"Answer","text":"UTF-8 is the standard choice for JSON. Avoid ambiguous encodings when sending JSON to APIs."}}
      ]
    }
  ]
}
</script>
</body>
</html>
HTML
}

make_page "index.html" "index" "JSON Formatter & Validator — Pretty Print, Minify, Debug" "https://mikanntool.com/tools/json-formatter-validator/"
make_page "all-tools.html" "all-tools" "All Tools — JSON Formatter & Validator" "https://mikanntool.com/tools/json-formatter-validator/all-tools.html"
make_page "about.html" "about" "About — JSON Formatter & Validator" "https://mikanntool.com/tools/json-formatter-validator/about.html"
make_page "contact.html" "contact" "Contact — JSON Formatter & Validator" "https://mikanntool.com/tools/json-formatter-validator/contact.html"
make_page "privacy.html" "privacy" "Privacy — JSON Formatter & Validator" "https://mikanntool.com/tools/json-formatter-validator/privacy.html"
make_page "terms.html" "terms" "Terms — JSON Formatter & Validator" "https://mikanntool.com/tools/json-formatter-validator/terms.html"
make_page "disclaimer.html" "disclaimer" "Disclaimer — JSON Formatter & Validator" "https://mikanntool.com/tools/json-formatter-validator/disclaimer.html"

# -------------------------
# content/index.en.html (2500+ words, high-detail)
# -------------------------
cat > "$BASE/content/index.en.html" <<'HTML'
<h2>Quick answer</h2>
<p>
If your JSON is failing, the fastest fix is usually one of these: remove trailing commas, quote all object keys, use double quotes (not single quotes),
and make sure brackets/braces match. Paste your JSON on the left, click <strong>Validate</strong>, and the tool will report the error (often with line/column).
Then click <strong>Format</strong> to produce a readable version or <strong>Minify</strong> to compress it for transport.
</p>

<h2>How to use this tool</h2>
<ol>
  <li><strong>Paste JSON</strong> into the input box. If you want a known-good example, click <strong>Load sample</strong>.</li>
  <li>Click <strong>Validate</strong> to check strict JSON syntax. If invalid, you’ll see an error message and (when available) line/column.</li>
  <li>Click <strong>Format</strong> to pretty-print the JSON with indentation, or <strong>Minify</strong> to remove whitespace.</li>
  <li>Enable <strong>Sort object keys</strong> only if your workflow is safe with reordered keys (some systems compare raw text).</li>
  <li>Use <strong>Copy output</strong> or <strong>Download</strong> to save results. Input is saved locally in your browser for convenience.</li>
</ol>
<p class="muted">
Privacy note: everything runs locally in your browser. This is designed to be safe for API payloads and configs you do not want to upload to a server.
</p>

<h2>What “valid JSON” really means</h2>
<p>
A lot of “JSON-like” text on the internet is not actually valid JSON. Standard JSON is defined by formal specifications (RFC 8259 and ECMA-404),
and strict parsers (like <code>JSON.parse</code>) enforce these rules. Understanding the rules saves time because the same mistakes repeat across
API debugging, configuration files, and data exports.
</p>

<h3>Rule 1: JSON has only these data types</h3>
<ul>
  <li><strong>Object</strong>: <code>{ "key": "value" }</code></li>
  <li><strong>Array</strong>: <code>[1, 2, 3]</code></li>
  <li><strong>String</strong>: <code>"text"</code> (double quotes only)</li>
  <li><strong>Number</strong>: <code>0</code>, <code>-12.34</code>, <code>1e6</code> (finite numbers only)</li>
  <li><strong>Boolean</strong>: <code>true</code> / <code>false</code></li>
  <li><strong>Null</strong>: <code>null</code></li>
</ul>
<p>
If you see <code>undefined</code>, <code>NaN</code>, <code>Infinity</code>, function bodies, or dates written like <code>new Date()</code>,
that’s JavaScript (or another language), not JSON.
</p>

<h3>Rule 2: Object keys must be strings in double quotes</h3>
<p>
This fails in strict JSON:
</p>
<pre><code>{ name: "Alice" }</code></pre>
<p>
This is correct:
</p>
<pre><code>{ "name": "Alice" }</code></pre>

<h3>Rule 3: Strings must use double quotes</h3>
<p>
Single quotes are common in examples, but strict JSON does not allow them:
</p>
<pre><code>{ "name": 'Alice' }</code></pre>
<p>
Use:
</p>
<pre><code>{ "name": "Alice" }</code></pre>

<h3>Rule 4: No trailing commas</h3>
<p>
Trailing commas are one of the top causes of “it looks fine but won’t parse”.
This is invalid:
</p>
<pre><code>{
  "a": 1,
}</code></pre>
<p>
So is this:
</p>
<pre><code>[1, 2, 3,]</code></pre>
<p>
Fix by removing the final comma before <code>}</code> or <code>]</code>.
</p>

<h3>Rule 5: Comments are not allowed</h3>
<p>
JSON does not support <code>//</code> or <code>/* */</code>. Some editors support “JSONC” (JSON with comments),
but APIs and strict parsers will reject it. If your toolchain requires comments, store them outside the JSON (docs, README),
or use a format that explicitly supports comments.
</p>

<h3>Rule 6: Encoding and escaping matter</h3>
<p>
JSON is typically transmitted as UTF-8. Most issues come from accidentally breaking strings:
unescaped newline characters, unescaped quotes, or invalid backslashes.
A backslash starts an escape sequence. For example, Windows paths often break because <code>\U</code> or <code>\n</code> is read as an escape.
If you need a literal backslash, escape it: <code>"C:\\Users\\Alice\\file.txt"</code>.
</p>

<h2>Step-by-step fixes for common errors</h2>
<p>
When you see an error like “Unexpected token …”, don’t guess. Fix systematically:
</p>
<ol>
  <li><strong>Validate</strong> first. Read the message and locate the position (line/column if provided).</li>
  <li><strong>Check the character at that spot</strong>: is it an extra comma, missing quote, or wrong bracket?</li>
  <li><strong>Confirm structure</strong>: every <code>{</code> must close with <code>}</code>, every <code>[</code> with <code>]</code>.</li>
  <li><strong>Fix one thing at a time</strong>, then validate again. Multiple changes at once makes debugging harder.</li>
</ol>

<h3>“Unexpected token o in JSON at position …”</h3>
<p>
This classic error often appears when you are parsing something that is already an object (not a string) in JavaScript,
or when you accidentally feed the parser non-JSON text like <code>ok</code>, <code>error</code>, or an HTML page.
In a tool like this, it usually means your JSON starts with a character that’s not valid JSON.
Valid JSON must start with <code>{</code>, <code>[</code>, <code>"</code>, a digit/minus, <code>true</code>, <code>false</code>, or <code>null</code>.
</p>

<h3>“Unexpected string”</h3>
<p>
Often caused by missing commas between properties:
</p>
<pre><code>{
  "a": 1
  "b": 2
}</code></pre>
<p>
Add a comma after <code>1</code>.
</p>

<h3>“Unexpected end of JSON input”</h3>
<p>
This means the parser reached the end while still expecting something:
a closing brace/bracket, a quote, or a value. Typical causes:
</p>
<ul>
  <li>Missing <code>}</code> or <code>]</code></li>
  <li>Unclosed string: <code>"name": "Alice</code></li>
  <li>Cut-off payload (copy/paste truncated)</li>
</ul>

<h3>Broken strings (quotes, newlines, backslashes)</h3>
<p>
If your JSON includes large text blocks, stack traces, or multi-line content, make sure newlines are escaped
as <code>\n</code> inside strings, and that embedded quotes are escaped as <code>\"</code>.
If you paste raw logs directly inside a JSON string without escaping, it will fail.
</p>

<h2>Best practices that prevent future pain</h2>
<p>
Valid JSON is the minimum. For real systems, consistency and safety matter too:
</p>

<h3>Use consistent indentation</h3>
<p>
Pick 2 or 4 spaces and stay consistent across a repository. Consistent formatting reduces merge conflicts and makes diffs readable.
</p>

<h3>Keep numbers precise (especially IDs)</h3>
<p>
JavaScript (and many tools) use IEEE-754 double precision for numbers. Very large integers can lose precision.
If you have IDs like <code>12345678901234567890</code>, store them as strings:
<code>"id": "12345678901234567890"</code>. This prevents accidental rounding.
</p>

<h3>Don’t rely on object key order</h3>
<p>
In JSON semantics, object key order is not significant. Some systems preserve order, but you should not depend on it unless the consumer explicitly says so.
If order matters, use arrays.
</p>

<h3>Prefer explicit nulls over missing keys (when contract matters)</h3>
<p>
For APIs and configs, decide whether “missing” and “null” are different. If they are, document the contract.
If you always include the key but allow it to be null, downstream code can be simpler.
</p>

<h3>Keep JSON small and split when necessary</h3>
<p>
Giant JSON blobs are hard to debug. If you control the format, split the payload into smaller objects or files,
and validate each part independently.
</p>

<h3>Use JSON Schema when structure matters</h3>
<p>
Syntax validation only answers “is this JSON?”. JSON Schema answers “is this the right shape?”:
required fields, types, enumerations, min/max, and more. For serious integrations, schema validation catches bugs earlier.
This tool focuses on strict JSON syntax; schema validation is a separate step.
</p>

<h2>Security & privacy notes</h2>
<p>
This tool is designed to run fully in the browser. That means your JSON stays on your device.
Still, be careful with sensitive payloads: if your browser has extensions that read pages, they could access input fields.
For highly sensitive data, use a clean browser profile and avoid unknown extensions.
</p>

<h2>Examples (8+)</h2>
<p class="muted">Each example shows input → formatted output. You can paste inputs into the tool and click Format.</p>

<h3>Example 1: Simple object</h3>
<pre><code>Input:
{"name":"Alice","active":true,"age":29}

Output:
{
  "name": "Alice",
  "active": true,
  "age": 29
}</code></pre>

<h3>Example 2: Nested arrays</h3>
<pre><code>Input:
{"tags":["json","format","validate"],"scores":[1,2,3]}

Output:
{
  "tags": [
    "json",
    "format",
    "validate"
  ],
  "scores": [
    1,
    2,
    3
  ]
}</code></pre>

<h3>Example 3: Escaped quotes</h3>
<pre><code>Input:
{"message":"She said: \"hello\"."}

Output:
{
  "message": "She said: \"hello\"."
}</code></pre>

<h3>Example 4: Windows path escaping</h3>
<pre><code>Input:
{"path":"C:\\Users\\Alice\\Documents\\file.txt"}

Output:
{
  "path": "C:\\Users\\Alice\\Documents\\file.txt"
}</code></pre>

<h3>Example 5: Booleans and null</h3>
<pre><code>Input:
{"ok":false,"value":null,"enabled":true}

Output:
{
  "ok": false,
  "value": null,
  "enabled": true
}</code></pre>

<h3>Example 6: API-style payload</h3>
<pre><code>Input:
{"user":{"id":"12345678901234567890","name":"Aki"},"roles":["admin","editor"]}

Output:
{
  "user": {
    "id": "12345678901234567890",
    "name": "Aki"
  },
  "roles": [
    "admin",
    "editor"
  ]
}</code></pre>

<h3>Example 7: Trailing comma (invalid → fix)</h3>
<pre><code>Invalid input:
{"a":1,"b":2,}

Fix:
{"a":1,"b":2}</code></pre>

<h3>Example 8: Missing comma (invalid → fix)</h3>
<pre><code>Invalid input:
{"a":1 "b":2}

Fix:
{"a":1,"b":2}</code></pre>

<h2>Troubleshooting (10+)</h2>
<ul>
  <li><strong>Trailing comma</strong>: remove the comma before <code>}</code> or <code>]</code>.</li>
  <li><strong>Single quotes</strong>: replace <code>'</code> with <code>"</code> for strings and keys.</li>
  <li><strong>Unquoted keys</strong>: change <code>{ name: "x" }</code> to <code>{ "name": "x" }</code>.</li>
  <li><strong>Comments present</strong>: remove <code>//</code> or <code>/* */</code> blocks.</li>
  <li><strong>Unescaped backslash</strong>: escape as <code>\\</code> inside strings.</li>
  <li><strong>Unescaped newline in string</strong>: use <code>\n</code> instead of an actual newline.</li>
  <li><strong>Cut-off JSON</strong>: ensure copy/paste includes the final closing bracket/brace.</li>
  <li><strong>Wrong bracket type</strong>: arrays use <code>[]</code>, objects use <code>{}</code>.</li>
  <li><strong>Invalid numbers</strong>: JSON does not allow <code>NaN</code> or <code>Infinity</code>.</li>
  <li><strong>Encoding issues</strong>: prefer UTF-8 when saving JSON files; avoid exotic encodings.</li>
</ul>

<h2>FAQ (10+)</h2>
<dl>
  <dt><strong>Is this tool private?</strong></dt>
  <dd>Yes. JSON formatting and validation run locally in your browser. No input is sent to a server.</dd>

  <dt><strong>Why can’t I use comments?</strong></dt>
  <dd>Standard JSON has no comment syntax. Some environments support JSONC, but strict parsers will reject it.</dd>

  <dt><strong>Why do trailing commas fail?</strong></dt>
  <dd>Strict JSON disallows trailing commas. Remove them before <code>}</code> or <code>]</code>.</dd>

  <dt><strong>What’s the difference between Format and Minify?</strong></dt>
  <dd>Format adds whitespace/indentation for readability. Minify removes whitespace to reduce size.</dd>

  <dt><strong>Does sorting keys change my data?</strong></dt>
  <dd>It should not change meaning, but it changes raw text. Some systems compare raw JSON strings, so use with care.</dd>

  <dt><strong>Can I validate against JSON Schema here?</strong></dt>
  <dd>This tool validates strict JSON syntax. Schema validation is a separate step and is planned as a related tool.</dd>

  <dt><strong>Why does my ID number change?</strong></dt>
  <dd>Large integers can lose precision in some tools. Store large IDs as strings.</dd>

  <dt><strong>Can JSON contain dates?</strong></dt>
  <dd>JSON has no date type. Use ISO 8601 strings (e.g., <code>"2026-01-27T12:34:56Z"</code>) and document it.</dd>

  <dt><strong>What content type should I use for APIs?</strong></dt>
  <dd>Typically <code>Content-Type: application/json; charset=utf-8</code>.</dd>

  <dt><strong>Why do I see “Unexpected end of JSON input”?</strong></dt>
  <dd>Your JSON is incomplete: missing a closing bracket/brace or an unclosed string.</dd>
</dl>

<h2>Glossary (10+)</h2>
<ul>
  <li><strong>JSON</strong>: JavaScript Object Notation, a text format for data exchange.</li>
  <li><strong>Object</strong>: Key-value mapping in braces <code>{}</code>.</li>
  <li><strong>Array</strong>: Ordered list in brackets <code>[]</code>.</li>
  <li><strong>String</strong>: Text value in double quotes.</li>
  <li><strong>Escape sequence</strong>: Backslash-based encoding like <code>\n</code>, <code>\"</code>, <code>\\</code>.</li>
  <li><strong>Minify</strong>: Remove whitespace to reduce size.</li>
  <li><strong>Pretty print</strong>: Add whitespace and indentation for readability.</li>
  <li><strong>Schema</strong>: A formal definition of expected JSON structure (JSON Schema).</li>
  <li><strong>UTF-8</strong>: Common encoding used for JSON text.</li>
  <li><strong>Trailing comma</strong>: Extra comma after the last element/property (invalid in JSON).</li>
</ul>

<h2>Related tools (5)</h2>
<ul>
  <li><strong>JSON to CSV Converter</strong> — Convert arrays/objects into CSV for spreadsheets. (Anchor: <em>JSON to CSV converter</em>)</li>
  <li><strong>CSV to JSON Converter</strong> — Turn CSV into JSON arrays with column mapping. (Anchor: <em>CSV to JSON</em>)</li>
  <li><strong>JSON Schema Validator</strong> — Validate data shape with JSON Schema rules. (Anchor: <em>JSON Schema validator</em>)</li>
  <li><strong>JWT Decoder</strong> — Decode JWT payload JSON safely in-browser. (Anchor: <em>JWT decode</em>)</li>
  <li><strong>Base64 Encoder/Decoder</strong> — Encode/decode API payload fragments. (Anchor: <em>Base64 decode</em>)</li>
</ul>

<h2>Popular tools</h2>
<ul>
  <li><a href="./">JSON Formatter & Validator</a></li>
  <li><a href="all-tools.html">All Tools</a></li>
</ul>

<h2>References (official docs)</h2>
<ul>
  <li><a href="https://www.rfc-editor.org/rfc/rfc8259" rel="nofollow">RFC 8259 — The JSON Data Interchange Format</a></li>
  <li><a href="https://www.ecma-international.org/publications-and-standards/standards/ecma-404/" rel="nofollow">ECMA-404 — The JSON Data Interchange Syntax</a></li>
  <li><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse" rel="nofollow">MDN: JSON.parse</a></li>
  <li><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify" rel="nofollow">MDN: JSON.stringify</a></li>
  <li><a href="https://json-schema.org/" rel="nofollow">JSON Schema (official site)</a></li>
</ul>
HTML

# -------------------------
# Translated content (ja/ko/zh) — full site i18n coverage for displayed text
# -------------------------
cat > "$BASE/content/index.ja.html" <<'HTML'
<h2>結論（Quick answer）</h2>
<p>
JSONが通らない原因の大半は、<strong>末尾カンマ</strong>・<strong>キーのダブルクォート忘れ</strong>・<strong>シングルクォート</strong>・<strong>括弧の対応ミス</strong>です。
左に貼り付けて <strong>検証</strong> を押し、エラー（多くの場合は行/列つき）を見て修正し、最後に <strong>整形</strong>（読みやすく）または <strong>最小化</strong>（軽量化）を使って仕上げます。
</p>

<h2>このツールの使い方</h2>
<ol>
  <li>入力欄にJSONを貼り付けます。迷ったら <strong>サンプル</strong> を押して、正しいJSONを入れてから試します。</li>
  <li><strong>検証</strong> を押し、strict JSONとして正しいか判定します。誤りがあればメッセージと行/列（可能な場合）を表示します。</li>
  <li><strong>整形</strong> で読みやすい形にし、<strong>最小化</strong> で空白を消してサイズを減らせます。</li>
  <li><strong>キーを並び替える</strong> は、文字列比較をするシステムでは差分が大きくなるので、必要なときだけ使います。</li>
  <li><strong>コピー</strong> / <strong>ダウンロード</strong> で結果を保存できます。入力はブラウザ内に自動保存されます。</li>
</ol>
<p class="muted">プライバシー：処理はブラウザ内だけで完結し、入力はサーバーへ送信されません。</p>

<h2>「有効なJSON」とは何か（重要）</h2>
<p>
ネット上の“JSONっぽい”例は、実はstrict JSONではないことがよくあります。strict JSONは仕様（RFC 8259 / ECMA-404）に従います。
ここを理解すると、APIデバッグや設定ファイルで毎回同じミスを繰り返さなくなります。
</p>

<h3>ルール：JSONの型は6つだけ</h3>
<ul>
  <li>オブジェクト：<code>{ "key": "value" }</code></li>
  <li>配列：<code>[1, 2, 3]</code></li>
  <li>文字列：<code>"text"</code>（ダブルクォートのみ）</li>
  <li>数値：<code>0</code>, <code>-12.34</code>, <code>1e6</code>（有限）</li>
  <li>真偽値：<code>true</code>/<code>false</code></li>
  <li>null：<code>null</code></li>
</ul>
<p><code>undefined</code> や <code>NaN</code>、<code>Infinity</code>、関数、<code>new Date()</code> はJSONではありません。</p>

<h3>ルール：キーは必ずダブルクォート</h3>
<pre><code>NG: { name: "Alice" }
OK: { "name": "Alice" }</code></pre>

<h3>ルール：文字列はダブルクォート</h3>
<pre><code>NG: { "name": 'Alice' }
OK: { "name": "Alice" }</code></pre>

<h3>ルール：末尾カンマ禁止</h3>
<pre><code>NG:
{ "a": 1, }

OK:
{ "a": 1 }</code></pre>

<h3>ルール：コメント禁止</h3>
<p><code>//</code> や <code>/* */</code> はJSONにありません。JSONC対応の環境以外は落ちます。</p>

<h2>典型エラーの直し方（順番が大事）</h2>
<ol>
  <li>まず <strong>検証</strong>。メッセージと位置（行/列）を見る。</li>
  <li>その位置の文字を確認（余計なカンマ、足りないクォート、括弧ミスが多い）。</li>
  <li><code>{}</code> と <code>[]</code> の対応を確認。</li>
  <li>1つ直したらすぐ再検証。まとめて直すと原因が分からなくなります。</li>
</ol>

<h2>具体例（8つ以上）</h2>
<p class="muted">入力→出力の例です。入力欄に貼って「整形」を押すと同じ形になります。</p>
<pre><code>例1 Input:
{"name":"Alice","active":true,"age":29}

Output:
{
  "name": "Alice",
  "active": true,
  "age": 29
}</code></pre>
<pre><code>例2 Input:
{"tags":["json","format","validate"],"scores":[1,2,3]}</code></pre>
<pre><code>例3 Input:
{"message":"She said: \"hello\"."}</code></pre>
<pre><code>例4 Input:
{"path":"C:\\Users\\Alice\\Documents\\file.txt"}</code></pre>
<pre><code>例5 Input:
{"ok":false,"value":null,"enabled":true}</code></pre>
<pre><code>例6 Input:
{"user":{"id":"12345678901234567890","name":"Aki"},"roles":["admin","editor"]}</code></pre>
<pre><code>例7 NG:
{"a":1,"b":2,}
Fix:
{"a":1,"b":2}</code></pre>
<pre><code>例8 NG:
{"a":1 "b":2}
Fix:
{"a":1,"b":2}</code></pre>

<h2>Troubleshooting（10個以上）</h2>
<ul>
  <li>末尾カンマを消す（<code>}</code>/<code>]</code> の直前）。</li>
  <li>シングルクォートをダブルクォートへ。</li>
  <li>キーを必ずダブルクォートで囲む。</li>
  <li>コメントを削除する（JSONCは別物）。</li>
  <li>バックスラッシュは <code>\\</code> にする。</li>
  <li>文字列内改行は <code>\n</code> にする。</li>
  <li>コピー漏れで末尾の括弧が落ちていないか。</li>
  <li><code>[]</code> と <code>{}</code> を混同していないか。</li>
  <li><code>NaN</code>/<code>Infinity</code> を使っていないか。</li>
  <li>UTF-8で保存されているか（別エンコーディングで崩れるケース）。</li>
</ul>

<h2>FAQ（10個以上）</h2>
<ul>
  <li><strong>安全？</strong>：ブラウザ内処理のみで、入力は送信されません。</li>
  <li><strong>コメントは？</strong>：標準JSONは不可です。</li>
  <li><strong>末尾カンマは？</strong>：不可です。</li>
  <li><strong>整形と最小化の違い</strong>：読みやすさ vs サイズ。</li>
  <li><strong>キー並び替え</strong>：意味は変えませんが、文字列比較の差分は変わります。</li>
  <li><strong>Schema検証</strong>：ここは構文のみ。形の検証はJSON Schemaで別途。</li>
  <li><strong>大きいID</strong>：数値だと丸められることがあるので文字列推奨。</li>
  <li><strong>日付</strong>：JSONに日付型はないのでISO文字列推奨。</li>
  <li><strong>Content-Type</strong>：APIは <code>application/json; charset=utf-8</code> が一般的。</li>
  <li><strong>Unexpected end</strong>：括弧/クォートが閉じていません。</li>
</ul>

<h2>用語集（10語以上）</h2>
<ul>
  <li><strong>JSON</strong>：データ交換のテキスト形式。</li>
  <li><strong>Object</strong>：<code>{}</code> のキー/値。</li>
  <li><strong>Array</strong>：<code>[]</code> の順序付きリスト。</li>
  <li><strong>Escape</strong>：<code>\n</code> や <code>\"</code> など。</li>
  <li><strong>Minify</strong>：空白削除。</li>
  <li><strong>Pretty print</strong>：整形。</li>
  <li><strong>Schema</strong>：構造ルール。</li>
  <li><strong>UTF-8</strong>：一般的な文字コード。</li>
  <li><strong>Trailing comma</strong>：末尾カンマ。</li>
  <li><strong>Strict</strong>：仕様に厳密なパース。</li>
</ul>

<h2>関連ツール（5つ）</h2>
<ul>
  <li>JSON to CSV Converter — スプレッドシート向けに変換</li>
  <li>CSV to JSON Converter — CSVをJSON配列へ</li>
  <li>JSON Schema Validator — 形の検証</li>
  <li>JWT Decoder — JWT payloadのJSON確認</li>
  <li>Base64 Encoder/Decoder — 文字列のエンコード/デコード</li>
</ul>

<h2>参考リンク（公式中心）</h2>
<ul>
  <li><a href="https://www.rfc-editor.org/rfc/rfc8259" rel="nofollow">RFC 8259</a></li>
  <li><a href="https://www.ecma-international.org/publications-and-standards/standards/ecma-404/" rel="nofollow">ECMA-404</a></li>
  <li><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse" rel="nofollow">MDN JSON.parse</a></li>
  <li><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify" rel="nofollow">MDN JSON.stringify</a></li>
  <li><a href="https://json-schema.org/" rel="nofollow">JSON Schema</a></li>
</ul>
HTML

cat > "$BASE/content/index.ko.html" <<'HTML'
<h2>Quick answer</h2>
<p>
JSON이 실패하는 가장 흔한 원인은 <strong>후행 쉼표</strong>, <strong>키 따옴표 누락</strong>, <strong>작은따옴표 사용</strong>, <strong>괄호 불일치</strong>입니다.
왼쪽에 붙여넣고 <strong>검증</strong>을 눌러 오류(가능하면 줄/열)를 확인한 뒤, <strong>정렬</strong>(가독성) 또는 <strong>축소</strong>(용량 감소)를 사용하세요.
</p>

<h2>사용 방법</h2>
<ol>
  <li>입력창에 JSON을 붙여넣습니다. 필요하면 <strong>예시</strong>로 정상 JSON을 불러옵니다.</li>
  <li><strong>검증</strong>을 눌러 strict JSON 문법을 확인합니다. 오류가 있으면 메시지와 위치를 표시합니다.</li>
  <li><strong>정렬</strong>로 보기 좋게, <strong>축소</strong>로 공백을 제거해 전송용으로 만듭니다.</li>
  <li><strong>키 정렬</strong>은 텍스트 비교가 중요한 시스템에서는 주의해서 사용합니다.</li>
  <li>결과는 복사/다운로드할 수 있고, 입력은 브라우저에 로컬 저장됩니다.</li>
</ol>
<p class="muted">개인정보: 모든 처리는 브라우저에서만 수행되며 입력은 서버로 전송되지 않습니다.</p>

<h2>유효한 JSON의 규칙</h2>
<ul>
  <li>키는 반드시 큰따옴표: <code>{"name":"A"}</code></li>
  <li>문자열도 큰따옴표만 허용</li>
  <li>후행 쉼표 금지: <code>{"a":1,}</code> 는 실패</li>
  <li>주석 금지: <code>//</code>, <code>/* */</code> 불가</li>
</ul>

<h2>Examples</h2>
<pre><code>Input: {"a":1,"b":2}
Output:
{
  "a": 1,
  "b": 2
}</code></pre>

<h2>Troubleshooting</h2>
<ul>
  <li>후행 쉼표 제거</li>
  <li>작은따옴표 → 큰따옴표</li>
  <li>키 따옴표 추가</li>
  <li>주석 제거</li>
  <li>백슬래시 이스케이프(\\)</li>
  <li>문자열 내 줄바꿈은 \n</li>
  <li>괄호 닫힘 확인</li>
  <li>NaN/Infinity 사용 금지</li>
  <li>UTF-8 저장 권장</li>
  <li>잘린 JSON 복구</li>
</ul>

<h2>References</h2>
<ul>
  <li><a href="https://www.rfc-editor.org/rfc/rfc8259" rel="nofollow">RFC 8259</a></li>
  <li><a href="https://www.ecma-international.org/publications-and-standards/standards/ecma-404/" rel="nofollow">ECMA-404</a></li>
  <li><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse" rel="nofollow">MDN JSON.parse</a></li>
  <li><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify" rel="nofollow">MDN JSON.stringify</a></li>
  <li><a href="https://json-schema.org/" rel="nofollow">JSON Schema</a></li>
</ul>
HTML

cat > "$BASE/content/index.zh.html" <<'HTML'
<h2>Quick answer</h2>
<p>
JSON 最常见的失败原因是：<strong>末尾多余逗号</strong>、<strong>对象键未加双引号</strong>、<strong>使用单引号</strong>、<strong>括号不匹配</strong>。
把 JSON 粘贴到左侧，点击<strong>校验</strong>查看错误（可能含行/列），再用<strong>格式化</strong>或<strong>压缩</strong>输出最终结果。
</p>

<h2>使用步骤</h2>
<ol>
  <li>粘贴 JSON，必要时点<strong>示例</strong>加载正确样例。</li>
  <li>点击<strong>校验</strong>，检查 strict JSON 语法。</li>
  <li>点击<strong>格式化</strong>生成易读缩进，或<strong>压缩</strong>去除空白用于传输。</li>
  <li><strong>键排序</strong>会改变原始文本顺序，只有在确定安全时使用。</li>
  <li>输出可复制/下载，输入会保存在浏览器本地。</li>
</ol>
<p class="muted">隐私：全部在浏览器本地运行，输入不会发送到服务器。</p>

<h2>有效 JSON 的关键规则</h2>
<ul>
  <li>键必须使用双引号：<code>{"name":"A"}</code></li>
  <li>字符串只能用双引号</li>
  <li>禁止末尾逗号：<code>{"a":1,}</code> 无效</li>
  <li>禁止注释：<code>//</code>、<code>/* */</code> 不支持</li>
</ul>

<h2>排错要点</h2>
<ul>
  <li>删除末尾逗号</li>
  <li>单引号改双引号</li>
  <li>补齐括号与引号</li>
  <li>反斜杠需要转义（\\）</li>
  <li>字符串内换行用 \n</li>
</ul>

<h2>References</h2>
<ul>
  <li><a href="https://www.rfc-editor.org/rfc/rfc8259" rel="nofollow">RFC 8259</a></li>
  <li><a href="https://www.ecma-international.org/publications-and-standards/standards/ecma-404/" rel="nofollow">ECMA-404</a></li>
  <li><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse" rel="nofollow">MDN JSON.parse</a></li>
  <li><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify" rel="nofollow">MDN JSON.stringify</a></li>
  <li><a href="https://json-schema.org/" rel="nofollow">JSON Schema</a></li>
</ul>
HTML

# -------------------------
# content for other pages (unique, per language)
# -------------------------
cat > "$BASE/content/about.en.html" <<'HTML'
<h2>About</h2>
<p>
JSON Formatter & Validator is a small, fast, client-side tool built for practical debugging: API payloads, config files,
webhook events, and data exports. The goal is simple: help you get to a <em>valid</em>, readable JSON result quickly,
with clear error location and real troubleshooting steps—not vague advice.
</p>
<p>
This site is intentionally lightweight (no tracking-heavy frameworks). For extremely sensitive data, we still recommend using a clean browser profile
and minimizing extensions that can read page content.
</p>
HTML

cat > "$BASE/content/about.ja.html" <<'HTML'
<h2>運営者情報</h2>
<p>
このサイトは、APIのペイロード・設定ファイル・Webhook・データ出力などで頻出するJSONのトラブルを、
<strong>最短で解決する</strong>ために作られた「ブラウザ内完結」の実用ツールです。抽象的な説明ではなく、
その場で直せる手順と典型ミスの整理に重きを置いています。
</p>
HTML

cat > "$BASE/content/about.ko.html" <<'HTML'
<h2>About</h2>
<p>
이 사이트는 API 페이로드, 설정 파일, 웹훅, 데이터 내보내기에서 자주 발생하는 JSON 문제를 빠르게 해결하기 위한
브라우저 기반 도구입니다. 추상적인 설명보다 “지금 당장 고치는 방법”을 우선합니다.
</p>
HTML

cat > "$BASE/content/about.zh.html" <<'HTML'
<h2>About</h2>
<p>
本工具用于快速解决 API 载荷、配置文件、Webhook、数据导出中常见的 JSON 问题。目标是用清晰的步骤与可复现的排错方法，
帮助您尽快得到“有效且可读”的 JSON 结果。
</p>
HTML

cat > "$BASE/content/contact.en.html" <<'HTML'
<h2>Contact</h2>
<p>
For feedback, bug reports, or improvement requests, contact us via the email address listed on the main domain contact page.
Please include:
</p>
<ul>
  <li>The URL of the page you were on</li>
  <li>Your browser name/version</li>
  <li>A minimal JSON sample (remove sensitive data)</li>
  <li>The exact error message shown</li>
</ul>
HTML

cat > "$BASE/content/contact.ja.html" <<'HTML'
<h2>お問い合わせ</h2>
<p>
不具合報告・改善要望は、メインドメインの問い合わせ先へお願いします。送るときは以下を添えると早いです。
</p>
<ul>
  <li>見ていたページURL</li>
  <li>ブラウザ名/バージョン</li>
  <li>最小の再現JSON（機密は削除）</li>
  <li>表示されたエラーメッセージ全文</li>
</ul>
HTML

cat > "$BASE/content/contact.ko.html" <<'HTML'
<h2>Contact</h2>
<p>
버그 제보/개선 요청은 메인 도메인의 문의 채널로 보내주세요. 아래 정보를 포함하면 처리 속도가 빨라집니다.
</p>
<ul>
  <li>페이지 URL</li>
  <li>브라우저 버전</li>
  <li>민감 정보를 제거한 최소 JSON 예시</li>
  <li>표시된 오류 메시지</li>
</ul>
HTML

cat > "$BASE/content/contact.zh.html" <<'HTML'
<h2>Contact</h2>
<p>
反馈与问题报告请通过主域名的联系方式提交。为便于定位，请附上：
</p>
<ul>
  <li>页面 URL</li>
  <li>浏览器版本</li>
  <li>去除敏感信息的最小 JSON 样例</li>
  <li>页面显示的完整错误信息</li>
</ul>
HTML

cat > "$BASE/content/privacy.en.html" <<'HTML'
<h2>Privacy</h2>
<p>
This tool runs locally in your browser. Your JSON input is not transmitted to our servers by the tool itself.
However, your browser and extensions may have their own behaviors. If you handle sensitive information,
use a trusted browser profile and avoid extensions that can read page content.
</p>
<p>
We may use advertising (Google AdSense) in a compliant, family-safe way. We do not ask users to click ads and we do not use deceptive UI.
If cookies are used by advertising providers, that is handled by those providers under their policies.
</p>
HTML

cat > "$BASE/content/privacy.ja.html" <<'HTML'
<h2>プライバシー</h2>
<p>
本ツールはブラウザ内で動作し、入力JSONをツール側でサーバー送信しません。ただし、ブラウザ拡張機能などが内容を読み取る可能性はあります。
機密情報を扱う場合は、信頼できる環境（拡張を減らす等）で利用してください。
</p>
<p>
広告（Google AdSense）を表示する場合でも、クリック誘導や誤解を招く表現は行いません。Cookie等は広告配信事業者の仕組みにより利用される場合があります。
</p>
HTML

cat > "$BASE/content/privacy.ko.html" <<'HTML'
<h2>Privacy</h2>
<p>
본 도구는 브라우저에서 로컬로 실행되며 입력 JSON을 서버로 전송하지 않습니다. 단, 브라우저 확장 프로그램 등은 페이지 내용을 읽을 수 있으므로,
민감한 데이터는 신뢰할 수 있는 환경에서 처리하세요.
</p>
<p>
광고(예: Google AdSense)를 표시하더라도 클릭 유도나 오해를 부르는 UI는 사용하지 않습니다. 쿠키 등은 광고 제공자의 정책에 따라 사용될 수 있습니다.
</p>
HTML

cat > "$BASE/content/privacy.zh.html" <<'HTML'
<h2>Privacy</h2>
<p>
本工具在浏览器本地运行，不会将输入 JSON 发送到服务器。但浏览器扩展等可能读取页面内容，处理敏感数据时请使用可信环境。
</p>
<p>
如展示广告（例如 Google AdSense），我们不会进行点击诱导或误导性展示。Cookie 等可能由广告提供方依据其政策使用。
</p>
HTML

cat > "$BASE/content/terms.en.html" <<'HTML'
<h2>Terms</h2>
<p>
By using this site, you agree that the tool is provided “as is” without warranties. You are responsible for verifying outputs before using them in production,
especially for API payloads and configuration files.
</p>
<p>
You must not use this site for illegal activities, harmful content, or to generate deceptive traffic. We reserve the right to update the site content and tool behavior
to improve accuracy, performance, and compliance.
</p>
HTML

cat > "$BASE/content/terms.ja.html" <<'HTML'
<h2>利用規約</h2>
<p>
本サイトおよびツールは現状有姿で提供されます。出力結果を実運用で使う前に、利用者自身で検証してください（APIや設定ファイルは特に重要です）。
</p>
<p>
違法行為や不正トラフィック、誤解を招く用途での利用は禁止します。品質向上・安全性・規約対応のため、内容や挙動を更新する場合があります。
</p>
HTML

cat > "$BASE/content/terms.ko.html" <<'HTML'
<h2>Terms</h2>
<p>
본 사이트와 도구는 “있는 그대로” 제공됩니다. 출력 결과를 실제 서비스에 적용하기 전에 반드시 사용자가 검증해야 합니다.
</p>
<p>
불법 행위, 부정 트래픽, 오해를 유발하는 목적의 사용은 금지됩니다. 품질과 규정 준수를 위해 내용/동작을 업데이트할 수 있습니다.
</p>
HTML

cat > "$BASE/content/terms.zh.html" <<'HTML'
<h2>Terms</h2>
<p>
本网站与工具按“现状”提供。将输出用于生产环境前，请自行验证，尤其是 API 载荷与配置文件。
</p>
<p>
禁止用于违法活动、不正当流量或误导性用途。为提升质量、性能与合规性，我们可能更新内容与工具行为。
</p>
HTML

cat > "$BASE/content/disclaimer.en.html" <<'HTML'
<h2>Disclaimer</h2>
<p>
This site provides tooling and educational content for JSON formatting and validation. It does not provide legal, financial, or security guarantees.
Always confirm the correctness of outputs and the suitability of JSON for your specific system.
</p>
<p>
We do not claim affiliation with any third-party services referenced in the documentation. References are provided for convenience.
</p>
HTML

cat > "$BASE/content/disclaimer.ja.html" <<'HTML'
<h2>免責事項</h2>
<p>
本サイトはJSONの整形・検証のためのツールおよび解説を提供します。出力の正確性や安全性を保証するものではありません。
必ず利用者自身で妥当性を確認してください。
</p>
<p>
記載している外部サービス/外部ドキュメントへのリンクは便宜上のもので、提携や保証を意味しません。
</p>
HTML

cat > "$BASE/content/disclaimer.ko.html" <<'HTML'
<h2>Disclaimer</h2>
<p>
본 사이트는 JSON 정렬/검증 도구와 학습용 콘텐츠를 제공합니다. 결과의 정확성이나 시스템 적합성을 보장하지 않습니다.
사용자는 반드시 스스로 확인해야 합니다.
</p>
<p>
외부 링크는 참고용이며 제휴 또는 보증을 의미하지 않습니다.
</p>
HTML

cat > "$BASE/content/disclaimer.zh.html" <<'HTML'
<h2>Disclaimer</h2>
<p>
本网站提供 JSON 格式化/校验工具与学习内容，不对输出的准确性或适用性作保证。使用前请自行确认。
</p>
<p>
外部链接仅为参考，不代表任何合作或担保。
</p>
HTML

cat > "$BASE/content/all-tools.en.html" <<'HTML'
<h2>All Tools</h2>
<p class="muted">This page will list all tools as they are added. For now, one tool is live.</p>
<ul>
  <li><a href="./">JSON Formatter & Validator</a> — Pretty print, minify, validate, and debug JSON with line/column hints.</li>
</ul>
HTML

cat > "$BASE/content/all-tools.ja.html" <<'HTML'
<h2>全ツール</h2>
<p class="muted">追加され次第ここに一覧化します。現在は1ツールのみ公開中です。</p>
<ul>
  <li><a href="./">JSON フォーマッター & バリデーター</a> — 整形/最小化/検証/行列つきエラー。</li>
</ul>
HTML

cat > "$BASE/content/all-tools.ko.html" <<'HTML'
<h2>All Tools</h2>
<p class="muted">도구가 추가되면 여기에서 모두 볼 수 있습니다. 현재는 1개 도구만 공개되어 있습니다.</p>
<ul>
  <li><a href="./">JSON Formatter & Validator</a> — 정렬/축소/검증/줄·열 오류 표시.</li>
</ul>
HTML

cat > "$BASE/content/all-tools.zh.html" <<'HTML'
<h2>All Tools</h2>
<p class="muted">工具添加后会在此汇总。目前仅上线 1 个工具。</p>
<ul>
  <li><a href="./">JSON 格式化与校验</a> — 格式化/压缩/校验/行列提示。</li>
</ul>
HTML

echo "OK: generated $BASE (tool + pages + i18n content)."
