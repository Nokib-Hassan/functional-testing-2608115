async function loadHealth() {
  const response = await fetch("/health");
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
      const response = await fetch(`/api/functions/${name}`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({args: parsed}),
      });
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
