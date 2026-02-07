class_name UITheme
extends RefCounted

## Central UI theme for gothic/elegant 1920s styling.
## Provides fonts, colors, ornaments, and button styling.


# ── Fonts ──────────────────────────────────────────────────────────────

static func font_title() -> SystemFont:
	var f := SystemFont.new()
	f.font_names = PackedStringArray(["Palatino Linotype", "Book Antiqua", "Georgia", "Times New Roman"])
	return f


static func font_body() -> SystemFont:
	var f := SystemFont.new()
	f.font_names = PackedStringArray(["Georgia", "Palatino Linotype", "Book Antiqua", "Times New Roman"])
	return f


static func font_ui() -> SystemFont:
	var f := SystemFont.new()
	f.font_names = PackedStringArray(["Segoe UI", "Calibri", "Arial"])
	return f


# ── Colors ─────────────────────────────────────────────────────────────

const GOLD := Color(0.85, 0.72, 0.45)
const GOLD_LIGHT := Color(1.0, 0.92, 0.75)
const GOLD_DIM := Color(0.6, 0.52, 0.35)
const TEXT_LIGHT := Color(0.85, 0.8, 0.72)
const TEXT_DIM := Color(0.5, 0.45, 0.4)
const BG_DARK := Color(0.04, 0.04, 0.06, 0.88)
const BG_PANEL := Color(0.06, 0.06, 0.09, 0.92)
const BORDER := Color(0.45, 0.38, 0.25, 0.6)
const BORDER_HOVER := Color(0.7, 0.58, 0.35, 0.85)


# ── Ornaments ──────────────────────────────────────────────────────────

const ORNAMENT_WIDE := "════  ◆  ════"
const ORNAMENT_NARROW := "~  ◆  ~"
const ORNAMENT_LINE := "━━━  ◆  ━━━"


static func create_ornament_label(ornament: String = ORNAMENT_WIDE, size: int = 18) -> Label:
	var lbl := Label.new()
	lbl.text = ornament
	lbl.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	lbl.add_theme_font_size_override("font_size", size)
	lbl.add_theme_color_override("font_color", GOLD_DIM)
	lbl.add_theme_font_override("font", font_body())
	return lbl


# ── Button Styling ─────────────────────────────────────────────────────

static func style_button(btn: Button, font_size: int = 22) -> void:
	var style := StyleBoxFlat.new()
	style.bg_color = Color(0.07, 0.07, 0.1, 0.75)
	style.border_color = BORDER
	style.set_border_width_all(1)
	style.set_corner_radius_all(2)
	style.content_margin_left = 16
	style.content_margin_right = 16
	style.content_margin_top = 10
	style.content_margin_bottom = 10
	btn.add_theme_stylebox_override("normal", style)

	var hover := style.duplicate()
	hover.bg_color = Color(0.14, 0.11, 0.08, 0.92)
	hover.border_color = BORDER_HOVER
	btn.add_theme_stylebox_override("hover", hover)

	var pressed := style.duplicate()
	pressed.bg_color = Color(0.04, 0.04, 0.06, 0.95)
	pressed.border_color = GOLD
	btn.add_theme_stylebox_override("pressed", pressed)

	var focus := style.duplicate()
	focus.border_color = GOLD_DIM
	btn.add_theme_stylebox_override("focus", focus)

	btn.add_theme_font_size_override("font_size", font_size)
	btn.add_theme_font_override("font", font_ui())
	btn.add_theme_color_override("font_color", TEXT_LIGHT)
	btn.add_theme_color_override("font_hover_color", GOLD_LIGHT)
	btn.add_theme_color_override("font_pressed_color", GOLD)


static func style_menu_button(btn: Button, font_size: int = 26) -> void:
	## Larger styled button for main menu / title screen.
	var style := StyleBoxFlat.new()
	style.bg_color = Color(0.06, 0.06, 0.09, 0.7)
	style.border_color = BORDER
	style.border_width_bottom = 1
	style.border_width_top = 1
	style.border_width_left = 1
	style.border_width_right = 1
	style.set_corner_radius_all(3)
	style.content_margin_top = 12
	style.content_margin_bottom = 12
	style.content_margin_left = 24
	style.content_margin_right = 24
	btn.add_theme_stylebox_override("normal", style)

	var hover := style.duplicate()
	hover.bg_color = Color(0.12, 0.1, 0.07, 0.9)
	hover.border_color = GOLD
	btn.add_theme_stylebox_override("hover", hover)

	var pressed := style.duplicate()
	pressed.bg_color = Color(0.04, 0.04, 0.06, 0.95)
	pressed.border_color = GOLD_LIGHT
	btn.add_theme_stylebox_override("pressed", pressed)

	var focus := style.duplicate()
	focus.border_color = GOLD_DIM
	btn.add_theme_stylebox_override("focus", focus)

	btn.add_theme_font_size_override("font_size", font_size)
	btn.add_theme_font_override("font", font_title())
	btn.add_theme_color_override("font_color", TEXT_LIGHT)
	btn.add_theme_color_override("font_hover_color", GOLD_LIGHT)
	btn.add_theme_color_override("font_pressed_color", GOLD)


static func style_quick_button(btn: Button) -> void:
	## Small button for in-game quick menu.
	var style := StyleBoxFlat.new()
	style.bg_color = Color(0.08, 0.08, 0.1, 0.5)
	style.border_color = Color(BORDER.r, BORDER.g, BORDER.b, 0.3)
	style.set_border_width_all(1)
	style.set_corner_radius_all(2)
	style.content_margin_left = 12
	style.content_margin_right = 12
	style.content_margin_top = 8
	style.content_margin_bottom = 8
	btn.add_theme_stylebox_override("normal", style)

	var hover := style.duplicate()
	hover.bg_color = Color(0.14, 0.11, 0.08, 0.8)
	hover.border_color = GOLD_DIM
	btn.add_theme_stylebox_override("hover", hover)

	var pressed := style.duplicate()
	pressed.bg_color = Color(0.04, 0.04, 0.06, 0.8)
	btn.add_theme_stylebox_override("pressed", pressed)

	var focus := style.duplicate()
	btn.add_theme_stylebox_override("focus", focus)

	btn.add_theme_font_size_override("font_size", 16)
	btn.add_theme_font_override("font", font_ui())
	btn.add_theme_color_override("font_color", TEXT_DIM)
	btn.add_theme_color_override("font_hover_color", GOLD_LIGHT)
