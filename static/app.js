async function fetchWithTimeout(url, options = {}, timeoutMs = 10000) {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), timeoutMs);
  try {
    return await fetch(url, {...options, signal: controller.signal});
  } finally {
    clearTimeout(timeout);
  }
}

async function loadHealth() {
  const response = await fetchWithTimeout("/health");
  if (!response.ok) {
    throw new Error(`Health check returned HTTP ${response.status}`);
  }
  const health = await response.json();
  document.querySelector("#deployment-sha").textContent = `Deployed commit: ${health.commit_sha}`;
}

function showResult(output, text, isError = false) {
  output.textContent = text;
  output.classList.toggle("error", isError);
}

document.querySelectorAll(".card").forEach((card) => {
  const name = card.dataset.function;
  const input = card.querySelector("textarea");
  const output = card.querySelector(".result");
  card.querySelector(".run").addEventListener("click", async () => {
    showResult(output, "Running...");
    try {
      const parsed = JSON.parse(input.value);
      const response = await fetchWithTimeout(`/api/functions/${name}`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({args: parsed}),
      }, 20000);
      const body = await response.json();
      if (!response.ok) {
        showResult(output, `${body.error_type}: ${body.error}`, true);
        return;
      }
      showResult(output, `${body.result_type}: ${JSON.stringify(body.result)}`);
    } catch (error) {
      showResult(output, `Input error: ${error.message}`, true);
    }
  });
  card.querySelector(".clear").addEventListener("click", () => {
    input.value = "[]";
    showResult(output, "Ready.");
  });
});

loadHealth().catch((error) => {
  document.querySelector("#deployment-sha").textContent = `Health check unavailable: ${error.message}`;
});
