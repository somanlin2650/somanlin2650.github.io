# frozen_string_literal: true

Jekyll::Hooks.register :site, :post_read do |site|
  tabs = site.data.dig("locales", "en", "tabs")
  tabs["writing"] = "Writing" if tabs
end
