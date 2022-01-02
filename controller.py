# -*- coding: utf-8 -*-

# python imports
from math import degrees

# pyfuzzy imports
from fuzzy.storage.fcl.Reader import Reader


class FuzzyController:

    def __init__(self, fcl_path):
        self.system = Reader().load_from_file(fcl_path)


    def _make_input(self, world):
        return dict(
            cp = world.x,
            cv = world.v,
            pa = degrees(world.theta),
            pv = degrees(world.omega)
        )


    def _make_output(self):
        return dict(
            force = 0.
        )


    # This function receives the amount of pa as input an returns a dictionary of pa amounts in different sets
    def pa_calculator(self, input_pa):
        output_dictionary = {}
        # Calculating up_more_right value
        if 0 <= input_pa <= 60:
           if 30 > input_pa:
               up_more_right_value = input_pa / 30
           if 30 == input_pa:
               up_more_right_value = 1
           if 30 < input_pa:
                up_more_right_value = - (input_pa / 30) + 2
        else:
            up_more_right_value = 0
        output_dictionary["up_more_right"] = up_more_right_value

        # Calculating up_right value
        if 30 <= input_pa <= 90:
           if 60 > input_pa:
               up_right_value = (input_pa / 30) - 1
           if 60 == input_pa:
               up_right_value = 1
           if 60 < input_pa:
                up_right_value = - (input_pa / 30) + 3
        else:
            up_right_value = 0

        output_dictionary["up_right"] = up_right_value

        # Calculating up value
        if 60 <= input_pa <= 120:
           if 90 > input_pa:
               up_value = (input_pa / 30) - 2
           if 90 == input_pa:
               up_value = 1
           if 90 < input_pa:
                up_value = - (input_pa / 30) + 4
        else:
            up_value = 0

        output_dictionary["up"] = up_value

        # Calculating up_left value
        if 90 <= input_pa <= 150:
           if 120 > input_pa:
               up_left_value = (input_pa / 30) - 3
           if 120 == input_pa:
               up_left_value = 1
           if 120 < input_pa:
                up_left_value = - (input_pa / 30) + 5
        else:
            up_left_value = 0

        output_dictionary["up_left"] = up_left_value

        # Calculating up_more_left value
        if 120 <= input_pa <= 180:
           if 150 > input_pa:
               up_more_left_value = (input_pa / 30) - 4
           if 150 == input_pa:
               up_more_left_value = 1
           if 150 < input_pa:
                up_more_left_value = - (input_pa / 30) + 6
        else:
            up_more_left_value = 0

        output_dictionary["up_more_left"] = up_more_left_value





    def decide(self, world):
        new_world = self._make_input(world)
        pa = new_world["pa"]
        pv = new_world["pv"]
        pa_dictionary = pa_calculator(pa)
        pv_dictionary = pv_calculator(pv)









        # return 2
       # output = self._make_output()
       # self.system.calculate(self._make_input(world), output)
       # return output['force']
