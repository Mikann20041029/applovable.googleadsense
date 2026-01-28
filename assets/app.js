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
