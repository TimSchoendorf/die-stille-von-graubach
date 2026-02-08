class_name UITheme
extends RefCounted

## Central UI theme for gothic/elegant 1920s styling.
## Provides fonts, colors, ornaments, and button styling.


# ── Scaling ───────────────────────────────────────────────────────────

static var _scale: float = 1.0
static var _is_mobile: bool = false


static func init_scaling() -> void:
	_is_mobile = OS.get_name() in ["Android", "iOS"]
	if _is_mobile:
		var dpi := DisplayServer.screen_get_dpi()
		var screen_px := DisplayServer.screen_get_size()
		if dpi > 0 and screen_px.x > 0:
			var diag_px := sqrt(float(screen_px.x) * screen_px.x + float(screen_px.y) * screen_px.y)
			var diag_inches := diag_px / float(dpi)
			# Smaller screens need more scaling; cap at 1.5 to fit viewport
			_scale = clampf(9.0 / diag_inches, 1.0, 1.5)
		else:
			_scale = 1.4
	else:
		_scale = 1.0


static func s(value: int) -> int:
	return int(value * _scale)


static func sf(value: float) -> float:
	return value * _scale


static func is_mobile() -> bool:
	return _is_mobile


static func margin_h() -> int:
	return s(60) if _is_mobile else 300


static func margin_v() -> int:
	return s(40) if _is_mobile else 80


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
	lbl.add_theme_font_size_override("font_size", s(size))
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
	style.content_margin_left = s(16)
	style.content_margin_right = s(16)
	style.content_margin_top = s(10)
	style.content_margin_bottom = s(10)
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

	btn.add_theme_font_size_override("font_size", s(font_size))
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
	style.content_margin_top = s(12)
	style.content_margin_bottom = s(12)
	style.content_margin_left = s(24)
	style.content_margin_right = s(24)
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

	btn.add_theme_font_size_override("font_size", s(font_size))
	btn.add_theme_font_override("font", font_title())
	btn.add_theme_color_override("font_color", TEXT_LIGHT)
	btn.add_theme_color_override("font_hover_color", GOLD_LIGHT)
	btn.add_theme_color_override("font_pressed_color", GOLD)


static func style_quick_button(btn: Button) -> void:
	## Styled button for in-game quick menu with text outline for readability.
	var style := StyleBoxFlat.new()
	style.bg_color = Color(0.06, 0.06, 0.09, 0.7)
	style.border_color = BORDER
	style.set_border_width_all(1)
	style.set_corner_radius_all(3)
	style.content_margin_left = s(16)
	style.content_margin_right = s(16)
	style.content_margin_top = s(10)
	style.content_margin_bottom = s(10)
	btn.add_theme_stylebox_override("normal", style)

	var hover := style.duplicate()
	hover.bg_color = Color(0.14, 0.11, 0.08, 0.88)
	hover.border_color = GOLD
	btn.add_theme_stylebox_override("hover", hover)

	var pressed := style.duplicate()
	pressed.bg_color = Color(0.04, 0.04, 0.06, 0.9)
	pressed.border_color = GOLD_LIGHT
	btn.add_theme_stylebox_override("pressed", pressed)

	var focus := style.duplicate()
	focus.border_color = GOLD_DIM
	btn.add_theme_stylebox_override("focus", focus)

	btn.add_theme_font_size_override("font_size", s(20))
	btn.add_theme_font_override("font", font_ui())
	btn.add_theme_color_override("font_color", TEXT_LIGHT)
	btn.add_theme_color_override("font_hover_color", GOLD_LIGHT)
	btn.add_theme_color_override("font_pressed_color", GOLD)

	# Text outline for readability over backgrounds
	btn.add_theme_constant_override("outline_size", s(3))
	btn.add_theme_color_override("font_outline_color", Color(0.0, 0.0, 0.0, 0.85))
