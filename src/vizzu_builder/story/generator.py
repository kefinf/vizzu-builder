# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

from __future__ import annotations

import black
import streamlit as st
from streamlit_extras.row import row  # type: ignore
from ipyvizzustory.env.st.story import Story
from ipyvizzustory import Slide, Step
from streamlit_vizzu import Config, Data, Style  # type: ignore

from ..chart.configurator import SelectedChartConfig
from ..config.presets import Preset
from ..data.configurator import DataConfig
from ..data.generator import DataGenerator
from .configurator import StoryConfig


class StoryGenerator:
    def __init__(self) -> None:
        self._data = st.session_state.get("BuilderData", DataConfig())
        if "BuilderStory" not in st.session_state:
            st.session_state["BuilderStory"] = StoryConfig(self._data)
        self._story = st.session_state["BuilderStory"]

        self._width = 640
        self._height = 320
        self._start_slide = -1
        if not self._data.df.empty:
            if self._story.data.df.empty:
                self._story.data = self._data
            if self._story.story is None or not self._story.data.df.equals(
                self._data.df
            ):
                self._story.data = self._data
                data = Data()
                data.add_df(self._data.df)
                self._story.story = Story(data=data)
                self.set_size(self._width, self._height)
                self.set_start_slide(self._start_slide)
                self._story.code = []

    def set_start_slide(self, index: int) -> None:
        self._story.story.start_slide = index

    def set_size(self, width: int, height: int) -> None:
        self._story.story.set_size(width, height)

    def add_slide(self, preset: Preset) -> None:
        filters = self._data.filters
        self._story.story.add_slide(
            Slide(
                Step(Data.filter(filters), Config(preset.config), Style(preset.style))
            )
        )
        filters = f'"{filters}"' if filters else None
        animation = (
            f"Data.filter({filters}), Config({preset.config}), Style({preset.style})"
        )
        self._story.code.append(f"story.add_slide(Slide(Step({animation})))")

    def play(self) -> None:
        if self._story.story is not None and self._story.story["slides"]:
            st.subheader("Story")
            self._story.story.set_feature("tooltip", self._get_tooltip())
            self._story.story.play()
            rows = row(2)
            self._add_delete_button(rows)
            self._add_download_button(rows)
            self._add_show_code_button()

    def _get_tooltip(self) -> bool:
        return st.session_state.get("BuilderConfig", SelectedChartConfig()).tooltip  # type: ignore

    def _add_delete_button(self, rows) -> None:  # type: ignore
        if self._story.story is not None and self._story.story["slides"]:
            rows.button(
                "Delete last Slide",
                use_container_width=True,
                on_click=self._delete_last_slide,
            )

    def _delete_last_slide(self) -> None:
        if (
            self._story.story is not None
            and self._story.story["slides"]
            and self._story.code
        ):
            self._story.story["slides"].pop()
            self._story.code.pop()

    def _add_download_button(self, rows) -> None:  # type: ignore
        if self._story.story is not None:
            self.set_start_slide(0)
            rows.download_button(
                label="Download Story",
                data=self._story.story.to_html(),
                file_name="story.html",
                mime="text/html",
                use_container_width=True,
            )
            self.set_start_slide(self._start_slide)

    def _add_show_code_button(self) -> None:
        if self._story.story is not None and self._story.code:
            show_code = st.expander("Show code")
            with show_code:
                st.code(
                    self._get_code(),
                    language="python",
                )

    def _get_code(self) -> str:
        if self._story.story is not None and self._story.code:
            code = []
            code.append("import pandas as pd")
            code.append("from ipyvizzu import Config, Data, Style")
            code.append("from ipyvizzustory import Story, Slide, Step")
            code += DataGenerator.get(self._data)
            code.append("story = Story(data)")
            code.append(f"story.set_size({self._width}, {self._height})")
            code.append(f'story.set_feature("tooltip", {self._get_tooltip()})\n')
            unformatted_code = "\n".join(code + self._story.code + ["\nstory.play()"])
            formatted_code = black.format_str(unformatted_code, mode=black.FileMode())
            return formatted_code
        return ""