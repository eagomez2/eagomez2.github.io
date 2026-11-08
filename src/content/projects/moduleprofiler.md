---
title: "moduleprofiler"
heading: "moduleprofiler"
subtitle: "Open-source neural networks profiling package"
category: "software"
date: "2024-09-29"
order: 2
tags: ["Open source", "Python", "PyTorch"]
cover: "/images/projects/moduleprofiler/cover.jpg"
---

<div class="cols">
<div class="col col-1-4">
<figure><img src="/images/projects/moduleprofiler/image-1.jpg" alt="moduleprofiler illustration: glowing network of connected nodes" width="495" height="400" loading="lazy"></figure>
</div>
<div class="col col-3-4">
<p><code>moduleprofiler</code> is a free open-source package to profile <code>torch.nn.Module</code> modules and obtain useful information to design a model that fits your needs and constraints at development time.</p>
<p>With <code>moduleprofiler</code> you can:</p>
<ul>
<li>Calculate the number of parameters of your model.</li>
<li>Trace the input and output sizes of each component of your model.</li>
<li>Estimate the number of operations your model performs in a forward pass.</li>
<li>Calculate per module and total inference time.</li>
</ul>
<p>All results can be obtained in one of the following formats:</p>
<ul>
<li><code>dict</code> (default output format)</li>
<li><code>pandas.DataFrame</code> (to perform further calculations or filtering in your code)</li>
<li><code>html</code> (to export as webpage)</li>
<li><code>LaTeX</code> (to include in your publications)</li>
</ul>
</div>
</div>

<h3>Links</h3>
<ul>
<li><a href="https://eagomez2.github.io/moduleprofiler/" rel="noopener" target="_blank">Official online documentation</a>.</li>
<li><a href="https://github.com/eagomez2/moduleprofiler" rel="noopener" target="_blank">Official repository</a>.</li>
<li><a href="https://eagomez2.github.io/moduleprofiler/tutorial/" rel="noopener" target="_blank">Basic tutorial</a>.</li>
<li><a href="https://eagomez2.github.io/moduleprofiler/reference/" rel="noopener" target="_blank">Reference documentation</a>.</li>
<li><a href="https://medium.com/@eagomez2/profiling-neural-networks-with-moduleprofiler-in-python-c566fe2cf896" rel="noopener" target="_blank">Medium article: Profiling neural networks with <code>moduleprofiler</code> in python</a>.</li>
</ul>
