// MathJax configuration for pymdownx.arithmatex (generic mode).
//
// Arithmatex wraps each formula in an element with class "arithmatex"; MathJax
// renders those. `document$` is Zensical/Material's instant-navigation
// observable, so we re-typeset after every client-side page swap.
window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true,
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex",
  },
};

// Re-typeset on every (instant-)navigation. The guard matters: `document$` fires
// its first emission immediately — before the MathJax library (loaded by the
// next <script>) exists. Without it, `MathJax.typesetPromise()` throws, RxJS
// tears the subscription down, and any page reached via instant navigation never
// gets typeset (its formulas render blank). On the very first load MathJax's own
// startup handles typesetting; this subscription then covers later navigations.
if (typeof document$ !== "undefined") {
  document$.subscribe(function () {
    if (window.MathJax && MathJax.typesetPromise) {
      MathJax.startup.output.clearCache();
      MathJax.typesetClear();
      MathJax.texReset();
      MathJax.typesetPromise();
    }
  });
}
