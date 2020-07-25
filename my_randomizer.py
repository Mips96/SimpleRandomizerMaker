# This is a randomizer file for the Simple Randomizer Maker.
# This file must be named my_randomizer.py in order to work.

from classes import *

def value(name):
	for att in attributes:
		if att.name == name:
			return att
	print("This attribute does not exist: "+name)
	return None

########################
# EDIT BELOW THIS LINE #
########################

program_name = "Amazing Mirror Randomizer"
rom_name = "Kirby & The Amazing Mirror (USA)"
rom_file_format = "gba"
about_page_text = "This is a sample randomizer for Kirby & The Amazing Mirror that changes the abilities given by a few enemies (specifically, the ones in the first area of the game)."

attributes = [
	Attribute(
		name="Waddle Dee",
		addresses=[0x35164E, 0x351B76],
		min_value=0,
		max_value=26,
	),
	Attribute(
		name="Droppy",
		addresses=[0x351AFE, 0x3527D6],
		min_value=0,
		max_value=26,
	),
	Attribute(
		name="Leap",
		addresses=0x3517B6,
		min_value=0,
		max_value=26,
	),
	Attribute(
		name="Big Waddle Dee",
		addresses=0x3517E6,
		min_value=0,
		max_value=26,
	),
	Attribute(
		name="Flamer",
		addresses=0x351816,
		min_value=0,
		max_value=26,
	),
	Attribute(
		name="Sword Knight",
		addresses=0x3518BE,
		min_value=0,
		max_value=26,
	),
	Attribute(
		name="Cupie",
		addresses=0x35176E,
		min_value=0,
		max_value=26,
	),
]

required_rules = [
]

optional_rulesets = [
	Ruleset(
		name="All Enemies Give An Ability",
		description="All enemies are guaranteed to give an ability.",
		rules=[
			Rule(
				description="All Enemies Give An Ability",
				left_side=[value("Waddle Dee"), value("Droppy"), value("Leap"), value("Big Waddle Dee"), value("Flamer"), value("Sword Knight"), value("Cupie")].count(0),
				rule_type="==",
				right_side=0,
			),
		],
		must_be_disabled="All Master",
	),
	Ruleset(
		name="All Unique",
		description="All enemies give different abilities.",
		rules=[
			Rule(
				description="All Unique",
				left_side=[value("Waddle Dee"), value("Droppy"), value("Leap"), value("Big Waddle Dee"), value("Flamer"), value("Sword Knight"), value("Cupie")],
				rule_type="!=",
				right_side=None,
			),
		],
		must_be_disabled="All Master",
	),
	Ruleset(
		name="All Master",
		description="All enemies give the Master ability (ability #26).",
		rules=[
			Rule(
				description="Waddle Dee gives Master",
				left_side=value("Waddle Dee"),
				rule_type="==",
				right_side=26,
			),
			Rule(
				description="All enemies give the same ability (by extension, they all give Master)",
				left_side=[value("Waddle Dee"), value("Droppy"), value("Leap"), value("Big Waddle Dee"), value("Flamer"), value("Sword Knight"), value("Cupie")],
				rule_type="==",
				right_side=None,
			),
		],
		must_be_disabled=["All Unique", "At Least 1 UFO"],
	),
	Ruleset(
		name="At Least 1 UFO",
		description="At least one enemy gives the UFO ability (ability #14).",
		rules=[
			Rule(
				description="At Least 1 UFO",
				left_side=[value("Waddle Dee"), value("Droppy"), value("Leap"), value("Big Waddle Dee"), value("Flamer"), value("Sword Knight"), value("Cupie")].count(0x0E),
				rule_type=">=",
				right_side=1,
			),
		],
		must_be_disabled="All Master",
	),
	Ruleset(
		name="All Different From Original",
		description="All enemies are guaranteed to give different abilities from what they usually give.",
		rules=[
			Rule(
				description="Waddle Dee is different",
				left_side=value("Waddle Dee"),
				rule_type="!=",
				right_side=0,
			),
			Rule(
				description="Droppy is different",
				left_side=value("Droppy"),
				rule_type="!=",
				right_side=0,
			),
			Rule(
				description="Leap is different",
				left_side=value("Leap"),
				rule_type="!=",
				right_side=0,
			),
			Rule(
				description="Big Waddle Dee is different",
				left_side=value("Big Waddle Dee"),
				rule_type="!=",
				right_side=0,
			),
			Rule(
				description="Flamer is different",
				left_side=value("Flamer"),
				rule_type="!=",
				right_side=3,
			),
			Rule(
				description="Sword Knight is different",
				left_side=value("Sword Knight"),
				rule_type="!=",
				right_side=0x12,
			),
			Rule(
				description="Cupie is different",
				left_side=value("Cupie"),
				rule_type="!=",
				right_side=0x13,
			),
		],
		must_be_disabled="All Master",
	),
	Ruleset(
		name="Smashing!",
		description="All enemies give either Smash, Fighting, Stone, Cutter, or Hammer.",
		rules=[
			Rule(
				description="Waddle Dee is smashing",
				left_side=value("Waddle Dee"),
				rule_type="==",
				right_side=[0x16, 0x14, 0x8, 0x6, 0x11],
			),
			Rule(
				description="Droppy is smashing",
				left_side=value("Droppy"),
				rule_type="==",
				right_side=[0x16, 0x14, 0x8, 0x6, 0x11],
			),
			Rule(
				description="Leap is smashing",
				left_side=value("Leap"),
				rule_type="==",
				right_side=[0x16, 0x14, 0x8, 0x6, 0x11],
			),
			Rule(
				description="Big Waddle Dee is smashing",
				left_side=value("Big Waddle Dee"),
				rule_type="==",
				right_side=[0x16, 0x14, 0x8, 0x6, 0x11],
			),
			Rule(
				description="Flamer is smashing",
				left_side=value("Flamer"),
				rule_type="==",
				right_side=[0x16, 0x14, 0x8, 0x6, 0x11],
			),
			Rule(
				description="Sword Knight is smashing",
				left_side=value("Sword Knight"),
				rule_type="==",
				right_side=[0x16, 0x14, 0x8, 0x6, 0x11],
			),
			Rule(
				description="Cupie is smashing",
				left_side=value("Cupie"),
				rule_type="==",
				right_side=[0x16, 0x14, 0x8, 0x6, 0x11],
			),
		],
		must_be_disabled=["All Master", "At Least 1 UFO"],
	),
]