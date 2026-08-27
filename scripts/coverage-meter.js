#!/usr/bin/env node
// coverage-meter: nyc|jest → {actual%, target%, gap, branches[]}
import { execSync } from "child_process";
import * as fs from "fs";
import * as path from "path";
function parseArgs() {
  const args = process.argv.slice(2);
  const opts = { tool: "nyc", target: 80, output: "text" };
  for (let i = 0; i < args.length; i++) {
    if (args[i] === "--tool") opts.tool = args[++i];
    if (args[i] === "--target") opts.target = parseInt(args[++i]);
    if (args[i] === "--output") opts.output = args[++i];
  }
  return opts;
}
function runCoverageNyc() {
  try {
    execSync("nyc report --reporter=json", { stdio: "pipe" });
    const f = path.join(process.cwd(), ".nyc_output", "coverage-final.json");
    if (!fs.existsSync(f)) return { actual: 0, branches: [] };
    const data = JSON.parse(fs.readFileSync(f, "utf-8"));
    let tot = 0, cov = 0;
    const b = [];
    Object.entries(data).forEach(([file, d]) => {
      if (!d.lines) return;
      const l = Object.values(d.lines);
      const c = l.filter(Boolean).length;
      tot += l.length;
      cov += c;
      const pct = Math.round((c / l.length) * 100);
      b.push({ name: path.basename(file), coverage: pct, status: pct >= 80 ? "ok" : pct >= 50 ? "warn" : "fail" });
    });
    const actual = tot > 0 ? Math.round((cov / tot) * 100) : 0;
    return { actual, branches: b.sort((a, x) => a.coverage - x.coverage) };
  } catch (e) {
    return { actual: 0, branches: [] };
  }
}
function runCoverageJest() {
  try {
    execSync("jest --coverage --coverageReporters=json", { stdio: "pipe" });
    const f = path.join(process.cwd(), "coverage/coverage-final.json");
    if (!fs.existsSync(f)) return { actual: 0, branches: [] };
    const data = JSON.parse(fs.readFileSync(f, "utf-8"));
    const b = [];
    let tot = 0;
    Object.entries(data).forEach(([file, d]) => {
      const p = d.lines?.pct || 0;
      b.push({ name: path.basename(file), coverage: Math.round(p), status: p >= 80 ? "ok" : p >= 50 ? "warn" : "fail" });
      tot += p;
    });
    const actual = b.length > 0 ? Math.round(tot / b.length) : 0;
    return { actual, branches: b.sort((a, x) => a.coverage - x.coverage) };
  } catch (e) {
    return { actual: 0, branches: [] };
  }
}
async function main() {
  const o = parseArgs();
  const c = o.tool === "jest" ? runCoverageJest() : runCoverageNyc();
  const g = o.target - c.actual;
  const r = { actual: c.actual, target: o.target, gap: g, status: g <= 0 ? "pass" : "fail", branches: c.branches, ts: new Date().toISOString() };
  if (o.output === "json") console.log(JSON.stringify(r, null, 2));
  else {
    console.log(`Coverage: ${c.actual}% (target: ${o.target}%, gap: ${g > 0 ? "+" + g : g}%) [${r.status.toUpperCase()}]`);
    c.branches?.forEach(b => console.log(`  [${b.status.toUpperCase()}] ${b.name}: ${b.coverage}%`));
  }
  process.exit(g > 0 ? 1 : 0);
}
main().catch(e => { console.error("Error:", e.message); process.exit(1); });
