---
title: Hello, World
description: First post on the new academic website.
---

Welcome to the blog. This is a sample post.

Here is inline math: $E=mc^2$ and a block:

$$
\int_0^1 x^2 \, dx = \frac{1}{3}
$$

```mermaid
graph TD
  A[Start] --> B{Is it working?}
  B -- Yes --> C[Ship it]
  B -- No --> D[Fix it]
  D --> B
```

<div id="plotly-sample" style="width:100%;max-width:560px;height:320px;"></div>
<script>
  if (window.Plotly) {
    const data = [{ x: [1,2,3], y: [1,4,9], mode: 'lines+markers' }];
    Plotly.newPlot('plotly-sample', data, { margin: { t: 20 } });
  }
  </script>


