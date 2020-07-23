from classes import *

########################
# EDIT BELOW THIS LINE #
########################

program_name = "Amazing Mirror Randomizer"
rom_name = "Kirby & The Amazing Mirror (USA)"
rom_file_format = "gba"

attributes = {
	"Sword Knight" : Attribute(
		name="Sword Knight",
		description="The ability given by Sword Knight",
		addresses=0x3518BE,
		min_value=0,
		max_value=26,
	),
	"Cupie" : Attribute(
		name="Cupie",
		description="The ability given by Cupie",
		addresses=0x35176E,
		min_value=0,
		max_value=26,
	),
}

required_rules = [
	Rule(
		name="Sword Knight and Cupie give the same ability",
		left_side=[attributes["Sword Knight"], attributes["Cupie"]],
		rule_type="==",
		right_side=None
	),
	# Rule(
	# 	name="Sword Knight is one more than Cupie",
	# 	left_side=attributes["Sword Knight"],
	# 	rule_type="==",
	# 	right_side=attributes["Cupie"]*2+1,
	# ),
	# Rule(
	# 	name="Sword Knight gives ability 5",
	# 	left_side=attributes["Sword Knight"],
	# 	rule_type="==",
	# 	right_side=10,
	# ),
]

optional_rulesets = {
	"My Rules 1" : [
		Rule(
			name="Sword Knight < 10",
			left_side=attributes["Sword Knight"],
			rule_type="<",
			right_side=10
		),
		Rule(
			name="Cupie >= 3",
			left_side=attributes["Cupie"],
			rule_type=">=",
			right_side=3
		),
	],
	"My Rules 2" : [
		Rule(
			name="Sword Knight > 12",
			left_side=attributes["Sword Knight"],
			rule_type=">",
			right_side=12
		),
		Rule(
			name="Cupie > 18",
			left_side=attributes["Cupie"],
			rule_type=">",
			right_side=18
		),
	],
	"My Rules 3" : [],
	"My Rules 4" : [],
	"My Rules 5" : [],
	"My Rules 6" : [],
	"My Rules 7" : [],
	"My Rules 8" : [],
	"My Rules 9" : [],
	"My Rules 10" : [],
}