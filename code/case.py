class Case:
	def __init__(self, row):
		self._create(row)

	def _create(self, row):
		self.param = dict(
			sex = row[0],
			age = row[1],
			location_pain_beginning = row[2],
			location_pain_now = row[3],
			intensity_of_pain = row[4],
			factors_increasing_pain = row[5],
			factors_bringing_relief = row[6],
			progression_of_pain = row[7],
			duration_of_pain = row[8],
			nature_pain_beginning = row[9],
			nature_pain_now = row[10],
			nausea_and_vomiting = row[11],
			appetite = row[12],
			bowel_movements = row[13],
			urination = row[14],
			previous_indigestion = row[15],
			jaundice_in_past = row[16],
			previous_abdominal_operations = row[18],
			medicines = row[19],
			mental_state = row[20],
			skin = row[21],
			temperature_under_the_armpit = row[22],
			pulse = row[23],
			respiratory_movements_of_the_abdominal_wall = row[25],
			flatulence = row[26],
			location_of_pressure_soreness = row[27],
			blumberg_symptom = row[28],
			muscle_defense = row[29],
			increased_tension_of_abdominal_wall = row[30],
			pathological_resistance = row[31],
			murphy_sign = row[32],
			diagnosis_classes = row[33]
		)

	def __str__(self):
		return "Płeć: {0}, " \
		       "Wiek: {1}, " \
		       "Lokalizacja bólu na początku zachorowania: {2}" \
		       "".format(self.param.get('sex'),
		                 self.param.get('age'),
		                 self.param.get('location_pain_beginning'))
