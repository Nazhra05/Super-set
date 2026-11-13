#!/usr/bin/env node
// Antigravity PreToolUse hook: blocks reading, editing, writing, or printing .env files.
let raw = "";
process.stdin.setEncoding("utf8");
process.stdin.on("data", (chunk) => { raw += chunk; });
process.stdin.on("end", () => {
  try {
    const input = JSON.parse(raw || "{}");
    const tc = input.toolCall || {};
    const args = tc.args || {};
    const pathArg = String(args.Path || "");
    const cmdArg = String(args.CommandLine || "");
    const envFileRe = /(^|[\\/])\.env(\.|$)/i;
    if (pathArg && envFileRe.test(pathArg)) {
      process.stdout.write(JSON.stringify({
        decision: "deny",
        reason: "Access to .env files is blocked by project workflow rules (env-guard)."
      }));
      return;
    }
    if (cmdArg && /(^|\s|["'`/\\])\.env(\.[a-zA-Z0-9_-]+)?(\s|["'`]|$)/.test(cmdArg) && !/git\s+ls-files/.test(cmdArg)) {
      process.stdout.write(JSON.stringify({
        decision: "deny",
        reason: "Shell commands referencing .env files are blocked by project workflow rules (env-guard)."
      }));
      return;
    }
  } catch (_) {}
  process.stdout.write(JSON.stringify({ decision: "allow" }));
});

