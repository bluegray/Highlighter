# Shamelessly ripped and modified from
# https://github.com/SublimeText/TrailingSpaces

import sublime, sublime_plugin

DEFAULT_MAX_FILE_SIZE = 1048576
DEFAULT_COLOR_SCOPE_NAME = "invalid"
DEFAULT_IS_ENABLED = True

# Set whether the plugin is on or off.
# Reuseing TrailingSpaces' config.
ts_settings = sublime.load_settings('trailing_spaces.sublime-settings')
trailing_spaces_enabled = bool(ts_settings.get('trailing_spaces_enabled',
	DEFAULT_IS_ENABLED))

# Determine if the view is a find results view.
def is_find_results(view):
	return view.settings().get('syntax') and \
		"Find Results" in view.settings().get('syntax')

# Return an array of regions matching mixed whitspace.
def find_mixed_whitspace(view):
	return view.find_all('(\t+ +)|( +\t+)')

# Highlight mixed whitspace.
def highlight_mixed_whitspace(view):
	max_size = ts_settings.get('trailing_spaces_file_max_size',
		DEFAULT_MAX_FILE_SIZE)
	color_scope_name = ts_settings.get('trailing_spaces_highlight_color',
		DEFAULT_COLOR_SCOPE_NAME)
	if view.size() <= max_size and not is_find_results(view):
		regions = find_mixed_whitspace(view)
		view.add_regions('MixedWhitespaceHighlightListener', regions,
			color_scope_name, "", sublime.DRAW_EMPTY)

# Highlight matching regions.
class MixedWhitespaceHighlightListener(sublime_plugin.EventListener):
	def on_modified(self, view):
		if trailing_spaces_enabled:
			highlight_mixed_whitspace(view)

	def on_activated(self, view):
		if trailing_spaces_enabled:
			highlight_mixed_whitspace(view)

	def on_load(self, view):
		if trailing_spaces_enabled:
			highlight_mixed_whitspace(view)
