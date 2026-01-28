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
