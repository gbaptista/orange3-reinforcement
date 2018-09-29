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

        current_point = 0

        if first_and_last_values:
            shortened_points[0] = points[:1][0]
            current_point += 1

        for _page in range(1, pages + 1):
            from_index, to_index = self.from_to_index(current_point,
                                                      points,
                                                      per_page,
                                                      first_and_last_values)

            actual_index, page_value = self.page_index_and_value(from_index,
                                                                 to_index,
                                                                 points)

            shortened_points[actual_index] = page_value

            current_point += per_page

        if first_and_last_values:
            shortened_points[points.size-1] = points[-1]

        return shortened_points

    def page_index_and_value(self, from_index, to_index, points):
        actual_index = int(from_index + ((to_index - from_index) / 2))

        sub_points = self.points_from_to(from_index, to_index, points)

        page_value = np.sum(sub_points) / sub_points.size

        return (actual_index, page_value)

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
    def points_from_to(from_index, to_index, points):
        if from_index == to_index:
            return points[to_index]

        return points[from_index:to_index]

    @staticmethod
    def mapped_points(points):
        mapped_points = {}

        for i, value in enumerate(points):
            mapped_points[i] = value

        return mapped_points
