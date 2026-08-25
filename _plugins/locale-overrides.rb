# frozen_string_literal: true

Jekyll::Hooks.register :site, :post_read do |site|
  tabs = site.data.dig("locales", "en", "tabs")
  tabs["writing"] = "Writing" if tabs
end

Jekyll::Hooks.register :pages, :post_render do |page|
  next unless page.data["layout"] == "post" && page.data["lang"] == "en"

  page.output.gsub!(%r{href="/categories/([^"/]+)/"}, 'href="/en/categories/#\1"')
  page.output.gsub!(%r{href="/tags/([^"/]+)/"}, 'href="/en/tags/#\1"')
end
