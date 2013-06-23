# Shamelessly ripped and modified from
# https://github.com/SublimeText/TrailingSpaces

import sublime
import sublime_plugin

DEFAULT_MAX_FILE_SIZE = 1048576
DEFAULT_COLOR_SCOPE_NAME = "invalid"
DEFAULT_IS_ENABLED = True

# Set whether the plugin is on or off.
hmw_settings = sublime.load_settings('highlight_mixed_whitespace.sublime-settings')
hmw_enabled = bool(hmw_settings.get('hmw_enabled', DEFAULT_IS_ENABLED))


# Determine if the view is a find results view.
def is_find_results(view):
    return view.settings().get('syntax') and \
        "Find Results" in view.settings().get('syntax')


# Return an array of regions matching mixed whitespace.
def find_mixed_whitespace(view):
    return view.find_all('(\t+ +)|( +\t+)')


# Highlight mixed whitspace.
def highlight_mixed_whitespace(view):
    max_size = hmw_settings.get('highlight_mixed_whitespace_max_file_size',
                                DEFAULT_MAX_FILE_SIZE)
    color_scope_name = hmw_settings.get('highlight_mixed_whitespace_scope_name',
                                        DEFAULT_COLOR_SCOPE_NAME)
    if view.size() <= max_size and not is_find_results(view):
        regions = find_mixed_whitespace(view)
        view.add_regions('MixedWhitespaceHighlightListener', regions,
                         color_scope_name, "", sublime.DRAW_EMPTY)


# Highlight matching regions.
class MixedWhitespaceHighlightListener(sublime_plugin.EventListener):
    def __init__(self):
        self.pending = 0

    def on_modified(self, view):
        if hmw_enabled:
            self.pending = self.pending + 1
            sublime.set_timeout(lambda: self.parse(view), 1000)

    def parse(self, view):
        self.pending = self.pending - 1
        if self.pending > 0:
            return
        highlight_mixed_whitespace(view)

    def on_activated(self, view):
        if hmw_enabled:
            highlight_mixed_whitespace(view)

    def on_load(self, view):
        if hmw_enabled:
            highlight_mixed_whitespace(view)
