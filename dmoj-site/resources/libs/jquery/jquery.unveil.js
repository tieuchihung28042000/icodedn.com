/**
 * Minified by jsDelivr using Terser v5.37.0.
 * Original file: /npm/jquery-unveil@1.3.2/jquery.unveil.js
 *
 * Do NOT use SRI with dynamically generated files! More information: https://www.jsdelivr.com/using-sri-with-dynamic-files
 */
!function(t){t.fn.unveil=function(i,e){var n,o=t(window),r=i||0,u=window.devicePixelRatio>1?"data-src-retina":"data-src",s=this;function l(){var i=s.filter((function(){var i=t(this),e=o.scrollTop(),n=e+o.height(),u=i.offset().top;return u+i.height()>=e-r&&u<=n+r}));n=i.trigger("unveil"),s=s.not(n)}return this.one("unveil",(function(){var t=this.getAttribute(u);(t=t||this.getAttribute("data-src"))&&(this.setAttribute("src",t),"function"==typeof e&&e.call(this))})),o.on("scroll.unveil resize.unveil lookup.unveil",l),l(),this}}(window.jQuery||window.Zepto);
//# sourceMappingURL=/sm/f66a23976ed42d710713d14c164920995a9e184889485407ba437fd1a21e0647.map