package require Tk 8.6

if {[tk windowingsystem] == "win32"} {
  set static ""
} else {
  set static " static"
}

font create SunValleyCaptionFont -family "Segoe UI Variable$static Small" -size -12
font create SunValleyBodyFont -family "Segoe UI Variable$static Text" -size -14
font create SunValleyBodyStrongFont -family "Segoe UI Variable$static Text Semibold" -size -14
font create SunValleyBodyLargeFont -family "Segoe UI Variable$static Text" -size -18
font create SunValleySubtitleFont -family "Segoe UI Variable$static Display Semibold" -size -20
font create SunValleyTitleFont -family "Segoe UI Variable$static Display Semibold" -size -28
font create SunValleyTitleLargeFont -family "Segoe UI Variable$static Display Semibold" -size -40
font create SunValleyDisplayFont -family "Segoe UI Variable$static Display Semibold" -size -68

proc config_input_font {w} {
  if {[ttk::style theme use] in [list "sun-valley-dark" "sun-valley-light"]} {
    $w configure -font SunValleyBodyFont
  }
}

bind TEntry <<ThemeChanged>> {config_input_font %W}
bind TCombobox <<ThemeChanged>> {config_input_font %W}
bind TSpinbox <<ThemeChanged>> {config_input_font %W}


source [file join [file dirname [info script]] theme light.tcl]
source [file join [file dirname [info script]] theme dark.tcl]


proc set_theme {mode} {
  if {$mode == "dark"} {
    ttk::style theme use "sun-valley-dark"
    
    ttk::style configure . \
      -background $ttk::theme::sv_dark::theme_colors(-bg) \
      -foreground $ttk::theme::sv_dark::theme_colors(-fg) \
      -troughcolor $ttk::theme::sv_dark::theme_colors(-bg) \
      -focuscolor $ttk::theme::sv_dark::theme_colors(-selbg) \
      -selectbackground $ttk::theme::sv_dark::theme_colors(-selbg) \
      -selectforeground $ttk::theme::sv_dark::theme_colors(-selfg) \
      -insertwidth 1 \
      -insertcolor $ttk::theme::sv_dark::theme_colors(-fg) \
      -fieldbackground $ttk::theme::sv_dark::theme_colors(-bg) \
      -font SunValleyBodyFont \
      -borderwidth 0 \
      -relief flat

    tk_setPalette \
      background $ttk::theme::sv_dark::theme_colors(-bg) \
      foreground $ttk::theme::sv_dark::theme_colors(-fg) \
      highlightColor $ttk::theme::sv_dark::theme_colors(-selbg) \
      selectBackground $ttk::theme::sv_dark::theme_colors(-selbg) \
      selectForeground $ttk::theme::sv_dark::theme_colors(-selfg) \
      activeBackground $ttk::theme::sv_dark::theme_colors(-selbg) \
      activeForeground $ttk::theme::sv_dark::theme_colors(-selfg)
    
    ttk::style map . -foreground [list disabled $ttk::theme::sv_dark::theme_colors(-disfg)]

    option add *tearOff 0
    option add *Menu.selectColor $ttk::theme::sv_dark::theme_colors(-fg)
  
  } elseif {$mode == "light"} {
    ttk::style theme use "sun-valley-light"
    
    ttk::style configure . \
      -background $ttk::theme::sv_light::theme_colors(-bg) \
      -foreground $ttk::theme::sv_light::theme_colors(-fg) \
      -troughcolor $ttk::theme::sv_light::theme_colors(-bg) \
      -focuscolor $ttk::theme::sv_light::theme_colors(-selbg) \
      -selectbackground $ttk::theme::sv_light::theme_colors(-selbg) \
      -selectforeground $ttk::theme::sv_light::theme_colors(-selfg) \
      -insertwidth 1 \
      -insertcolor $ttk::theme::sv_light::theme_colors(-fg) \
      -fieldbackground $ttk::theme::sv_light::theme_colors(-bg) \
      -font SunValleyBodyFont \
      -borderwidth 0 \
      -relief flat

    tk_setPalette \
      background $ttk::theme::sv_light::theme_colors(-bg) \
      foreground $ttk::theme::sv_light::theme_colors(-fg) \
      highlightColor $ttk::theme::sv_light::theme_colors(-selbg) \
      selectBackground $ttk::theme::sv_light::theme_colors(-selbg) \
      selectForeground $ttk::theme::sv_light::theme_colors(-selfg) \
      activeBackground $ttk::theme::sv_light::theme_colors(-selbg) \
      activeForeground $ttk::theme::sv_light::theme_colors(-selfg)
    
    ttk::style map . -foreground [list disabled $ttk::theme::sv_light::theme_colors(-disfg)]

    option add *tearOff 0
    option add *Menu.selectColor $ttk::theme::sv_light::theme_colors(-fg)
  }
}
