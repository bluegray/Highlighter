#Highlighter

A plugin for [Sublime Text](http://www.sublimetext.com) (ST2 and ST3) to highlight mixed
tabs and spaces, some unicode characters and trailing space.

![Highlighter Screenshot](https://github.com/bluegray/Highlight-Mixed-Whitespace/raw/master/images/mixed-whitespace.png "Highlighter Screenshot")

## Additional highlighted characters

These characters are highlighted by default:  

- **U+2026** Horizontal ellipsis
- **U+2018** Left single quotation mark
- **U+2019** Right single quotation mark
- **U+201c** Left double quotation mark
- **U+201d** Right double quotation mark
- **U+2013** En dash
- **U+2014** Em dash
- **U+00a0** Non-breaking space
- **U+3000** Ideographic spaces

## Key bindings

`Ctrl+Alt+Shift+h` : Toggle highlighting on/off.

## Menu commands
You can toggle highlighting in the `View` menu.
The setting is per view, and not saved to disk. This can be changed in the settings, see below.

## Configuration

You can override the default settings by creating a file in `Packages/User/highlighter.sublime-settings`:
Check the default highlighter.sublime-settings file for available settings.

### Syntax ignore

You can add a list of syntaxes to ignore with the following setting:
```javascript
{
  "highlighter_syntax_ignore": ["Python", "PHP"]
}
```

### Save toggled state

To persist the toggled state to disk, set the following to true:

```javascript
{
  "highlighter_save_settings_on_change": true
}
```

### Custom regex

You can customise the regex to highlight:

**highlighter_regex**      <- Matching characters highlighted with fill and outline  
**highlighter_regex_cool** <- Matching characters highlighted with stippled underline  

```javascript
{
  "highlighter_regex": "(\t+ +(?![*]))|( +\t+)|([\t ]+$)",
  "highlighter_regex_cool": "[\u2026\u2018\u2019\u201c\u201d\u2013\u2014\u00a0]"
}
```
