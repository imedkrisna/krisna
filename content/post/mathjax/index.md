---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Adding equation numbering on my hugo academic theme blog."
subtitle: ""
summary: ""
authors: []
tags: [blog]
categories: [blog]
date: 2020-08-21T11:01:29+10:00
lastmod: 2020-08-21T11:01:29+10:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

I just recently migrated my blog from Jekyll powered website to hugo powered one using academic theme. The migration went quite smoothly especially since I really have little content when I moved away from Jekyll. Everything works great in the hugo academic, but one.

I didn't understand at first why Hugo Academic Theme does not render equation labelling correctly. It worked on my Jekyll blog. I was trying to look for easy solution everywhere with no luck (sorry I am lazy and not a programmer).

But then I remembered that my Jekyll blog also did not load \\(\latex\\) correctly first time either. I followed an approach conducted by [CSega](http://csega.github.io/mypost/2017/03/28/how-to-set-up-mathjax-on-jekyll-and-github-properly.html) to solve this easily and it worked. Perhaps I can also use this approach for my Hugo blog. Be warned though that I am not 100% understand why this approach worked.

I copied a code snippet from CSega on the head.html file.

```html
       <head>
       ...
       <script type="text/x-mathjax-config"> MathJax.Hub.Config({ TeX: { equationNumbers: { autoNumber: "all" } } }); </script>
       <script type="text/x-mathjax-config">
         MathJax.Hub.Config({
           tex2jax: {
             inlineMath: [ ['$','$'], ["\\(","\\)"] ],
             processEscapes: true
           }
         });
       </script>
       <script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
       </head>
```

I just needed to locate where this snippet should be put to. In other words, I needed to locate my 'head.html' in my new hugo website. Fortunately Hugo Academic Theme have great documentation about this. All I needed to do was making a new file named 'layouts\partials\custom_head.html' on my folder and pasting the snippet there. So that file should be consists only for the snippet from CSega. It is important to note that this snippet must not be pasted on 'theme/academic/layours'. I tried to keep files in the theme folder untouched.

I hope this post is useful for you when you want to add equation numbering / labeling in your blog. If you do have comments or clarifications on what this code means in general will be great! 