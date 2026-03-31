---
title:
date: 2022-10-24
type: landing

sections:
  - block: resume-biography
    content:
      username: admin
      text:
    design:
      css_class: dark
      background:
        color: black
        image:
          filename: fotox.jpg
          filters:
            brightness: 0.4
          size: cover
          position: center
          parallax: false

  - block: collection
    content:
      title: Publikasi Terbaru
      text: ''
      page_type: publication
      count: 5
      filters:
        author: ""
        category: ""
        tag: ""
        exclude_featured: false
        exclude_future: false
        exclude_past: false
        publication_type: ""
      offset: 0
      order: desc
    design:
      view: citation
      spacing:
        padding: [0, 0, 0, 0]

  - block: collection
    content:
      title: Presentasi Terakhir
      text: ''
      page_type: event
      count: 3
      filters:
        author: ""
        category: ""
        tag: ""
        exclude_featured: false
        exclude_future: false
        exclude_past: false
      offset: 0
      order: desc
    design:
      view: date-title-summary
      spacing:
        padding: [0, 0, 0, 0]

  - block: markdown
    content:
      title: Curriculum Vitae
      subtitle: ''
      text: |-
        - Lihat CV saya dalam [format html](/files/CV.html).
        - Unduh CV saya dalam [format pdf](/files/CV.pdf).
        - Jika diperlukan, unduh foto saya dalam [format jpg](/files/foto_krisna.jpg).
    design:
      columns: '1'

  - block: collection
    content:
      title: Tulisan Blog Terbaru
      subtitle: ''
      text: ''
      page_type: post
      count: 3
      filters:
        author: ""
        category: ""
        tag: ""
        exclude_featured: false
        exclude_future: false
        exclude_past: false
      offset: 0
      order: desc
    design:
      view: card
      spacing:
        padding: [0, 0, 0, 0]

  - block: markdown
    content:
      title: My music
      subtitle: ''
      text: |-
        <iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/3PAMt81vvT7HVX9tfizCuo?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
    design:
      columns: '1'

  - block: collection
    content:
      title: Hobi
      text: ''
      page_type: hobby
      count: 3
      filters:
        author: ""
        category: ""
        tag: ""
        exclude_featured: false
        exclude_future: false
        exclude_past: false
      offset: 0
      order: desc
    design:
      view: date-title-summary
      spacing:
        padding: [0, 0, 0, 0]
---
