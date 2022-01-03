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


    # This function receives a list of integers and finds the amount of maximum element
    def max_finder(self, input_list):
        if len(input_list) == 0:
            return 0
        max = input_list[0]
        i = 1
        while i < len(input_list):
            if input_list[i] > max:
                max = input_list[i]
            i += 1
        return max


    # This function infers according to the amounts of pa and pv
    def inference_function(self, input_pa_dict, input_pv_dict):
        stop_list = []
        left_fast_list = []
        left_slow_list = []
        right_fast_list = []
        right_slow_list = []

        # Rules:
        stop_list.append(max(min(input_pa_dict["up"], input_pv_dict["stop"]), min(input_pa_dict["up_right"], input_pv_dict["ccw_slow"]), min(input_pa_dict["up_left"], input_pv_dict["cw_slow"])))
        right_fast_list.append(min(input_pa_dict["up_more_right"], input_pv_dict["ccw_slow"]))
        right_fast_list.append(min(input_pa_dict["up_more_right"], input_pv_dict["cw_slow"]))
        left_fast_list.append(min(input_pa_dict["up_more_left"], input_pv_dict["cw_slow"]))
        left_fast_list.append(min(input_pa_dict["up_more_left"], input_pv_dict["ccw_slow"]))
        left_slow_list.append(min(input_pa_dict["up_more_right"], input_pv_dict["ccw_fast"]))
        right_fast_list.append(min(input_pa_dict["up_more_right"], input_pv_dict["cw_fast"]))
        right_slow_list.append(min(input_pa_dict["up_more_left"], input_pv_dict["cw_fast"]))
        left_fast_list.append(min(input_pa_dict["up_more_left"], input_pv_dict["ccw_fast"]))
        right_fast_list.append(min(input_pa_dict["down_more_right"], input_pv_dict["ccw_slow"]))
        stop_list.append(min(input_pa_dict["down_more_right"], input_pv_dict["cw_slow"]))
        left_fast_list.append(min(input_pa_dict["down_more_left"], input_pv_dict["cw_slow"]))
        stop_list.append(min(input_pa_dict["down_more_left"], input_pv_dict["ccw_slow"]))
        stop_list.append(min(input_pa_dict["down_more_right"], input_pv_dict["ccw_fast"]))
        stop_list.append(min(input_pa_dict["down_more_right"], input_pv_dict["cw_fast"]))
        stop_list.append(min(input_pa_dict["down_more_left"], input_pv_dict["cw_fast"]))
        stop_list.append(min(input_pa_dict["down_more_left"], input_pv_dict["ccw_fast"]))
        right_fast_list.append(min(input_pa_dict["down_right"], input_pv_dict["ccw_slow"]))
        right_fast_list.append(min(input_pa_dict["down_right"], input_pv_dict["cw_slow"]))
        left_fast_list.append(min(input_pa_dict["down_left"], input_pv_dict["cw_slow"]))
        left_fast_list.append(min(input_pa_dict["down_left"], input_pv_dict["ccw_slow"]))
        stop_list.append(min(input_pa_dict["down_right"], input_pv_dict["ccw_fast"]))
        right_slow_list.append(min(input_pa_dict["down_right"], input_pv_dict["cw_fast"]))
        stop_list.append(min(input_pa_dict["down_left"], input_pv_dict["cw_fast"]))
        left_slow_list.append(min(input_pa_dict["down_left"], input_pv_dict["ccw_fast"]))
        right_slow_list.append(min(input_pa_dict["up_right"], input_pv_dict["ccw_slow"]))
        right_fast_list.append(min(input_pa_dict["up_right"], input_pv_dict["cw_slow"]))
        right_fast_list.append(min(input_pa_dict["up_right"], input_pv_dict["stop"]))
        left_slow_list.append(min(input_pa_dict["up_left"], input_pv_dict["cw_slow"]))
        left_fast_list.append(min(input_pa_dict["up_left"], input_pv_dict["ccw_slow"]))
        left_fast_list.append(min(input_pa_dict["up_left"], input_pv_dict["stop"]))
        left_fast_list.append(min(input_pa_dict["up_right"], input_pv_dict["ccw_fast"]))
        right_fast_list.append(min(input_pa_dict["up_right"], input_pv_dict["cw_fast"]))
        right_fast_list.append(min(input_pa_dict["up_left"], input_pv_dict["cw_fast"]))
        left_fast_list.append(min(input_pa_dict["up_left"], input_pv_dict["ccw_fast"]))
        right_fast_list.append(min(input_pa_dict["down"], input_pv_dict["stop"]))
        stop_list.append(min(input_pa_dict["down"], input_pv_dict["cw_fast"]))
        stop_list.append(min(input_pa_dict["down"], input_pv_dict["ccw_fast"]))
        left_slow_list.append(min(input_pa_dict["up"], input_pv_dict["ccw_slow"]))
        left_fast_list.append(min(input_pa_dict["up"], input_pv_dict["ccw_fast"]))
        right_slow_list.append(min(input_pa_dict["up"], input_pv_dict["cw_slow"]))
        right_fast_list.append(min(input_pa_dict["up"], input_pv_dict["cw_fast"]))
        stop_list.append(min(input_pa_dict["up"], input_pv_dict["stop"]))
        output_dictionary = {}
        output_dictionary["stop"] = self.max_finder(stop_list)
        output_dictionary["left_fast"] = self.max_finder(left_fast_list)
        output_dictionary["left_slow"] = self.max_finder(left_slow_list)
        output_dictionary["right_fast"] = self.max_finder(right_fast_list)
        output_dictionary["right_slow"] = self.max_finder(right_slow_list)
        return output_dictionary


    # This function gets the number of needed points between -100 and 100 and returns a list of them
    def points_generator(self, number_of_points):
        output_list = []
        temp = -100.
        i = 1
        while i <= number_of_points:
            output_list.append(temp + (200. / number_of_points))
            temp = temp + (200. / number_of_points)
            i += 1
        return output_list


    # This function calculates the amount of input_point in stop set of force
    def stop_func(self, input_point, stop_max):
        if -60 <= input_point <= 60:
            if input_point < 0:
                main_stop_result = (input_point / 60) + 1
            if input_point == 0:
                main_stop_result = 1
            if input_point > 0:
                main_stop_result = - (input_point / 60) + 1

            if main_stop_result >= stop_max:
                return stop_max
            else:
                return main_stop_result

        else:
            return 0

    # This function calculates the amount of input_point in left_fast set of force
    def left_fast_func(self, input_point, left_fast_max):
        if -100 <= input_point <= -60:
            if input_point < -80:
                main_stop_result = (input_point / 20) + 5
            if input_point == -80:
                main_stop_result = 1
            if input_point > -80:
                main_stop_result = - (input_point / 20) - 3

            if main_stop_result >= left_fast_max:
                return left_fast_max
            else:
                return main_stop_result

        else:
            return 0

    # This function calculates the amount of input_point in left_slow set of force
    def left_slow_func(self, input_point, left_slow_max):
        if -80 <= input_point <= 0:
            if input_point < -60:
                main_stop_result = (input_point / 20) + 4
            if input_point == -60:
                main_stop_result = 1
            if input_point > -60:
                main_stop_result = - (input_point / 60)

            if main_stop_result >= left_slow_max:
                return left_slow_max
            else:
                return main_stop_result

        else:
            return 0

    # This function calculates the amount of input_point in right_slow set of force
    def right_slow_func(self, input_point, right_slow_max):
        if 0 <= input_point <= 80:
            if input_point < 60:
                main_stop_result = (input_point / 60)
            if input_point == 60:
                main_stop_result = 1
            if input_point > 60:
                main_stop_result = - (input_point / 20) + 4

            if main_stop_result >= right_slow_max:
                return right_slow_max
            else:
                return main_stop_result

        else:
            return 0


    # This function calculates the amount of input_point in right_fast set of force
    def right_fast_func(self, input_point, right_fast_max):
        if 60 <= input_point <= 100:
            if input_point < 60:
                main_stop_result = (input_point / 20) - 3
            if input_point == 60:
                main_stop_result = 1
            if input_point > 60:
                main_stop_result = - (input_point / 20) + 5

            if main_stop_result >= right_fast_max:
                return right_fast_max
            else:
                return main_stop_result

        else:
            return 0


    # This function calculates the final amount of force by integration
    def integration_calculator(self, input_force_dict, num_of_points):
        points_list = self.points_generator(num_of_points)
        print(points_list)
        results_list = []
        for point in points_list:
            results_list.append(max(self.stop_func(point, input_force_dict["stop"]), self.left_fast_func(point, input_force_dict["left_fast"]), self.left_slow_func(point, input_force_dict["left_slow"]), self.right_fast_func(point, input_force_dict["right_fast"]), self.right_slow_func(point, input_force_dict["right_slow"])))
        i = 0
        a = 0
        b = 0
        while i < num_of_points:
            a += points_list[i] * results_list[i]
            b += results_list[i]
            i += 1
        return a / b


    def decide(self, world):
        new_world = self._make_input(world)
        pa = new_world["pa"]
        pv = new_world["pv"]
        pa_dictionary = self.pa_calculator(pa)
        pv_dictionary = self.pv_calculator(pv)
        force_dictionary = self.inference_function(pa_dictionary, pv_dictionary)
        number_of_points = 1000.    # This point must be here because of the error of python 2.7.16 interpreter in calculating floating points
        my_result = self.integration_calculator(force_dictionary, number_of_points)
        return max(force_dictionary["stop"], force_dictionary["left_fast"], force_dictionary["right_fast"], force_dictionary["left_slow"], force_dictionary["right_slow"])








