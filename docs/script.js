// ===== 아주 작은 동작들 (외부 라이브러리 없이 순수 JS) =====

// 1) 푸터의 연도를 자동으로 채운다
document.getElementById("year").textContent = new Date().getFullYear();

// 2) 다크모드 토글 (선택을 localStorage에 기억)
const root = document.documentElement;
const toggle = document.getElementById("themeToggle");

// 저장된 설정이 있으면 적용, 없으면 OS 설정을 따른다
const saved = localStorage.getItem("theme");
const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
applyTheme(saved || (prefersDark ? "dark" : "light"));

toggle.addEventListener("click", () => {
  const next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
  applyTheme(next);
  localStorage.setItem("theme", next);
});

function applyTheme(theme) {
  root.setAttribute("data-theme", theme);
  toggle.textContent = theme === "dark" ? "☀️" : "🌙";
}

// 3) 같은 페이지 안의 앵커(#) 링크만 부드럽게 스크롤 (페이지 이동 링크는 그대로)
document.querySelectorAll('a[href^="#"]').forEach((link) => {
  link.addEventListener("click", (e) => {
    const target = document.querySelector(link.getAttribute("href"));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: "smooth" });
    }
  });
});
