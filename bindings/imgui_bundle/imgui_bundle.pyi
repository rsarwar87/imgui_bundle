"""
"""

from typing import Tuple
import numpy as np
import enum

from imgui_bundle.hello_imgui import RunnerParams
from imgui_bundle.imgui_md import MarkdownOptions
from imgui_bundle.imgui_node_editor import Config as NodeEditorConfig


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# <litgen_stub> // Autogenerated code below! Do not edit!
####################    <generated_from:imgui_bundle.h>    ####################
# ///////////////////////////////////////////////////////////////////////////////////////
#
# Helper to run an app with "named params emulation" in C++
# (call it using designated initializers!)
#
# /////////////////////////////////////////////////////////////////////////////////////

class AddOnsParams:
    with_implot: bool = False
    with_markdown: bool = False
    with_node_editor: bool = False
    with_node_editor_config: Optional[NodeEditorConfig] = None
    with_markdown_options: Optional[ImGuiMd.MarkdownOptions] = None

def run(
    runner_params: HelloImGui.RunnerParams,
    add_ons_params: AddOnsParams = AddOnsParams(),
) -> None:
    pass

def run(
    simple_params: HelloImGui.SimpleRunnerParams,
    add_ons_params: AddOnsParams = AddOnsParams(),
) -> None:
    pass

# ///////////////////////////////////////////////////////////////////////////////////////
#
# Helpers to run an app from Python (using named parameters)
#
# /////////////////////////////////////////////////////////////////////////////////////

def clock_seconds() -> float:
    pass

def current_node_editor_context() -> ax.NodeEditor.EditorContext:
    pass
####################    </generated_from:imgui_bundle.h>    ####################

# </litgen_stub> // Autogenerated code end!
