---
title: "h5pack"
heading: "h5pack"
subtitle: "Pack and inspect HDF5 audio datasets"
category: "software"
date: "2026-10-02"
order: 1
tags: ["Open source", "Python", "HDF5", "Audio datasets"]
cover: "/images/projects/h5pack/cover.jpg"
---

<div class="cols">
<div class="col col-1-4">
<figure><img src="/images/projects/h5pack/cover.jpg" alt="h5pack logo: a waveform turning into stacked bars inside a dark circle" width="900" height="900" loading="lazy"></figure>
</div>
<div class="col col-3-4">
<p><code>h5pack</code> is a utility made to pack, analyze and unpack HDF5 audio datasets using data and annotations of various sources. It was made to go from raw files to HDF5 files and back in a robust, consistent and simple way.</p>
<p>It provides a collection of tools for all the necessary tasks:</p>
<ul>
<li><code>h5pack init</code>: creates a configuration file from an annotations <code>.csv</code> file.</li>
<li><code>h5pack pack</code>: converts raw data and/or annotation files into an HDF5 file.</li>
<li><code>h5pack unpack</code>: extracts raw data from an HDF5 file, allowing regeneration of the original input data.</li>
<li><code>h5pack virtual</code>: combines multiple datasets into a single virtual dataset without duplicating data.</li>
<li><code>h5pack info</code>: displays the contents of an HDF5 file generated with <code>h5pack</code>.</li>
<li><code>h5pack checksum</code>: verifies the integrity of an HDF5 file to detect potential corruption.</li>
<li><code>h5pack show</code>: shows, saves or plays the data of any row of an HDF5 file.</li>
</ul>
<p>Packed data can be read in Python with <code>h5pack.open()</code>, which also works with PyTorch <code>DataLoader</code> workers.</p>
</div>
</div>

<h3>Links</h3>
<ul>
<li><a href="https://github.com/eagomez2/h5pack" rel="noopener" target="_blank">Official online repository</a>.</li>
<li><a href="https://eagomez2.github.io/h5pack/" rel="noopener" target="_blank">Documentation</a>.</li>
</ul>
