/*
  Запоминание места чтения и прогресс для веб-версии книги (read/).
  Копируется в read/reader.js скриптом build_read.py.

  Всё хранится в localStorage этого браузера:
    last — страница и номер абзаца, на котором остановился читатель,
           и признак того, что глава дочитана до конца;
    done — список дочитанных до конца страниц.
*/

(function () {
  "use strict";

  var KEY = "lotm-read:v1";

  function load() {
    try {
      var state = JSON.parse(localStorage.getItem(KEY));
      if (state && Array.isArray(state.done)) return state;
    } catch (e) {}
    return { last: null, done: [] };
  }

  function save(state) {
    try {
      localStorage.setItem(KEY, JSON.stringify(state));
    } catch (e) {}
  }

  var page = location.pathname.split("/").pop();

  // Страницы глав — XHTML, а XML-парсер Chrome игнорирует defer
  // и выполняет скрипт прямо в <head>, до появления текста
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }

  function init() {
    if (/^index\d+\.xhtml$/.test(page)) {
      initChapter();
    } else if (document.getElementById("resume")) {
      initToc();
    }
  }

  // ── Страница главы ──────────────────────────────────────

  function initChapter() {
    var paragraphs = document.querySelectorAll(".main-body p");
    var state = load();

    // Абзац, который сейчас у верхнего края экрана
    function currentParagraph() {
      for (var i = 0; i < paragraphs.length; i++) {
        if (paragraphs[i].getBoundingClientRect().bottom > 0) return i;
      }
      return 0;
    }

    function remember() {
      var last = state.last && state.last.page === page ? state.last : { page: page };
      last.para = currentParagraph();
      last.finished = state.done.indexOf(page) !== -1 && last.finished;
      state.last = last;
      save(state);
    }

    // Переход по «Продолжить» — возвращаемся к сохранённому абзацу
    if (location.hash === "#continue") {
      var target = state.last && state.last.page === page && paragraphs[state.last.para];
      var restore = function () {
        if (target) target.scrollIntoView({ block: "start" });
      };
      restore();
      // Шрифт может догрузиться и сдвинуть текст — повторяем после загрузки
      if (document.fonts && document.fonts.ready) document.fonts.ready.then(restore);
      history.replaceState(null, "", location.pathname + location.search);
    }

    var timer = null;
    window.addEventListener("scroll", function () {
      clearTimeout(timer);
      timer = setTimeout(remember, 300);
    }, { passive: true });

    document.addEventListener("visibilitychange", function () {
      if (document.visibilityState === "hidden") remember();
    });

    // Дочитал до нижней навигации — глава прочитана
    var navs = document.querySelectorAll(".read-nav");
    var end = navs[navs.length - 1];
    if (end && paragraphs.length && "IntersectionObserver" in window) {
      new IntersectionObserver(function (entries, observer) {
        if (!entries[0].isIntersecting) return;
        // Короткая глава может целиком уместиться на экране сразу —
        // засчитываем, только если читатель пробыл на ней хоть немного
        setTimeout(function () {
          state = load();
          if (state.done.indexOf(page) === -1) state.done.push(page);
          state.last = { page: page, para: currentParagraph(), finished: true };
          save(state);
        }, 1500);
        observer.disconnect();
      }).observe(end);
    }

    remember();
  }

  // ── Оглавление ──────────────────────────────────────────

  function initToc() {
    var state = load();
    var links = Array.prototype.slice.call(document.querySelectorAll(".toc li a"));
    var hrefs = links.map(function (a) { return a.getAttribute("href"); });
    var done = {};
    state.done.forEach(function (p) { done[p] = true; });

    var readCount = 0;
    links.forEach(function (a, i) {
      if (done[hrefs[i]]) {
        a.classList.add("is-read");
        readCount++;
      }
    });

    if (!state.last && !readCount) return;

    // Куда продолжать: дочитанная глава → следующая по оглавлению
    var target = state.last ? state.last.page : null;
    var hash = "#continue";
    if (state.last && state.last.finished) {
      var i = hrefs.indexOf(target);
      if (i !== -1 && i + 1 < hrefs.length) {
        target = hrefs[i + 1];
        hash = "";
      }
    }

    var resume = document.getElementById("resume");
    var html = "";

    if (target) {
      var link = document.querySelector('.toc a[href="' + target + '"]');
      var title = link ? link.textContent : "";
      html +=
        '<a class="resume-btn" href="' + target + hash + '">' +
        '<span class="resume-label">Продолжить чтение</span>' +
        '<span class="resume-title"></span></a>';

      if (link) {
        link.classList.add("is-current");
        var details = link.closest("details");
        if (details) details.open = true;
      }
    }

    var percent = links.length ? Math.floor((readCount / links.length) * 100) : 0;
    var percentText = percent === 0 && readCount > 0 ? "менее 1%" : percent + "%";
    html +=
      '<div class="progress" role="progressbar" aria-valuemin="0" aria-valuemax="' + links.length +
      '" aria-valuenow="' + readCount + '"><div class="progress-bar" style="width:' + percent + '%"></div></div>' +
      '<p class="progress-text">Прочитано ' + readCount + " из " + links.length + " глав · " + percentText + "</p>";

    resume.innerHTML = html;
    if (target) resume.querySelector(".resume-title").textContent = title;
    resume.hidden = false;
  }
})();
