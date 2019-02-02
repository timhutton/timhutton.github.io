---
layout: post
title: yes is not an allowed title
---

Well that was an interesting couple of hours. I was trying to update Jekyll on this blog and kept getting an odd error:

```
  Liquid Exception: no implicit conversion of true into String in /_layouts/post.html
jekyll 3.7.4 | Error:  no implicit conversion of true into String
```

I eventually tracked the error down to [this old post](https://timhutton.github.io/2007/09/07/10497.html) from 2007 which has code like this:

```
---
layout: post
title: yes
---

Words here.
```

Can you spot what the problem might be? The title of the post is a single word 'yes'. Somehow the title is getting evaluated as a boolean, which gives the value 'true' and then an error when it expects a string.

I have reported the bug to Jekyll: [https://github.com/jekyll/jekyll/issues/7514](https://github.com/jekyll/jekyll/issues/7514)