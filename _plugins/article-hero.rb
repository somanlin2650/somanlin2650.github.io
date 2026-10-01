# frozen_string_literal: true

require "cgi"

# Put each article's banner at the top of the post, before the <header> that
# holds the h1. Chirpy only renders front matter `image` inside the metadata
# block, after the title, and crops it to 1.91:1, so the banner comes from
# _data/writing.yml instead (the same data the article list uses) and keeps
# its full panoramic proportions.
Jekyll::Hooks.register [:pages, :documents], :post_render do |page|
  next unless page.output_ext == ".html"

  entries = page.site.data["writing"] || []
  english = page.data["lang"] == "en"
  copy = nil
  item = entries.find do |entry|
    copy = entry[english ? "en" : "zh-TW"]
    copy && copy["url"] == page.url
  end
  next unless item && item["image"]

  image = item["image"]
  src = "#{page.site.baseurl}#{image['path']}"
  figure = %(<figure class="post-hero"><img src="#{src}" width="#{image['width']}" ) +
           %(height="#{image['height']}" alt="#{CGI.escapeHTML(copy['image_alt'].to_s)}" ) +
           %(fetchpriority="high" decoding="async"></figure>)
  page.output.sub!(%r{(<article\b[^>]*\bdata-toc=[^>]*>)}) { "#{Regexp.last_match(1)}#{figure}" }
end
