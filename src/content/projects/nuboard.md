---
title: "NuBoard"
heading: "NuBoard"
subtitle: "Local experiment tracker for ML"
category: "software"
date: "2026-10-14"
order: 1
tags: ["Open source", "Python", "Machine learning", "Experiment tracking"]
cover: "/images/projects/nuboard/cover.jpg"
---

<div class="cols">
<div class="col col-1-4">
<figure><img src="/images/projects/nuboard/cover.jpg" alt="NuBoard logo: a red arch on a cream rounded square" width="900" height="900" loading="lazy"></figure>
</div>
<div class="col col-3-4">
<p><code>nuboard</code> is a fast, local, folder-based experiment tracker and viewer for machine learning training. It logs your training runs with three Python calls, keeps every run as a plain folder on disk, and opens thousands of them in a fast viewer that runs on your own machine. There is no account to create, no server to keep running and no database to back up.</p>
<p>With <code>nuboard</code> you can:</p>
<ul>
<li>Log with three calls (<code>init</code>, <code>add_scalar</code>, <code>finish</code>). Config, git commit and diff, installed packages, GPUs, command line and rank are recorded for you.</li>
<li>Keep one folder per run that you can copy, rsync, zip or delete, with stars, notes and tags stored next to the data.</li>
<li>Group a sweep into mean ± std bands over seeds, smooth, zoom and follow runs live while they train.</li>
<li>Log a range, not just a number, and see where the time goes with per-step timers.</li>
<li>Inspect audio with its annotations: overlay a voice activity probability and label tracks on the waveform.</li>
<li>Catch NaN and Inf values, loss and gradient spikes and throughput drops with health alerts.</li>
<li>Track versioned datasets and checkpoints with a lineage graph.</li>
</ul>
</div>
</div>

<figure><img src="/images/projects/nuboard/image-1.jpg" alt="NuBoard Charts page: a learning-rate sweep grouped by lr, with mean ± std bands over three seeds and health alerts below" width="1400" height="1101" loading="lazy"></figure>

<figure><img src="/images/projects/nuboard/image-2.jpg" alt="NuBoard waveform figure: a denoised speech clip with its speech probability on top and target, predicted and event tracks below" width="1400" height="1101" loading="lazy"></figure>

<h3>Links</h3>
<ul>
<li><a href="https://github.com/eagomez2/nuboard" rel="noopener" target="_blank">Official online repository</a>.</li>
<li><a href="https://eagomez2.github.io/nuboard/" rel="noopener" target="_blank">Documentation</a>.</li>
<li><a href="https://medium.com/@eagomez2/tracking-machine-learning-experiments-with-nuboard-cebb0daf9088" rel="noopener" target="_blank">Medium article: Tracking machine learning experiments with NuBoard.</a></li>
</ul>
