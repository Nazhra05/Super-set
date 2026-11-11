// Claude Code status line (W-06). Saves the status JSON to .claude/usage.json so the
// router can read plan usage and context size, then prints one short line.
const fs = require("fs");
const path = require("path");

let raw = "";
process.stdin.on("data", (c) => (raw += c));
process.stdin.on("end", () => {
  let s = {};
  try {
    s = JSON.parse(raw);
  } catch {
    process.stdout.write("usage: ?");
    return;
  }
  const out = path.join(__dirname, "..", ".claude", "usage.json");
  try {
    fs.writeFileSync(out, JSON.stringify({ savedAt: new Date().toISOString(), ...s }, null, 2));
  } catch {
    // Status line must never fail; the router treats a stale file as unknown.
  }
  const pct = (v) => (typeof v === "number" ? `${Math.round(v)}%` : "?");
  const tok = (v) =>
    typeof v !== "number" ? "?" : v >= 1e6 ? `${+(v / 1e6).toFixed(1)}M` : `${Math.round(v / 1000)}k`;
  const cw = s.context_window || {};
  const parts = [
    `ctx ${pct(cw.used_percentage)} (${tok(cw.total_input_tokens)}/${tok(cw.context_window_size)} tok)`,
    `5h ${pct(s.rate_limits?.five_hour?.used_percentage)}`,
    `7d ${pct(s.rate_limits?.seven_day?.used_percentage)}`,
  ];
  if (typeof s.cost?.total_cost_usd === "number") parts.push(`$${s.cost.total_cost_usd.toFixed(2)}`);
  process.stdout.write(parts.join(" | "));
});
