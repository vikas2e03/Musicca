# yaru.tcl, generated by ThemeGenerator
# License: GNU GPLv3
# Copyright (c) 2020 RedFantom

package require Tk 8.6
namespace eval ttk::theme::yaru {
	set dir [file dirname [info script]]
	set image_file [file join $dir "images.tcl"]
	
	source $image_file
	
	ttk::style theme create yaru -parent default -settings {
		ttk::style configure . \
			-foreground #5D5D5D \
			-background #FFFFFF \
			-selectforeground #ffffff \
			-selectbackground #E95420
	
		ttk::style layout TButton {
			Button.button -children {
			    Button.focus -children {
			        Button.padding -children {
			            Button.label -side left -expand true
			        }
			    }
			}
		}
		ttk::style element create Button.button image [list $images(button) \
				{active selected} $images(button-active-selected) \
				active $images(button-active) \
				pressed $images(button-pressed) \
				disabled $images(button-disabled) \
			] -border {4 4 4 4}
	
	
		ttk::style element create Checkbutton.indicator image [list $images(checkbutton) \
				{active selected} $images(checkbutton-active-selected) \
				{pressed selected} $images(checkbutton-pressed-selected) \
				{hover selected} $images(checkbutton-hover-selected) \
				{disabled selected} $images(checkbutton-disabled-selected) \
				active $images(checkbutton-active) \
				pressed $images(checkbutton-pressed) \
				hover $images(checkbutton-hover) \
				disabled $images(checkbutton-disabled) \
				selected $images(checkbutton-selected) \
			] -width 22 -sticky w
	
	
		ttk::style element create Radiobutton.indicator image [list $images(radiobutton) \
				{active selected} $images(radiobutton-active-selected) \
				{pressed selected} $images(radiobutton-pressed-selected) \
				{hover selected} $images(radiobutton-hover-selected) \
				{disabled selected} $images(radiobutton-disabled-selected) \
				active $images(radiobutton-active) \
				pressed $images(radiobutton-pressed) \
				hover $images(radiobutton-hover) \
				disabled $images(radiobutton-disabled) \
				selected $images(radiobutton-selected) \
			]
	
	
		ttk::style element create Arrow image [list $images(arrow) \
				active $images(arrow-active) \
				disabled $images(arrow-disabled) \
				pressed $images(arrow-pressed) \
			]
		}
	ttk::style configure TRadiobutton -padding 3
	ttk::style configure TCheckbutton -padding 3
	ttk::style map TRadiobutton -background [list active #ffffff]
	}
package provide yaru 1.0
