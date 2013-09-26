# Shamelessly ripped and modified from
# https://github.com/SublimeText/TrailingSpaces

import sublime
import sublime_plugin

DEFAULT_MAX_FILE_SIZE = 1048576
DEFAULT_COLOR_SCOPE_NAME = "invalid"
DEFAULT_IS_ENABLED = True
DEFAULT_REGEX = '(\t+ +)|( +\t+)|[\u2026\u2018\u2019\u201c\u201d\u2013\u2014]|[\t ]+$'
DEFAULT_DELAY = 3000

def plugin_loaded():
    global Pref
    settings = sublime.load_settings('highlighter.sublime-settings')
    class Preferences:
        def load(self):
            Pref.enabled          = bool(settings.get('highlighter_enabled', DEFAULT_IS_ENABLED))
            Pref.regex            = settings.get('highlighter_regex', DEFAULT_REGEX)
            Pref.max_size         = settings.get('highlighter_max_file_size', DEFAULT_MAX_FILE_SIZE)
            Pref.color_scope_name = settings.get('highlighter_scope_name', DEFAULT_COLOR_SCOPE_NAME)
            Pref.delay            = settings.get('highlighter_delay', DEFAULT_DELAY)

    Pref = Preferences()
    Pref.load()

    settings.add_on_change('reload', lambda: Pref.load())

# Determine if the view is a find results view.
def is_find_results(view):
    return view.settings().get('syntax') and \
        "Find Results" in view.settings().get('syntax')


# Return an array of regions matching regex.
def find_regexes(view):
    return view.find_all(Pref.regex)


# Highlight regex matches.
def highlighter(view):
    if view.size() <= Pref.max_size and not is_find_results(view):
        regions = find_regexes(view)
        view.add_regions('HighlighterListener', regions,
                         Pref.color_scope_name, "", sublime.DRAW_EMPTY)


# Highlight matching regions.
class HighlighterListener(sublime_plugin.EventListener):
    def __init__(self):
        self.pending = 0

    def on_modified(self, view):
        if Pref.enabled:
            self.pending = self.pending + 1
            sublime.set_timeout(lambda: self.parse(view), Pref.delay)

    def parse(self, view):
        self.pending = self.pending - 1
        if self.pending > 0:
            return
        highlighter(view)

    def on_activated(self, view):
        if Pref.enabled:
            highlighter(view)

    def on_load(self, view):
        if Pref.enabled:
            highlighter(view)

# ST2 backwards compatibility
if int(sublime.version()) < 3000:
    plugin_loaded()
