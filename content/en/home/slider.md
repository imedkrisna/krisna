+++
# Slider widget.
widget = "slider"  # See https://sourcethemes.com/academic/docs/page-builder/
headless = true  # This file represents a page section.
active = true  # Activate this widget? true/false
weight = 1  # Order that this section will appear.

# Slide interval.
# Use `false` to disable animation or enter a time in ms, e.g. `5000` (5s).
interval = 8000

# Slide height (optional).
# E.g. `500px` for 500 pixels or `calc(100vh - 70px)` for full screen.
height = "300px"

# Slides.
# Duplicate an `[[item]]` block to add more slides.
[[item]]
  title = "Welcome!"
  content = "This is Krisna Gupta! Use the top right menu to set the theme (light/dark) and language (en/id). Untuk Bahasa Indonesia, ketuk ini"
  align = "center"

  cta_label = "Bahasa Indonesia"
  cta_url = "https://krisna.netlify.app/id"
  cta_icon_pack = "far"
  cta_icon = "window-maximize"

  overlay_color = "#888"  # An HTML color value.
  overlay_img = "headers/bubbles-wide.jpg"  # Image path relative to your `static/media/` folder.
  overlay_filter = 0.5  # Darken the image. Value in range 0-1.

[[item]]
  title = "Welcome!"
  content = "I use this page to store my CV and blogs. I blog mostly in Indonesian, sometimes english."
  align = "center"  # Choose `center`, `left`, or `right`.

  # Overlay a color or image (optional).
  #   Deactivate an option by commenting out the line, prefixing it with `#`.
  overlay_color = "#666"  # An HTML color value.
  overlay_img = "headers/bubbles-wide.jpg"  # Image path relative to your `static/media/` folder.
  overlay_filter = 0.5  # Darken the image. Value in range 0-1.

  # Call to action button (optional).
  #   Activate the button by specifying a URL and button label below.
  #   Deactivate by commenting out parameters, prefixing lines with `#`.
  cta_label = "Posts"
  cta_url = "https://krisna.netlify.app/post"
  cta_icon_pack = "fas"
  cta_icon = "blog"

# [[item]]
#   title = "courses"
#   content = "this page hosts my courses as well (in Indonesian)"
#   align = "center"

#   overlay_color = "#333"  # An HTML color value.
#   overlay_img = ""  # Image path relative to your `static/media/` folder.
#   overlay_filter = 0.5  # Darken the image. Value in range 0-1.

[[item]]
  title = "Hobbies"
  content = "I also store hobby in this page. Be prepared to hear some crappy voice 🤣🤣"
  align = "center"

  overlay_color = "#555"  # An HTML color value.
  overlay_img = "sing.jpg"  # Image path relative to your `static/media/` folder.
  overlay_filter = 0.5  # Darken the image. Value in range 0-1.

  cta_label = "Hobby"
  cta_url = "https://krisna.netlify.app/hobby"
  cta_icon_pack = "fas"
  cta_icon = "music"



+++