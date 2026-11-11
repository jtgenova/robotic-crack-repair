"use strict";
// Unweighted means of six trial MAEs from Tables 6 and 7.
const metrics = {
  fill: { title: "Fill-error MAE (%)", unit: "%", maximum: 40, table: 6,
    values: [[29.21,34.86,35.81,30.62,33.05,34.68], [26.55,28.54,29.49,29.91,30.45,36.15], [26.12,27.13,30.50,24.40,27.12,28.67], [10.68,14.13,15.11,9.36,11.36,12.36]] },
  depth: { title: "Depth-error MAE (mm)", unit: " mm", maximum: 3, table: 7,
    values: [[1.94,2.95,2.47,2.33,2.63,2.91], [2.15,2.43,2.02,1.79,2.21,2.89], [1.98,2.54,2.91,1.94,2.02,2.23], [0.83,1.23,1.13,0.68,0.49,0.92]] }
};
const metricButtons = document.querySelectorAll("[data-metric]");
metricButtons.forEach(button => button.addEventListener("click", () => {
  const metric = metrics[button.dataset.metric];
  document.getElementById("chart-title").textContent = metric.title;
  document.querySelectorAll(".bar-row").forEach((row, index) => {
    const mean = metric.values[index].reduce((sum, value) => sum + value, 0) / 6;
    row.querySelector(".bar").style.setProperty("--bar-width", `${mean / metric.maximum * 100}%`);
    row.querySelector("strong").textContent = mean.toFixed(2) + metric.unit;
  });
  document.getElementById("chart-source").textContent = `Calculated from Table ${metric.table}. Unweighted means of trial MAEs, rather than pooled waypoint errors. See Tables 6 and 7 in the paper for full trial results.`;
  metricButtons.forEach(other => other.setAttribute("aria-pressed", String(other === button)));
}));
const copyButton = document.getElementById("copy-citation");
copyButton.hidden = false;
copyButton.addEventListener("click", async () => {
  const citation = document.getElementById("bibtex");
  const status = document.getElementById("copy-status");
  try {
    if (!navigator.clipboard || !window.isSecureContext) throw new Error("Clipboard unavailable");
    await navigator.clipboard.writeText(citation.textContent);
    status.textContent = "BibTeX copied to clipboard.";
  } catch {
    const range = document.createRange();
    range.selectNodeContents(citation);
    const selection = window.getSelection();
    selection.removeAllRanges();
    selection.addRange(range);
    status.textContent = "Citation selected. Press Ctrl+C (or Command+C) to copy.";
  }
});
