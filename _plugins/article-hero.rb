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

# Chirpy's related-post cards (the "相關文章" block under a post) link to other
# articles; give each card that article's banner above its text.
Jekyll::Hooks.register [:pages, :documents], :post_render do |page|
  next unless page.output_ext == ".html" && page.output.include?('id="related-posts"')

  lang = page.data["lang"] == "en" ? "en" : "zh-TW"
  base = page.site.baseurl
  page.output.gsub!(%r{(<a href="([^"]+)" class="post-preview card[^"]*">)(\s*<div class="card-body">)}) do
    open_tag, href, body = Regexp.last_match(1), Regexp.last_match(2), Regexp.last_match(3)
    item = (page.site.data["writing"] || []).find do |entry|
      %w[zh-TW en].any? { |key| entry[key] && "#{base}#{entry[key]['url']}" == href }
    end
    next "#{open_tag}#{body}" unless item && item["image"]

    image = item["image"]
    img = %(<img class="card-img-top related-hero" src="#{base}#{image['path']}" width="#{image['width']}" ) +
          %(height="#{image['height']}" alt="#{CGI.escapeHTML(item[lang]['image_alt'].to_s)}" loading="lazy" decoding="async">)
    "#{open_tag}#{img}#{body}"
  end
end
