# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,R0801

from __future__ import annotations

from .style import Style


class D2M1:
    # pylint: disable=too-few-public-methods

    @staticmethod
    def get(dimension1: str, dimension2: str, measure1: str) -> list:
        return [
            {
                "config": {
                    "coordSystem": "cartesian",
                    "geometry": "rectangle",
                    "x": [dimension1, dimension2],
                    "y": {"set": measure1, "range": {"min": None, "max": "110%"}},
                    "color": dimension2,
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "horizontal",
                },
                "style": Style.style(),
                "chart": "Grouped Column Chart",
            },
            {
                "config": {
                    "coordSystem": "cartesian",
                    "geometry": "rectangle",
                    "x": [dimension2, dimension1],
                    "y": {"set": measure1, "range": {"min": None, "max": "110%"}},
                    "color": dimension2,
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "horizontal",
                },
                "style": Style.style(),
                "chart": "Grouped Column Chart V2",
            },
            {
                "config": {
                    "coordSystem": "cartesian",
                    "geometry": "rectangle",
                    "x": dimension1,
                    "y": {
                        "set": [dimension2, measure1],
                        "range": {"min": None, "max": "110%"},
                    },
                    "color": dimension2,
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "horizontal",
                },
                "style": Style.style(),
                "chart": "Stacked Column Chart",
            },
            {
                "config": {
                    "coordSystem": "cartesian",
                    "geometry": "rectangle",
                    "x": dimension1,
                    "y": {
                        "set": [dimension2, measure1],
                        "range": {"min": None, "max": "110%"},
                    },
                    "color": dimension2,
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": True,
                    "align": "none",
                    "orientation": "horizontal",
                },
                "style": Style.style(),
                "chart": "Splitted Column Chart",
            },
            {
                "config": {
                    "coordSystem": "cartesian",
                    "geometry": "rectangle",
                    "x": dimension1,
                    "y": {
                        "set": [dimension2, measure1],
                        "range": {"min": None, "max": None},
                    },
                    "color": dimension2,
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "stretch",
                    "orientation": "horizontal",
                },
                "style": Style.style(),
                "chart": "100% Stacked Column Chart",
            },
            {
                "config": {
                    "coordSystem": "cartesian",
                    "geometry": "rectangle",
                    "x": measure1,
                    "y": {
                        "set": [dimension1, dimension2],
                        "range": {"min": None, "max": None},
                    },
                    "color": dimension2,
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "vertical",
                },
                "style": Style.style(),
                "chart": "Grouped Bar Chart",
            },
            {
                "config": {
                    "coordSystem": "cartesian",
                    "geometry": "rectangle",
                    "x": measure1,
                    "y": {
                        "set": [dimension2, dimension1],
                        "range": {"min": None, "max": None},
                    },
                    "color": dimension2,
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "vertical",
                },
                "style": Style.style(),
                "chart": "Grouped Bar Chart V2",
            },
            {
                "config": {
                    "coordSystem": "cartesian",
                    "geometry": "rectangle",
                    "x": [dimension2, measure1],
                    "y": {"set": dimension1, "range": {"min": None, "max": None}},
                    "color": dimension2,
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "vertical",
                },
                "style": Style.style(),
                "chart": "Stacked Bar Chart",
            },
            {
                "config": {
                    "coordSystem": "cartesian",
                    "geometry": "rectangle",
                    "x": [dimension2, measure1],
                    "y": {"set": dimension1, "range": {"min": None, "max": None}},
                    "color": dimension2,
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": True,
                    "align": "none",
                    "orientation": "vertical",
                },
                "style": Style.style(),
                "chart": "Splitted Bar Chart",
            },
            {
                "config": {
                    "coordSystem": "cartesian",
                    "geometry": "rectangle",
                    "x": [dimension2, measure1],
                    "y": {"set": dimension1, "range": {"min": None, "max": None}},
                    "color": dimension2,
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "stretch",
                    "orientation": "horizontal",
                },
                "style": Style.style(),
                "chart": "100% Stacked Bar Chart",
            },
            {
                "config": {
                    "coordSystem": "cartesian",
                    "geometry": "line",
                    "x": dimension1,
                    "y": {"set": measure1, "range": {"min": None, "max": "110%"}},
                    "color": dimension2,
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "horizontal",
                },
                "style": Style.style(),
                "chart": "Line Chart",
            },
            {
                "config": {
                    "coordSystem": "cartesian",
                    "geometry": "area",
                    "x": dimension1,
                    "y": {
                        "set": [dimension2, measure1],
                        "range": {"min": None, "max": "110%"},
                    },
                    "color": dimension2,
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "horizontal",
                },
                "style": Style.style(),
                "chart": "Stacked Area Chart",
            },
            {
                "config": {
                    "coordSystem": "cartesian",
                    "geometry": "area",
                    "x": dimension1,
                    "y": {
                        "set": [dimension2, measure1],
                        "range": {"min": None, "max": None},
                    },
                    "color": dimension2,
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "stretch",
                    "orientation": "horizontal",
                },
                "style": Style.style(),
                "chart": "100% Stacked Area Chart",
            },
            {
                "config": {
                    "coordSystem": "cartesian",
                    "geometry": "area",
                    "x": dimension1,
                    "y": {
                        "set": [dimension2, measure1],
                        "range": {"min": None, "max": None},
                    },
                    "color": dimension2,
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": True,
                    "align": "none",
                    "orientation": "horizontal",
                },
                "style": Style.style(),
                "chart": "Ridgeline Plot",
            },
            {
                "config": {
                    "coordSystem": "cartesian",
                    "geometry": "area",
                    "x": dimension1,
                    "y": {
                        "set": [dimension2, measure1],
                        "range": {"min": None, "max": "110%"},
                    },
                    "color": dimension2,
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "center",
                    "orientation": "horizontal",
                },
                "style": Style.style(),
                "chart": "Stream Graph",
            },
            {
                "config": {
                    "coordSystem": "cartesian",
                    "geometry": "area",
                    "x": dimension1,
                    "y": {
                        "set": [dimension2, measure1],
                        "range": {"min": None, "max": "110%"},
                    },
                    "color": dimension2,
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": True,
                    "align": "center",
                    "orientation": "horizontal",
                },
                "style": Style.style(),
                "chart": "Violin Graph",
            },
            {
                "config": {
                    "coordSystem": "cartesian",
                    "geometry": "circle",
                    "x": None,
                    "y": {"set": None, "range": {"min": None, "max": None}},
                    "color": dimension2,
                    "lightness": None,
                    "size": [dimension1, measure1],
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "horizontal",
                },
                "style": Style.style(),
                "chart": "Stacked Bubble Chart",
            },
            {
                "config": {
                    "coordSystem": "polar",
                    "geometry": "rectangle",
                    "x": dimension1,
                    "y": {
                        "set": [dimension2, measure1],
                        "range": {"min": None, "max": None},
                    },
                    "color": dimension2,
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "horizontal",
                },
                "style": Style.style(),
                "chart": "Polar Stacked Column Chart",
            },
            {
                "config": {
                    "coordSystem": "polar",
                    "geometry": "area",
                    "x": dimension1,
                    "y": {
                        "set": [dimension2, measure1],
                        "range": {"min": None, "max": None},
                    },
                    "color": dimension2,
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "horizontal",
                },
                "style": Style.style(),
                "chart": "Polar Stacked Area Chart",
            },
            {
                "config": {
                    "coordSystem": "polar",
                    "geometry": "rectangle",
                    "x": [dimension2, measure1],
                    "y": {"set": dimension1, "range": {"min": "-50%", "max": None}},
                    "color": dimension2,
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "vertical",
                },
                "style": Style.style(),
                "chart": "Radial Stacked Bar Chart",
            },
            {
                "config": {
                    "coordSystem": "polar",
                    "geometry": "rectangle",
                    "x": [dimension2, measure1],
                    "y": {"set": dimension1, "range": {"min": "-50%", "max": None}},
                    "color": dimension2,
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "stretch",
                    "orientation": "vertical",
                },
                "style": Style.style_nesteddonut(),
                "chart": "Nested Donut Chart",
            },
            {
                "config": {
                    "coordSystem": "cartesian",
                    "geometry": "rectangle",
                    "x": dimension1,
                    "y": {"set": dimension2, "range": {"min": None, "max": None}},
                    "color": None,
                    "lightness": measure1,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "horizontal",
                },
                "style": Style.style_heatmap(),
                "chart": "Heat Map",
            },
            {
                "config": {
                    "coordSystem": "cartesian",
                    "geometry": "rectangle",
                    "x": dimension1,
                    "y": {"set": dimension2, "range": {"min": None, "max": None}},
                    "color": measure1,
                    "lightness": None,
                    "size": None,
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "horizontal",
                },
                "style": Style.style_heatmap(),
                "chart": "Heat Map Gradient",
            },
        ]
