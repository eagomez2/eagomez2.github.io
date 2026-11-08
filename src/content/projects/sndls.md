---
title: "sndls"
heading: "sndls"
subtitle: "Open-source audio-friendly ls tool"
category: "software"
date: "2025-04-21"
order: 1
tags: ["Open source", "Command line", "Audio"]
cover: "/images/projects/sndls/cover.jpg"
---

<div class="cols">
<div class="col col-1-4">
<figure><img src="/images/projects/sndls/image-1.jpg" alt="sndls illustration: magnifying glass over a cyan audio waveform" width="1024" height="576" loading="lazy"></figure>
</div>
<div class="col col-3-4">
<p><code>sndls</code> is a free open-source audio-friendly <code>ls-like</code> command line tool <em>with a little something extra</em>.</p>
<p>Besides inspecting relevant statistics of your audio data, with <code>sndls</code> you can:</p>
<ul>
<li>Save search results to a <code>.csv</code> file for later analysis.</li>
<li>Detect clipped, silent, or anomalous files that may impact machine learning pipelines.</li>
<li>Compute and verify SHA-256 hashes to detect file modifications or corruption.</li>
<li>Filter files using <code>python</code> expressions to identify those matching specific criteria.</li>
<li>Perform fast, metadata-based file inspection.</li>
<li>Execute post-processing actions, such as removing clipped files, copying files that meet certain conditions, and more.</li>
</ul>
<p><code>sndls</code> currently supports the following extensions: <code>.aif</code>, <code>.aiff</code>, <code>.mp3</code>, <code>.flac</code>, <code>.ogg</code>, <code>.wav</code>, <code>.wave</code>.</p>
</div>
</div>

<h3>Links</h3>
<ul>
<li><a href="https://github.com/eagomez2/sndls" rel="noopener" target="_blank">Official online repository</a>.</li>
<li><a href="https://github.com/eagomez2/sndls?tab=readme-ov-file#tutorial" rel="noopener" target="_blank">Basic tutorial</a>.</li>
<li><a href="https://medium.com/@eagomez2/inspecting-audio-file-collections-with-sndls-aace1c4242ed" rel="noopener" target="_blank">Medium article: Inspecting audio file collections with  <code>sndls</code>.</a></li>
</ul>
