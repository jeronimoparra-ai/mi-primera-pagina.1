const navToggle = document.querySelector(".nav-toggle");
const navMenu = document.querySelector(".nav-menu");
const navLinks = document.querySelectorAll(".nav-menu a");
const yearElement = document.querySelector("#year");
const revealElements = document.querySelectorAll(".reveal");
const retoButtons = document.querySelectorAll(".reto-btn");
const retoPanels = document.querySelectorAll(".reto-panel");
const parseDurationToMs = (durationValue) => {
  const value = durationValue.trim();
  if (value.endsWith("ms")) {
    return Number.parseFloat(value);
  }

  if (value.endsWith("s")) {
    return Number.parseFloat(value) * 1000;
  }

  return NaN;
};

const panelTransitionToken = getComputedStyle(document.documentElement).getPropertyValue(
  "--transition-panel"
);
const parsedPanelTransition = parseDurationToMs(panelTransitionToken);
const PANEL_TRANSITION_DURATION = Number.isFinite(parsedPanelTransition)
  ? parsedPanelTransition
  : 350;

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
    if (event.key === "Escape" && navMenu.classList.contains("is-open")) {
      closeMenu();
    }
  });

  document.addEventListener("click", (event) => {
    if (!navMenu.classList.contains("is-open")) {
      return;
    }

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

if (retoButtons.length && retoPanels.length) {
  let activePanelId = null;

  const closePanel = (button, panel) => {
    panel.classList.remove("open");
    button.classList.remove("active");
    button.setAttribute("aria-expanded", "false");
    setTimeout(() => {
      if (!panel.classList.contains("open")) {
        panel.hidden = true;
      }
    }, PANEL_TRANSITION_DURATION);
  };

  const openPanel = (button, panel) => {
    panel.hidden = false;
    requestAnimationFrame(() => panel.classList.add("open"));
    button.classList.add("active");
    button.setAttribute("aria-expanded", "true");
    activePanelId = panel.id;
  };

  const getButtonByPanelId = (panelId) =>
    Array.from(retoButtons).find(
      (button) => button.getAttribute("data-target") === panelId
    );

  const toggleChallenge = (button) => {
    const targetId = button.getAttribute("data-target");
    const panel = document.getElementById(targetId);
    if (!targetId || !panel) {
      return;
    }

    if (activePanelId === targetId) {
      closePanel(button, panel);
      activePanelId = null;
      return;
    }

    if (activePanelId) {
      const previousPanel = document.getElementById(activePanelId);
      const previousButton = getButtonByPanelId(activePanelId);
      if (previousPanel && previousButton) {
        closePanel(previousButton, previousPanel);
      }
    }

    openPanel(button, panel);
  };

  retoButtons.forEach((button, index, buttons) => {
    button.addEventListener("click", () => toggleChallenge(button));

    button.addEventListener("keydown", (event) => {
      const isNext = event.key === "ArrowRight" || event.key === "ArrowDown";
      const isPrevious = event.key === "ArrowLeft" || event.key === "ArrowUp";

      if (!isNext && !isPrevious) {
        return;
      }

      event.preventDefault();
      const offset = isNext ? 1 : -1;
      const nextIndex = (index + offset + buttons.length) % buttons.length;
      buttons[nextIndex].focus();
    });
  });
}
