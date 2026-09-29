# frozen_string_literal: true

Jekyll::Hooks.register :site, :post_read do |site|
  tabs = site.data.dig("locales", "en", "tabs")
  tabs["writing"] = "Writing" if tabs
  tabs["books"] = "Books" if tabs
  tabs["books-en"] = "Books" if tabs
end

# Chirpy reads the global tagline even on translated pages. Localize the
# rendered subtitle at build time so it also works without JavaScript.
Jekyll::Hooks.register [:pages, :documents], :post_render do |page|
  next unless page.data["lang"] == "en"

  page.output.sub!(%r{(<p\b[^>]*class="[^"]*\bsite-subtitle\b[^"]*"[^>]*>).*?(</p>)}m) do
    "#{$1}AI · Philosophy · Learning#{$2}"
  end
end

# Render ordinary links as well as hreflang metadata so both translations can
# be discovered without JavaScript. Do not put page-specific links in Chirpy's
# cached footer, which is shared by all pages of a language.
Jekyll::Hooks.register [:pages, :documents], :post_render do |page|
  alternate = page.data["alternate_url"]
  next unless alternate && page.output.include?("<main ")

  english = page.data["lang"] == "en"
  label = english ? "繁體中文" : "English"
  language = english ? "zh-Hant" : "en"
  href = "#{page.site.baseurl}#{alternate}"
  link = %(<nav class="translation-link" aria-label="#{english ? 'Translation' : '其他語言'}"><a href="#{href}" hreflang="#{language}" lang="#{language}">#{label}</a></nav>)
  page.output.sub!(%r{(<main\b[^>]*>)}, "\\1#{link}")
end

Jekyll::Hooks.register :pages, :post_render do |page|
  next unless page.data["layout"] == "post" && page.data["lang"] == "en"

  page.output.gsub!(%r{href="/categories/([^"/]+)/"}, 'href="/en/categories/#\1"')
  page.output.gsub!(%r{href="/tags/([^"/]+)/"}, 'href="/en/tags/#\1"')
end
