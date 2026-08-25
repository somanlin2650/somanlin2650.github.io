#!/usr/bin/env ruby
#
# Check for changed posts, including translated article pages.

module PostsLastmodHook
  def self.apply(document)
    commit_num = `git rev-list --count HEAD "#{document.path}"`

    return unless commit_num.to_i > 1

    lastmod_date = `git log -1 --pretty="%ad" --date=iso "#{document.path}"`
    document.data['last_modified_at'] = lastmod_date
  end
end

Jekyll::Hooks.register :posts, :post_init do |post|
  PostsLastmodHook.apply(post)
end

Jekyll::Hooks.register :pages, :post_init do |page|
  PostsLastmodHook.apply(page) if page.data['layout'] == 'post'
end
