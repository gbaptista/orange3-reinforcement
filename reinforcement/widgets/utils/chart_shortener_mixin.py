from math import ceil

import numpy as np


class ChartShortenerMixin:
    def shorten_points(self, points, max_points=300,
                       first_and_last_values=True):
        if not points.size > max_points:
            return self.mapped_points(points)

        pages, per_page = self.pages_and_per_page(points, max_points,
                                                  first_and_last_values)

        shortened_points = {}

        if first_and_last_values:
            shortened_points[0] = points[:1][0]

            current_point = 1
        else:
            current_point = 0

        for _page in range(1, pages + 1):

            from_index, to_index = self.from_to_index(current_point,
                                                      points,
                                                      per_page,
                                                      first_and_last_values)

            actual_index = int(from_index + ((to_index - from_index) / 2))

            if from_index == to_index:
                sub_points = points[to_index]
            else:
                sub_points = points[from_index:to_index]

            page_value = np.sum(sub_points) / sub_points.size

            shortened_points[actual_index] = page_value

            current_point += per_page

        if first_and_last_values:
            shortened_points[points.size-1] = points[-1]

        return shortened_points

    @staticmethod
    def pages_and_per_page(points, max_points, first_and_last_values):
        if first_and_last_values:
            pages = max_points - 2
            per_page = ceil((points.size-2) / pages)
        else:
            pages = max_points
            per_page = ceil(points.size / pages)

        return (pages, per_page)

    @staticmethod
    def from_to_index(from_index, points, per_page, first_and_last_values):
        last_index_distance = 2 if first_and_last_values else 1

        if from_index >= points.size:
            from_index = points.size - last_index_distance

        to_index = from_index + per_page

        if to_index >= points.size:
            to_index = points.size - last_index_distance

        return (from_index, to_index)

    @staticmethod
    def mapped_points(points):
        mapped_points = {}

        for i, value in enumerate(points):
            mapped_points[i] = value

        return mapped_points
