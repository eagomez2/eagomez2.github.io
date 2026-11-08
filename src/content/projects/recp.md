---
title: "recp"
heading: "recp"
subtitle: "Command-line pipelines defined in YAML"
category: "software"
date: "2026-10-02"
order: 2
cover: "/images/projects/recp/cover.jpg"
---

<div class="cols">
<div class="col col-1-4">
<figure><img src="/images/projects/recp/cover.jpg" alt="recp logo: a chef's hat with a terminal prompt inside a dark circle" width="900" height="900" loading="lazy"></figure>
</div>
<div class="col col-3-4">
<p><code>recp</code> (short for recipe) runs recipes: <code>.yaml</code> files that group shell commands into steps. Commands can be generated from templates, take values from environment variables or prompts, run in parallel and skip outputs that already exist, which is useful when processing large datasets.</p>
<ul>
<li><strong>Steps</strong>: each step has its own commands, environment variables and working folder. Steps can be selected with <code>--tag</code> or <code>--step</code>, and a failed run can be resumed with <code>--from</code>.</li>
<li><strong>Modifiers</strong>: expand one command into many before the recipe runs, e.g. one command per file with <code>dir_files</code> or per combination of values with <code>cartesian_product</code>.</li>
<li><strong>Constructors</strong>: such as <code>!input</code>, <code>!prompt</code> and <code>!shell</code> set variables when the recipe is loaded, so the same recipe can be used with different data or settings.</li>
<li><strong>Parallel commands</strong>: steps with a <code>parallel</code> key run several commands at a time, with their status shown in a live table.</li>
</ul>
<p>The <code>--dry-run</code> option prints the commands without running them.</p>
</div>
</div>

<h3>Links</h3>
<ul>
<li><a href="https://github.com/eagomez2/recp" rel="noopener" target="_blank">Official online repository</a>.</li>
<li><a href="https://eagomez2.github.io/recp/" rel="noopener" target="_blank">Documentation</a>.</li>
</ul>
