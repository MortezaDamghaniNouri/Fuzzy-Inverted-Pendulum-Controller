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

        # Calculating down_more_left value
        if 180 <= input_pa <= 240:
           if 210 > input_pa:
               down_more_left_value = (input_pa / 30) - 6
           if 210 == input_pa:
               down_more_left_value = 1
           if 210 < input_pa:
                down_more_left_value = - (input_pa / 30) + 8
        else:
            down_more_left_value = 0

        output_dictionary["down_more_left"] = down_more_left_value

        # Calculating down_left value
        if 210 <= input_pa <= 270:
           if 240 > input_pa:
               down_left_value = (input_pa / 30) - 7
           if 240 == input_pa:
               down_left_value = 1
           if 240 < input_pa:
                down_left_value = - (input_pa / 30) + 9
        else:
            down_left_value = 0

        output_dictionary["down_left"] = down_left_value

        # Calculating down value
        if 240 <= input_pa <= 300:
           if 270 > input_pa:
               down_value = (input_pa / 30) - 8
           if 270 == input_pa:
               down_value = 1
           if 270 < input_pa:
                down_value = - (input_pa / 30) + 10
        else:
            down_value = 0

        output_dictionary["down"] = down_value

        # Calculating down_right value
        if 270 <= input_pa <= 330:
           if 300 > input_pa:
               down_right_value = (input_pa / 30) - 9
           if 300 == input_pa:
               down_right_value = 1
           if 300 < input_pa:
                down_right_value = - (input_pa / 30) + 11
        else:
            down_right_value = 0

        output_dictionary["down_right"] = down_right_value

        # Calculating down_more_right value
        if 300 <= input_pa <= 360:
           if 330 > input_pa:
               down_more_right_value = (input_pa / 30) - 10
           if 330 == input_pa:
               down_more_right_value = 1
           if 330 < input_pa:
                down_more_right_value = - (input_pa / 30) + 12
        else:
            down_more_right_value = 0

        output_dictionary["down_more_right"] = down_more_right_value

        return output_dictionary


    # This function receives the amount of pv as input an returns a dictionary of pv amounts in different sets
    def pv_calculator(self, input_pv):
        output_dictionary = {}
        # Calculating cw_fast
        if -200 <= input_pv <= -100:
            cw_fast_value = (- 0.01 * input_pv) - 1
        else:
            cw_fast_value = 0
        output_dictionary["cw_fast"] = cw_fast_value

        # Calculating cw_slow
        if -200 <= input_pv <= 0:
            if input_pv < -100:
                cw_slow_value = (0.01 * input_pv) + 2
            if input_pv == -100:
                cw_slow_value = 1
            if -100 < input_pv:
                cw_slow_value = - 0.01 * input_pv
        else:
            cw_slow_value = 0
        output_dictionary["cw_slow"] = cw_slow_value

        # Calculating stop
        if -100 <= input_pv <= 100:
            if input_pv < 0:
                stop_value = (0.01 * input_pv) + 1
            if input_pv == 0:
                stop_value = 1
            if 0 < input_pv:
                stop_value = (- 0.01 * input_pv) + 1
        else:
            stop_value = 0
        output_dictionary["stop"] = stop_value

        # Calculating ccw_slow
        if 0 <= input_pv <= 200:
            if input_pv < 100:
                ccw_slow_value = (0.01 * input_pv)
            if input_pv == 100:
                ccw_slow_value = 1
            if 100 < input_pv:
                ccw_slow_value = (- 0.01 * input_pv) + 2
        else:
            ccw_slow_value = 0
        output_dictionary["ccw_slow"] = ccw_slow_value

        # Calculating ccw_fast
        if 100 <= input_pv <= 200:
            ccw_fast_value = (0.01 * input_pv) - 1
        else:
            ccw_fast_value = 0
        output_dictionary["ccw_fast"] = ccw_fast_value

        return output_dictionary


    def decide(self, world):
        new_world = self._make_input(world)
        pa = new_world["pa"]
        pv = new_world["pv"]
        pa_dictionary = self.pa_calculator(pa)
        pv_dictionary = self.pv_calculator(pv)









        # return 2
       # output = self._make_output()
       # self.system.calculate(self._make_input(world), output)
       # return output['force']
