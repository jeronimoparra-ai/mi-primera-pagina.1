const navToggle = document.querySelector(".nav-toggle");
const navMenu = document.querySelector(".nav-menu");
const navLinks = document.querySelectorAll(".nav-menu a");
const yearElement = document.querySelector("#year");
const revealElements = document.querySelectorAll(".reveal");

if (yearElement) {
  yearElement.textContent = new Date().getFullYear();
}

if (navToggle && navMenu) {
  const closeMenu = () => {
    navMenu.classList.remove("is-open");
    navToggle.setAttribute("aria-expanded", "false");
  };

  navToggle.addEventListener("click", () => {
    navMenu.classList.toggle("is-open");
    navToggle.setAttribute(
      "aria-expanded",
      String(navMenu.classList.contains("is-open"))
    );
  });

  navLinks.forEach((link) => {
    link.addEventListener("click", closeMenu);
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      closeMenu();
    }
  });

  document.addEventListener("click", (event) => {
    const target = event.target;
    if (
      target instanceof Node &&
      !navMenu.contains(target) &&
      !navToggle.contains(target)
    ) {
      closeMenu();
    }
  });
}

const showElement = (element) => element.classList.add("reveal-visible");

if ("IntersectionObserver" in window) {
  const observer = new IntersectionObserver(
    (entries, obs) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          showElement(entry.target);
          obs.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15 }
  );

  revealElements.forEach((element) => observer.observe(element));
} else {
  revealElements.forEach(showElement);
}
