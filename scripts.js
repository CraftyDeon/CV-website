// ===== Hello Test =====
function sayHello() {
  alert("Hello World");
}

// ===== Experience Slider =====
let currentIndex = 0;
const container = document.getElementById("experience-container");
const items = document.querySelectorAll(".experience-item");

function showSlide(index) {
  if (index < 0) currentIndex = items.length - 1;
  else if (index >= items.length) currentIndex = 0;
  else currentIndex = index;
  container.style.transform = "translateX(" + (-currentIndex * 100) + "%)";
}
function prevSlide() { showSlide(currentIndex - 1); }
function nextSlide() { showSlide(currentIndex + 1); }
setInterval(nextSlide, 6000);

// ===== Skills Animation =====
const skillCircles = document.querySelectorAll('.skill-circle');

const skillObserver = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    const circle = entry.target;
    const percent = circle.getAttribute("data-percent");
    const textEl = circle.querySelector('.skill-percent');

    if (entry.isIntersecting) {
      let current = 0;
      const animateFill = setInterval(() => {
        if (current >= percent) {
          clearInterval(animateFill);
        } else {
          current++;
          circle.style.setProperty("--percent", current + "%");
          textEl.textContent = current + "%";
        }
      }, 15);
    } else {
      circle.style.setProperty("--percent", "0%");
      textEl.textContent = "0%";
    }
  });
}, { threshold: 0.5 });

skillCircles.forEach(circle => skillObserver.observe(circle));
